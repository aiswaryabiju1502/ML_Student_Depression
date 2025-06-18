import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
with open("St_depression_main.pkl","rb") as obj1:
    dict1=pickle.load(obj1)

st.markdown(
    '''
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRF5h9vTVMim98YEs6yPMcQ8aNhhBsVbt2bA&s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''',
    unsafe_allow_html=True)

st.markdown(
    "<h1 style='color: #65081F;'>Student Depression Prediction</h1>",
    unsafe_allow_html=True
)

gender=st.selectbox("Gender",['Male','Female'])
gender=dict1['gender_encode'].transform([gender])[0]
age=st.number_input("Age",15,60)
academic_pr=st.number_input("Academic Pressure",value=0.00,step=0.01,format="%.2f")
cgpa=st.number_input("CGPA",value=0.00,step=0.01,format="%.2f")
study_sat=st.number_input("Study Satisfaction",value=0.00,step=0.01,format="%.2f")
sleep_dur=st.selectbox("Sleep Duration",['Less than 5 hours','7-8 hours','5-6 hours','More than 8 hours','Others'])
sleep_dur=dict1['sleep'].transform([[sleep_dur]])
sleep_dur=sleep_dur.flatten()
diet=st.selectbox("Dietry Habit",['Unhealthy','Moderate','Healthy','Others'])
diet=dict1['diet'].transform([[diet]])
diet=diet.flatten()
category=st.selectbox("Field Of Education",['Science & Technology','Higher Secondary','Law & Education','Commerce & Management','Medical & Health Sciences','Hospitality & Architecture','Arts & Humanities','Other'])
category=dict1['category'].transform([[category]])
category=category.flatten()
suicide=st.selectbox('Have You Ever Had Suicidal Thoughts?',['Yes','No'])
suicide=dict1['suicide_encode'].transform([suicide])[0]
study=st.number_input("Study Hours",0,15)
financial_stress=st.number_input("Financial Stress",value=0.00,step=0.01,format="%.2f")
family=st.selectbox("Family History Of Mental Illnes",['Yes','No'])
family=dict1['family_encode'].transform([family])[0]

button=st.button('PREDICT')
if button:
    data=[[gender,age,academic_pr,cgpa,study_sat,suicide,study,financial_stress,family,*sleep_dur,*diet,*category]]
    scaled=dict1['scaler'].transform(data)
    res=dict1['model'].predict(scaled)[0]
    if res==1:
        st.success("No depression")
        
    elif res==0:
        st.warning("Depression")
        