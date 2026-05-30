import joblib
import streamlit as st


model = joblib.load(r"C:\Users\hp\Desktop\14 Days 14 Models\Day 4\model.pkl")


st.header("Spam Dectetor!!")

message = st.text_area("Enter your text for checking, whether is it spam or not? ")


if st.button("Predict"):


    lower = message.lower()
    # vectorize_form =  
    model.predict(message)
