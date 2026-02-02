import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("extra_trees_creadit_model.pkl")
encoders = {col: joblib.load(f"{col}_encoder.pkl") for col in ["Sex","Housing","Saving accounts","Checking account",]}

st.title("Credit Risk Prediction App")
st.write("Enter application information to predict if the creadit risk is good or bad")

age = st.number_input("Age",min_value =18, max_value =80, value = 30)

sex = st.selectbox("Sex",["male","female"])
job = st.number_input("Job(0-3)",min_value= 0, max_value =3, value =1)

housing = st.selectbox("Housing",["own","rent","free"])
Saving_accounts = st.selectbox("Saving Accounts",["little","moderate","rich","quite rich"])

Checking_account = st.selectbox("Checking Accounts",["little","moderate","rich"])

Credit_amount = st.number_input("Cradit Amount",min_value =0, value =1000)
duration = st.number_input("Duration(months)",min_value = 1,value =12)

input_df = pd.Dataframe({
    "Age":[age],
    "Sex":[encoders["sex"].transform([sex])[0]],
    "Housing":[encoders["Housing"].transform([housing])[0]],
    "Seving account":[encoders["Seving account"].transform([Saving_accounts])[0]],
    "Checking account":[encoders["Checking account"].transform([Checking_account])[0]],
    "Credit amount":[Credit_amount],
    "Duration":[duration]
})

if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]
    if pred ==1:
        st.success("The predicted credit risk is: **GOOD**")
    else:
        st.error("The predicted risk is: **BAD**")