import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title = "Prediction of Disease Outbreaks ",
                   layout = "wide",
                   page_icon = "Doctor")

# getting the working directory of main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved model
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('saved_models/heart_diseases.sav', 'rb'))

parkinsons_model = pickle.load(open('D:\C DATA AFTER RAM & SSD INSTALLATION\CODE HISTORY\AICTE INTERNSHIP\Disease Prediction\saved_models\parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Diseases Outbreak System',
                           ['Diabetes Prediction', 
                            'Heart Diseases Prediction',
                            'Parkinsons Diseases Prediction'],
                            menu_icon = 'hospital-fill',
                            icons = ['activity', 'heart', 'person'],
                            default_index = 0) 
    
diab_diagnosis = ''

# Diabetes Prediction page 
if selected == 'Diabetes Prediction':

    # page title 
    st.title('Diabetes Prediction using ML')

    # getting the user input
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies ***(0-17)***')
    with col2:
        Glucose = st.text_input('Glucose Level ***(0-200)***')
    with col3:
        Blood_P = st.text_input('Blood Pressure Value ***(0-122)***')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value ***(0-99)***')
    with col2:
        Insulin = st.text_input('Insulin Level ***(0-846)***')
    with col3:
        BMI = st.text_input('BMI Value ***(0-67)***')
    with col1:
        Diabetes_Pedigree_function = st.text_input('Diabetes Pedigree Function Value ***(0.08-2.42)***')
    with col2:
        Age = st.text_input('Age of person ***(21-81)***') 
        
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, Blood_P, SkinThickness, 
            Insulin, BMI, Diabetes_Pedigree_function, Age]
 
        user_input = [float(x) for x in user_input]

        diabetes_prediction = diabetes_model.predict([user_input])

        if diabetes_prediction[0] == 1:
            diab_diagnosis = 'Person is diabetic'
        else:
            diab_diagnosis = 'Person is not diabetic' 

    st.success(diab_diagnosis)        



# HEART DISEASES

heart_diagnosis = ''

if selected == 'Heart Diseases Prediction':

    # Heart Disease Prediction page
    st.title('Heart Disease Prediction using ML')

    # Getting user input
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age ***(29-77)***')
        trestbps = st.text_input('Resting Blood Pressure ***(94-200)***')
        restecg = st.text_input('Resting Electrocardiographic Results ***(0-2)***')
        exang = st.text_input('Exercise Induced Angina ***(0-1)***')
        ca = st.text_input('Number of Major Vessels ***(0-3)***')
    
    with col2:
        sex = st.text_input('Sex ***(1 = male, 0 = female)***')
        chol = st.text_input('Serum Cholesterol (mg/dl) ***(126-564)***')
        thalach = st.text_input('Maximum Heart Rate Achieved ***(71-202)***')
        oldpeak = st.text_input('ST Depression Induced by Exercise ***(0-6.2)***')
        thal = st.text_input('Thalassemia ***(0-3)***')
    
    with col3:
        cp = st.text_input('Chest Pain Type ***(0-3)***')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl ***(1 = True, 0 = False)***')
        slope = st.text_input('Slope of the Peak Exercise ST Segment ***(0-2)***')

    # Prediction button
    if st.button('Heart Disease Test Result'):
        user_input2 = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
        user_input2 = [float(x) for x in user_input2]
        heart_prediction = heart_disease_model.predict([user_input2])
    
        if heart_prediction[0] == 1:
            heart_diagnosis = 'Person is likely to have heart disease'
        else:
            heart_diagnosis = 'Person is unlikely to have heart disease'

    st.success(heart_diagnosis)

# Parkinson's Disease Diagnosis
parkin_diagnosis = ''

# Parkinson's Disease Prediction page
if selected == 'Parkinsons Diseases Prediction':

    # page title 
    st.title('Parkinson\'s Disease Prediction using ML')

    # getting the user input
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('FO ***(88-260)***')
    with col2:
        fhi = st.text_input('FHI ***(102-592)***')
    with col3:
        flo = st.text_input('FLO ***(65-239)***')
    with col1:
        Jitter_percent = st.text_input('Jitter Percent ***(0.001-0.033)***')
    with col2:
        Jitter_Abs = st.text_input('Jitter Abs ***(0.00001-0.00026)***')
    with col3:
        RAP = st.text_input('RAP ***(0.0006-0.021)***')
    with col1:
        PPQ = st.text_input('PPQ ***(0.0005-0.019)***')
    with col2:
        DDP = st.text_input('DDP ***(0.002-0.064)***')
    with col3:
        Shimer = st.text_input('Shimer ***(0.009-0.119)***')
    with col1:
        Shimer_dB = st.text_input('Shimer dB ***(0.085-1.302)***')
    with col2:
        APQ3 = st.text_input('APQ3 ***(0.002-0.066)***')
    with col3:
        APQ5 = st.text_input('APQ5 ***(0.003-0.078)***')
    with col1:
        APQ = st.text_input('APQ ***(0.004-0.134)***')
    with col2:
        DDA = st.text_input('DDA ***(0.007-0.198)***')
    with col3:
        NHR = st.text_input('NHR ***(0.0006-0.314)***')
    with col1:
        HNR = st.text_input('HNR ***(8-33)***')
    with col2:
        RPDE = st.text_input('RPDE ***(0.256-0.684)***')
    with col3:
        DFA = st.text_input('DFA ***(0.574-0.825)***')
    with col1:
        spread1 = st.text_input('Spread1 ***(-7.95 to -2.43)***')
    with col2:
        spread2 = st.text_input('Spread2 ***(0.006-0.450)***')
    with col3:
        D2 = st.text_input('D2 ***(1.4-3.9)***')
    with col1:
        PPE = st.text_input('PPE ***(0.04-0.55)***')

    if st.button('Parkinson\'s Disease Test Result'):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimer, 
                      Shimer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        user_input = [float(x) for x in user_input]

        parkin_prediction = parkinsons_model.predict([user_input])

        if parkin_prediction[0] == 1:
            parkin_diagnosis = 'Person is at risk of Parkinson\'s disease'
        else:
            parkin_diagnosis = 'Person is not at risk of Parkinson\'s disease' 

    st.success(parkin_diagnosis)
    
