Credit Risk Prediction Model

This project aims to develop a robust credit risk prediction model capable of classifying loan applicants as either 'good' or 'bad' risk. The primary goal is to assist financial institutions in making informed lending decisions, thereby minimizing potential losses due to loan defaults.

Dataset
The model was trained and evaluated using the German Credit Data dataset. This dataset contains a comprehensive set of features related to loan applicants, including demographic information, credit history, and financial details, allowing for a thorough analysis of factors influencing credit risk.

Technologies and Libraries
The project leverages a stack of powerful Python-based technologies:

Python: The core programming language for all development.
Pandas: Utilized for efficient data manipulation, cleaning, and preprocessing of the German Credit Data.
Scikit-learn: Employed for building and evaluating various machine learning models, including Decision Trees, Random Forests, and Extra Trees Classifiers, to identify the best-performing algorithm for credit risk prediction.
Flask: Used to develop a lightweight web API, enabling the deployment of the trained machine learning model for real-time predictions.
ngrok: For securely exposing the local Flask API server to the internet, facilitating testing and demonstration of the prediction service.



data/: This directory should contain your dataset, e.g., german_credit_data.csv.
models/: This directory is where trained models will be saved. For this project, the extra_trees_credit_model.pkl should be present here after training or downloaded if provided.
encoders/: This directory will store the LabelEncoder objects for categorical features and the target variable. Specifically, Sex.encoder.pkl, Housing.encoder.pkl, Saving accounts.encoder.pkl, Checking account.encoder.pkl, and target_.encoder.pkl should be available.
