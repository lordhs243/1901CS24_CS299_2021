import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All!"

def predict_loan_approval(dpdt,grad,slf,incm,cinc,lamt,ltrm,hist,pwrt,p_ar):
    prediction=classifier.predict(([[int(dpdt),int(grad),int(slf),int(incm),int(cinc),int(lamt),int(ltrm),int(hist),int(pwrt),int(p_ar)]]))
    print(prediction)
    return prediction

def main():
    st.title("Loan Approval Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Loan Approval Predictor ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    dpdt=st.text_input("Number of Dependents","Type Here")
    grad=st.text_input("Are you a Graduate?","Type 1 if graduate and 0 otherwise")
    slf=st.text_input("Are you Self-employed?","Type 1 if self-employed and 0 otherwise")
    incm=st.text_input("Monthly Income of Beneficiary","Type Here")
    cinc=st.text_input("Monthly Income of Co-beneficiary","Type Here")
    lamt=st.text_input("Loan Amount Requested","Type Here")
    ltrm=st.text_input("Loan Term Opted","60/120/180 or 240 months terms available")
    hist=st.text_input("Credit History","Type 1 if you took previous loan and repaid it, and 0 otherwise")
    pwrt=st.text_input("Net Property Worth","Type Here")
    p_ar=st.text_input("Property Area","Type 2 for Urban,1 for Semi-urban and 0 for Rural")
    result=""
    if st.button("Predict"):
        result=predict_loan_approval(dpdt,grad,slf,incm,cinc,lamt,ltrm,hist,pwrt,p_ar)
        if result==1:
            st.success("Approval")
        if result==0:
            st.success("Dismissal")
            
if __name__=='__main__':
    main()