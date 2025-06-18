# ML Student Depression
💡 Project Title: Student Depression Prediction Using Machine Learning

📌 Objective:
To build a web application that predicts whether a student is likely experiencing depression based on various personal, academic, and lifestyle factors.

⚙️ How It Works:
1. User Interface (Front End) – Streamlit:
The application is built using Streamlit, a Python library for creating web apps. It provides a clean, interactive UI where the user inputs several details:

Demographic Details: Gender, Age

Academic Factors: CGPA, Academic Pressure, Study Hours, Study Satisfaction

Lifestyle & Health:

Sleep Duration (e.g., “7-8 hours”, “Less than 5 hours”)

Diet Quality (Healthy, Moderate, Unhealthy)

Family History of Mental Illness (Yes/No)

Suicidal Thoughts (Yes/No)

Financial Stress

2. Preprocessing and Transformation:
Once the user enters the data:

Categorical values (like gender, sleep duration, diet, education field, suicidal thoughts, family history) are encoded using pre-trained encoders Label Encoder and Onehot Encoder saved in a .pkl file (St_depression_main.pkl).

The data is scaled using a pre-fitted Minmax Scaler to normalize input features.

3. Prediction (Back End – ML Model):
The app loads a pre-trained machine learning model from the .pkl file.

Input data is reshaped and passed into the model for prediction.

The model outputs:

1 → No Depression

0 → Depression Detected

4. Output Display:
Based on the model’s output:

A green success message (“No depression”) is shown if depression is not detected.

A yellow warning (“Depression”) appears if the model predicts depression.

🧠 Machine Learning Techniques Used:
Evaluated the performance using different classification algorithms:

KNeighbourClassifier
SVC
GaussianNB
RandomForestClassifier
GradientBoostingClassifier
DecisionTreeClassifier
XGBClassifier

Best model is identified as XGBClassifier.

 📌 Hyperparameter Tuning
 Done on XGBClassifier model and get an average score around 87%.
 
These models are trained on labeled datasets with depression status as the target variable.

🌐 Deployment & Usability:
Web-based and Interactive: No need for technical background to use.

Real-time Prediction: As soon as the user fills in details and clicks "PREDICT", a prediction is made instantly.

Background Image: Aesthetic design using a soft background image to make the interface user-friendly.
