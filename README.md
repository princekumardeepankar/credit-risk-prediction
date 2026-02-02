## Project Description: Credit Risk Prediction Model

This project aims to develop a robust credit risk prediction model capable of classifying loan applicants as either 'good' or 'bad' risk. The primary goal is to assist financial institutions in making informed lending decisions, thereby minimizing potential losses due to loan defaults.

### Dataset

The model was trained and evaluated using the German Credit Data dataset. This dataset contains a comprehensive set of features related to loan applicants, including demographic information, credit history, and financial details, allowing for a thorough analysis of factors influencing credit risk.

### Technologies and Libraries

The project leverages a stack of powerful Python-based technologies:

*   **Python**: The core programming language for all development.
*   **Pandas**: Utilized for efficient data manipulation, cleaning, and preprocessing of the German Credit Data.
*   **Scikit-learn**: Employed for building and evaluating various machine learning models, including Decision Trees, Random Forests, and Extra Trees Classifiers, to identify the best-performing algorithm for credit risk prediction.
*   **Flask**: Used to develop a lightweight web API, enabling the deployment of the trained machine learning model for real-time predictions.
*   **ngrok**: For securely exposing the local Flask API server to the internet, facilitating testing and demonstration of the prediction service.


## Repository Structure

```
credit_risk_predictor/
├── data/
│   └── german_credit_data.csv        # Raw dataset for model training
├── models/
│   └── extra_trees_credit_model.pkl  # Trained Extra Trees Classifier model
├── encoders/
│   ├── Sex.encoder.pkl               # Label encoder for 'Sex' feature
│   ├── Housing.encoder.pkl           # Label encoder for 'Housing' feature
│   ├── Saving accounts.encoder.pkl   # Label encoder for 'Saving accounts' feature
│   ├── Checking account.encoder.pkl  # Label encoder for 'Checking account' feature
│   └── target_.encoder.pkl           # Label encoder for the 'Risk' target variable
├── app.py                          # Flask application for inference
├── requirements.txt                # Python dependencies for the project
└── README.md                       # Project documentation and setup instructions
```

### Explanation of Directories and Files:

*   **`credit_risk_predictor/`**: The root directory of the project.
*   **`data/`**: This directory contains the raw dataset used for training the machine learning model. `german_credit_data.csv` is the primary dataset.
*   **`models/`**: This directory stores the trained machine learning model. `extra_trees_credit_model.pkl` is the serialized Extra Trees Classifier model.
*   **`encoders/`**: This directory holds the serialized `LabelEncoder` objects used for transforming categorical features and the target variable. Each `.pkl` file corresponds to an encoder for a specific column.
*   **`app.py`**: This is the main application file. It contains the Flask code to load the trained model and encoders, and expose an interface for making predictions.
*   **`requirements.txt`**: This file lists all the Python libraries and their versions required to run the project. It ensures reproducibility of the development environment.
*   **`README.md`**: This Markdown file provides an overview of the project, setup instructions, how to run the application, and any other relevant documentation.


## Setup Instructions

To get this project up and running on your local machine, please follow the steps below:

### 1. Clone the Repository
First, you need to clone the project repository from GitHub. Make sure you have Git installed on your system. Open your terminal or command prompt and run the following command:

```bash
git clone <repository_url>
cd <repository_name>
```
Replace `<repository_url>` with the actual URL of the GitHub repository and `<repository_name>` with the name of the cloned directory.

### 2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects. You can use either `venv` (standard Python module) or `conda`).

#### Using `venv`:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

#### Using `conda`:
```bash
conda create -n credit_risk_env python=3.9  # Or your preferred Python version
conda activate credit_risk_env
```

### 3. Install Required Python Packages
With your virtual environment activated, install all the necessary Python libraries using the `requirements.txt` file provided in the repository:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Environment and Data
Ensure that your project structure includes the following directories and necessary files:

*   **`data/`**: This directory should contain your dataset, e.g., `german_credit_data.csv`.
*   **`models/`**: This directory is where trained models will be saved. For this project, the `extra_trees_credit_model.pkl` should be present here after training or downloaded if provided.
*   **`encoders/`**: This directory will store the `LabelEncoder` objects for categorical features and the target variable. Specifically, `Sex.encoder.pkl`, `Housing.encoder.pkl`, `Saving accounts.encoder.pkl`, `Checking account.encoder.pkl`, and `target_.encoder.pkl` should be available.


## Usage Guide: Credit Risk Prediction API

This section explains how to run the Flask API locally, expose it using ngrok, and make predictions.

### 1. Run the Flask Application
Navigate to the project root directory where `app.py` is located and run the Flask application:

```bash
python app.py
```
This will start the Flask server, typically on `http://127.0.0.1:5000`.

### 2. Expose the API with ngrok
To make your local Flask API accessible over the internet, you can use `ngrok`. If you don't have ngrok, download it from [ngrok.com](https://ngrok.com/download) and set it up.

Once ngrok is installed and configured (e.g., authenticated with your auth token), run the following command in a new terminal window:

```bash
ngrok http 5000
```
ngrok will provide a public URL (e.g., `https://<random_subdomain>.ngrok-free.app`). Keep this URL handy, as you'll use it to send prediction requests.


### 4. Interpret the API Response

The API will respond with a JSON object containing the `risk_prediction` field. The value of this field will be either `'Good Risk'` or `'Bad Risk'`, indicating the model's assessment of the applicant's creditworthiness.

**Example Response for 'Bad Risk':**

```json
{
    "risk_prediction": "Bad Risk"
}
```

**Example Response for 'Good Risk':**

```json
{
    "risk_prediction": "Good Risk"
}
```


## Model Details

The chosen model for credit risk prediction is the **Extra Trees Classifier**. This ensemble learning method, similar to Random Forests, builds multiple decision trees and merges their predictions to improve accuracy and control overfitting. Extra Trees are particularly effective due to their high randomization in feature and split point selection, leading to reduced variance.

### Performance:
*   **Extra Trees Accuracy**: 0.6476
*   **Best Parameters (from GridSearchCV)**: `{'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}`


## Results and Performance Comparison

During the model training phase, several classification algorithms were evaluated using GridSearchCV. The Extra Trees Classifier was selected for deployment due to its good balance of performance and interpretability, though XGBoost showed slightly higher test accuracy.

The performance of the evaluated models on the test set (accuracy) is as follows:

*   **Extra Trees Classifier (Deployed Model)**: 0.6476
*   **XGBoost Classifier**: 0.6667
*   **Random Forest Classifier**: 0.6190
*   **Decision Tree Classifier**: 0.5810




