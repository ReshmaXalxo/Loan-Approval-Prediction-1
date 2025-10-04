📘 Loan Approval Prediction using Machine Learning
🧩 Overview

This project focuses on building a Machine Learning model to predict whether a loan application will be approved or rejected based on applicant details such as income, loan amount, employment status, credit score, and other key attributes.
It automates the decision-making process and helps financial institutions improve efficiency and accuracy in loan evaluation.

🧠 Objective

Predict loan approval status using machine learning algorithms.

Analyze key factors influencing loan decisions.


📊 Dataset

Dataset Name: Loan Approval Dataset
Features include:

no_of_dependents – Number of dependents

education – Graduate / Not Graduate

self_employed – Employment type

income_annum – Annual income

loan_amount – Requested loan amount

loan_term – Duration of the loan

cibil_score – Applicant’s credit score

assets – Total value of owned assets

loan_status – Target variable (Approved/Rejected)

🧹 Data Preprocessing

Handled missing and infinite values.

Encoded categorical variables.

Checked and removed zero variance features.

Normalized large numeric features using StandardScaler.

Split dataset into training (80%) and testing (20%) sets.

🧮 Machine Learning Models

The following models were implemented and compared:

Random Forest Classifier (best performing model)

The Random Forest model achieved the highest accuracy and stability due to its ability to handle feature correlations and reduce overfitting.
📈 Model Evaluation

Metrics used for evaluation:



Accuracy: 0.9824
Precision: 0.9813
Recall: 0.9906
F1 Score: 0.9859
ROC-AUC: 0.9799
