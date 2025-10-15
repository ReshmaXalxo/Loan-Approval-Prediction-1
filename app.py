import streamlit as st
import pandas as pd
import pickle as pk

import pickle as pk

model = pk.load(open("model.pkl", "rb"))
scaler = pk.load(open("scaler.pkl", "rb"))


st.header('Loan Prediction App')


No_of_dep=st.slider('choose Number  of Dependents',0,10)
Grad=st.selectbox('Choose Education',['Graduated','Not Graduated'])
Self_emp=st.selectbox('Self Employed',['yes','no'])
Annual_income=st.slider('choose Annnual Income',0,10000000)
Loan_Amount=st.slider('Choose Loan Amount',0,10000000)
Loan_duration=st.slider('choose Loan Duration',0,30)
Credit=st.slider('Choose cibil Score',0,1000)
Assets=st.slider('choose Assets',0,10000000)

if Grad=='Graduaated':
    Grad_s=0
else:
    Grad_s=1
if Self_emp=='No':
    emp_s=0
else:
    emp_s=1
if st.button("Predict"):
    pred_data=pd.DataFrame([[No_of_dep, Grad_s, emp_s,	Annual_income,	Loan_Amount,	Loan_duration,Credit, Assets]],columns=['no_of_dependents',	'education', 'self_employed', 'income_annum',	'loan_amount',	'loan_term',	'cibil_score',	'assets'])
    pred_data=scaler.transform(pred_data)
    predict=model.predict(pred_data)
    if predict==1:
        st.markdown('Loan is approved')
    else:

        st.markdown('Loan is Rejected')
