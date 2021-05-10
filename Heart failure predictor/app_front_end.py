import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in=open("lr_clf.pkl","rb")
lr_clf=pickle.load(pickle_in)

pickle_in=open("sv_clf.pkl","rb")
sv_clf=pickle.load(pickle_in)

pickle_in=open("kn_clf.pkl","rb")
kn_clf=pickle.load(pickle_in)

pickle_in=open("dt_clf.pkl","rb")
dt_clf=pickle.load(pickle_in)

pickle_in=open("rf_clf.pkl","rb")
rf_clf=pickle.load(pickle_in)

pickle_in=open("gb_clf.pkl","rb")
gb_clf=pickle.load(pickle_in)

def welcome():
    return "Welcome All!"

def lr_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim):
    prediction=lr_clf.predict(([[int(age),int(anm),int(c_p),int(dbt),int(ejf),int(hbp),int(plt),int(s_c),int(s_s),int(sex),int(smk),int(tim)]]))
    print(prediction)
    return prediction

def sv_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim):
    prediction=sv_clf.predict(([[int(age),int(anm),int(c_p),int(dbt),int(ejf),int(hbp),int(plt),int(s_c),int(s_s),int(sex),int(smk),int(tim)]]))
    print(prediction)
    return prediction

def kn_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim):
    prediction=kn_clf.predict(([[int(age),int(anm),int(c_p),int(dbt),int(ejf),int(hbp),int(plt),int(s_c),int(s_s),int(sex),int(smk),int(tim)]]))
    print(prediction)
    return prediction

def dt_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim):
    prediction=dt_clf.predict(([[int(age),int(anm),int(c_p),int(dbt),int(ejf),int(hbp),int(plt),int(s_c),int(s_s),int(sex),int(smk),int(tim)]]))
    print(prediction)
    return prediction

def rf_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim):
    prediction=rf_clf.predict(([[int(age),int(anm),int(c_p),int(dbt),int(ejf),int(hbp),int(plt),int(s_c),int(s_s),int(sex),int(smk),int(tim)]]))
    print(prediction)
    return prediction

def gb_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim):
    prediction=gb_clf.predict(([[int(age),int(anm),int(c_p),int(dbt),int(ejf),int(hbp),int(plt),int(s_c),int(s_s),int(sex),int(smk),int(tim)]]))
    print(prediction)
    return prediction

def main():
    st.title("Heart Failure Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Failure Predictor ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.text_input("Age","Type Here")
    anm=st.text_input("Do you have anaemia?","Type 1 if yes and 0 if no")
    c_p=st.text_input("Creatinine-phosphokinase","Enter your creatinine-phosphokinase level")
    dbt=st.text_input("Are you diabetic?","Type 1 if yes and 0 if no")
    ejf=st.text_input("Ejection Fraction","Enter your ejection fraction level")
    hbp=st.text_input("Do you have high blood pressure?","Type 1 if yes and 0 if no")
    plt=st.text_input("Platelets count","Type Here")
    s_c=st.text_input("Serum creatinine level","Type Here")
    s_s=st.text_input("Serum sodium level","Type Here")
    sex=st.text_input("Sex","Type 1 for male and 0 for female")
    smk=st.text_input("Do you smoke?","Type 1 if yes and 0 if no")
    tim=st.text_input("Time","Type Here")
    
    lr_res=""
    if st.button("LR_Predict"):
        lr_res=lr_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim)
        if lr_res==1:
            st.success("Heart Failure likely to occur")
        if lr_res==0:
            st.success("Heart Failure unlikely to occur")
            
    sv_res=""
    if st.button("SV_Predict"):
        sv_res=sv_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim)
        if sv_res==1:
            st.success("Heart Failure likely to occur")
        if sv_res==0:
            st.success("Heart Failure unlikely to occur")
            
    kn_res=""
    if st.button("KN_Predict"):
        kn_res=kn_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim)
        if kn_res==1:
            st.success("Heart Failure likely to occur")
        if kn_res==0:
            st.success("Heart Failure unlikely to occur")
            
    dt_res=""
    if st.button("DT_Predict"):
        dt_res=dt_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim)
        if dt_res==1:
            st.success("Heart Failure likely to occur")
        if dt_res==0:
            st.success("Heart Failure unlikely to occur")
            
    rf_res=""
    if st.button("RF_Predict"):
        rf_res=rf_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim)
        if rf_res==1:
            st.success("Heart Failure likely to occur")
        if rf_res==0:
            st.success("Heart Failure unlikely to occur")
            
    gb_res=""
    if st.button("GB_Predict"):
        gb_res=gb_predict_heart_failure(age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim)
        if gb_res==1:
            st.success("Heart Failure likely to occur")
        if gb_res==0:
            st.success("Heart Failure unlikely to occur")
            
if __name__=='__main__':
    main()