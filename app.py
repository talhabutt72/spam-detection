import joblib
import streamlit as st


model = joblib.load("model.pkl")
vec = joblib.load("vec.pkl")



st.header("Spam Dectetor!!")

message = st.text_area("Enter your text for checking, whether is it spam or not? ")


if st.button("Predict"):


    lower = message.lower()
    vectorize_form =  vec.transform([lower])
    preiction = model.predict(vectorize_form)

    st.subheader(preiction)
