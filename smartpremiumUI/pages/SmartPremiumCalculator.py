import numpy as np
import streamlit as st
import pickle

# Load the best trained model as a pickle file
pickleFilePath = r'C:\Users\HP\best_model.pkl'
with open(pickleFilePath, 'rb') as file:
    model = pickle.load(file)
 
def styled_label(text):
    return f'''
        <label style="
            font-size: 20px;
            font-weight: 100;
            color: #007BFF;">
            {text}
        </label>
    '''

# Set the page layout to wide
st.set_page_config(layout="wide")  


# Split the columns in to 1:3 ratio
col1, col2 = st.columns([1, 3])
with col1:    
    st.image("assets\guvi.jpeg", width=250) 
with col2:
    st.markdown(
            """<h2 style="text-align: center; color: #4CAF50;">
                Welcome to Smart Premium Calculator
            </h2>
            """,
            unsafe_allow_html=True
        )
st.write("<h3 style='font-size:20px; color:green;'>Kindly enter your details to predict your insurance premium smartly</h3>", unsafe_allow_html=True)


# Split the page in the ratio 50:50 column wise
col1, col2 = st.columns([50,50]) 


with col1:
    st.markdown(styled_label('Age'), unsafe_allow_html=True)
    age = st.number_input('',min_value=18, max_value=100, value=30)
    
    st.markdown(styled_label('Number of Dependents'), unsafe_allow_html=True)
    dependents = st.number_input('', min_value=0, max_value=10, value=1)

    st.markdown(styled_label('Occupation'), unsafe_allow_html=True)
    occupation = st.selectbox('', ['Self-Employed', 'Employed', 'Unemployed'])

    st.markdown(styled_label('Location'), unsafe_allow_html=True)
    location = st.selectbox('', ['Urban', 'Rural', 'Sub-Urban'])

    st.markdown(styled_label('Credit Score'), unsafe_allow_html=True)
    credit_score = st.number_input('', min_value=200, max_value=850, value=700)

with col2:    
    st.markdown(styled_label('Gender'), unsafe_allow_html=True)
    gender = st.selectbox('', ['Male', 'Female'])

    st.markdown(styled_label('Education Level'), unsafe_allow_html=True)
    education_level = st.selectbox('', ['High School', 'Bachelor', 'Master', 'PhD'])

    st.markdown(styled_label('Health Score (1-100)'), unsafe_allow_html=True)
    health_score = st.slider('', 1, 100, 80)

    st.markdown(styled_label('Policy Type'), unsafe_allow_html=True)
    policyType = st.selectbox('', ['Premium', 'Comprehensive', 'Basic'])

    st.markdown(styled_label('Exercise Frequency'), unsafe_allow_html=True)
    exercise_frequency = st.selectbox('', ['Weekly', 'Monthly', 'Daily', 'Rarely'])

    # Feature processing
    annual_income=None
    marital_status=None
    smoking_status=None 
    exercise_frequency=None 
    propertyType=None
    previousClaims=None
    vehicleAge=None
    insuranceDuration=None

    gender = 1 if gender == 'Male' else 0

    if not annual_income:
        annual_income = 200000
    else:
        annual_income = st.number_input('Annual Income', min_value=1000, value=50000)
    
    if not marital_status:
        marital_status = 1
    else:
        marital_status = {'Single':2, 'Married':1, 'Divorced':0}[marital_status]
    
    education_level = {'High School':1,'Bachelor':0,'Master':2,'PhD':3,}[education_level]
    occupation = {'Self-Employed':1, 'Employed':0, 'Unemployed':2}[occupation]
    location={'Urban':2,'Rural':0,'Sub-Urban':1}[location]
    policyType = {'Premium':2,'Comprehensive':1,'Basic':0}[policyType]

    if not smoking_status:
        smoking_status = 0
    else:
        smoking_status = 1 if smoking_status == 'Yes' else 0

    if not previousClaims:
        previousClaims = 1
    else:
        previousClaims = st.number_input('Previous Claims', min_value=0, value=0)

    if not vehicleAge:
        vehicleAge = 7
    else:
        vehicleAge = st.number_input('Vehicle Age', min_value=0, value=0)

    if not insuranceDuration:
        insuranceDuration = 15
    else:
        insuranceDuration = st.slider('Insurance Duration', min_value=1, max_value=100, value=1)

    if not exercise_frequency:
        exercise_frequency = 1
    else:
        exercise_frequency = {'Weekly':3, 'Monthly':1, 'Daily':0, 'Rarely':2}[exercise_frequency]
    
    if not propertyType:
        propertyType = 2
    else:
        propertyType = {'House':2, 'Apartment':0, 'Condo':1}[propertyType]

with col2:
    # Styling for the Predict button
    st.markdown("""
                    <style>
                        div.stButton > button:first-child {
                            background-color: #4CAF50;
                            color: white;
                            font-size: 16px;
                            font-weight: bold;
                            padding: 0.5em 1.5em;
                            border-radius: 8px;
                            border: none;
                            transition: 0.3s;
                    }
                        div.stButton > button:first-child:hover {
                            background-color: #45a049;
                            color: #fff;
                    }
                    </style>
                """, unsafe_allow_html=True)
    
    # Clicking the Predict button
    if st.button("Predict"):
        features = np.array([[age, gender, annual_income, marital_status, dependents, education_level, 
                  occupation, health_score, location, policyType, previousClaims,vehicleAge, 
                  credit_score, insuranceDuration, smoking_status, exercise_frequency, propertyType]])
        prediction = model.predict(features)
        st.success(f"Predicted Premium Amount: Rs: {prediction[0]:,.2f}")
        st.write("\n\n**Note:** This is merely an accurate estimate. For exact values, please contact your insurance provider.")