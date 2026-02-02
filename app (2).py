import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
model = joblib.load('extra_trees_credit_model.pkl')

# Load the target encoder for inverse transformation
le_target = joblib.load('target_.encoder.pkl')

# Define DummyEncoders for categorical features based on the training data's unique values
class DummyEncoder:
    def __init__(self, categories):
        self.categories_ = categories
        self.mapping = {v: i for i, v in enumerate(categories)}

    def transform(self, values):
        # Ensure all values to transform are in the mapping
        for v in values:
            if v not in self.mapping:
                raise ValueError(f"Category '{v}' not found in encoder categories: {self.categories_}")
        return [self.mapping[v] for v in values]

# Re-create dummy encoders for categorical features based on the unique values identified earlier in the notebook
sex_encoder = DummyEncoder(categories=['female', 'male'])
housing_encoder = DummyEncoder(categories=['free', 'own', 'rent'])
saving_accounts_encoder = DummyEncoder(categories=['little', 'moderate', 'quite rich', 'rich'])
checking_account_encoder = DummyEncoder(categories=['little', 'moderate', 'rich'])

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        # Prepare input data for prediction
        age = data['Age']
        sex = data['Sex']
        job = data['Job']
        housing = data['Housing']
        saving_accounts = data['Saving accounts']
        checking_account = data['Checking account']
        credit_amount = data['Credit amount']
        duration = data['Duration']

        # Encode categorical features
        encoded_sex = sex_encoder.transform([sex])[0]
        encoded_housing = housing_encoder.transform([housing])[0]
        encoded_saving_accounts = saving_accounts_encoder.transform([saving_accounts])[0]
        encoded_checking_account = checking_account_encoder.transform([checking_account])[0]

        # Create a DataFrame for the model input
        input_df = pd.DataFrame([[
            age, encoded_sex, job, encoded_housing, 
            encoded_saving_accounts, encoded_checking_account, 
            credit_amount, duration
        ]], columns=[
            'Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 
            'Checking account', 'Credit amount', 'Duration'
        ])

        # Make prediction
        prediction_encoded = model.predict(input_df)
        prediction_label = le_target.inverse_transform(prediction_encoded)[0]

        return jsonify({'risk_prediction': prediction_label})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
