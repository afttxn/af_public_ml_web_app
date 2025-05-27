# -*- coding: utf-8 -*-
"""
Created on Sun May 25 20:30:01 2025

@author: Aftab
"""

import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu

# Loading the saved model 

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_model = pickle.load(open('heart_disease_model.sav','rb'))

breast_model = pickle.load(open('breast_model.sav','rb'))

# Sidebar for navigate 

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],
                           icons = ['activity','heart','person'],
                           default_index = 0 )


# Diabetes Prediction Page 

if(selected == 'Diabetes Prediction'):
    
    # Page title
    st.title("Diabetes Prediction usinh ML ")
    
    col1, col2 , col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Level')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedegree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
        diab_diagnosis = ''
        
        if st.button('Diabetes Test Result'):
            input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            input_data = [float(i) for i in input_data]
            diab_prediction = diabetes_model.predict([input_data])
            
            if(diab_prediction[0] ==1):
                diab_diagnosis = 'The person is non-diabetic'
            else:
                diab_diagnosis = 'The person is diabetic'
                
            st.success(diab_diagnosis)

               
                
                
     


if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the person')

    with col2:
        sex = st.text_input('Gender of the person')
    
    with col3:
        cp  = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
            
    with col2:
        chol = st.text_input('Serum Chlorestol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting electrocardiographic result')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input("Excercised Induced Angina")
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major Vessels colored by fluroscopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal;1 = fixed defect; 2 = reversable defect')
        
        heart_diagnosis = ''
        
        # Creating a button for prediction 
        
        if st.button('Heart Disease Test Result'):
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            input_data = [float(i) for i in input_data]
            heart_prediction = heart_model.predict([input_data])
            
            if(heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having a heart disease'
            else:
                heart_diagnosis = 'The person is not having heart disease'
                
            st.success(heart_diagnosis)  # ✅ Now it runs no matter the result

    


if (selected == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
    with col2:
        texture_mean = st.text_input('Texture Mean') 
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean') 
    with col1:
        area_mean = st.text_input('Area Mean')
    with col2: 
        smoothness_mean = st.text_input('Smoothness Mean') 
    with col3: 
        compactness_mean = st.text_input('Compactness Mean') 
    with col1: 
        concavity_mean = st.text_input('Concavity Mean') 
    with col2: 
        concave_points_mean = st.text_input('Concave Points Mean') 
    with col3: 
        symmetry_mean = st.text_input('Symmetry Mean') 
    with col1: 
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean') 
    with col2: 
        radius_se = st.text_input('Radius SE') 
    with col3: 
        texture_se = st.text_input('Texture SE')
    with col1:
        perimeter_se = st.text_input('Perimeter SE')
    with col2:
        area_se = st.text_input('Area SE')
    with col3:
        smoothness_se = st.text_input('Smoothness SE')
    with col1:
        compactness_se = st.text_input('Compactness SE')
    with col2:
        concavity_se = st.text_input('Concavity SE')
    with col3:
        concave_points_se = st.text_input('Concave Points SE')
    with col1:
        symmetry_se = st.text_input('Symmetry SE')
    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')
    with col3:
        radius_worst = st.text_input('Radius Worst')
    with col1:
        texture_worst = st.text_input('Texture Worst')
    with col2:
        perimeter_worst = st.text_input('Perimeter Worst')
    with col3:
        area_worst = st.text_input('Area Worst')
    with col1:
        smoothness_worst = st.text_input('Smoothness Worst')
    with col2:
        compactness_worst = st.text_input('Compactness Worst')
    with col3:
        concavity_worst = st.text_input('Concavity Worst')
    with col1:
        concave_points_worst = st.text_input('Concave Points Worst')
    with col2:
        symmetry_worst = st.text_input('Symmetry Worst')
    with col3:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')
    
    breast_diagnosi = ''
    
    # Creating a button for prediction 
    
    if st.button('Breast Disease Result'):
        input_data = [radius_mean,texture_mean,perimeter_mean,
                                                   area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,
                                                   symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,
                                                   area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,
                                                   symmetry_se,fractal_dimension_se,radius_worst,texture_worst,
                                                   perimeter_worst,area_worst,smoothness_worst,compactness_worst,
                                                   concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]
        input_data = [float(i) for i in input_data]
        breast_prediction =  breast_model.predict([input_data])
        
        
         
        if(breast_prediction[0] == 1):
            breast_diagnosi = 'The person has breast cancer'
        else:
            breast_diagnosi = 'The person doesnt have breast cancer'
            
        st.success(breast_diagnosi)
