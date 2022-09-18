import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from tensorflow import keras


# loading the saved models
diabetes_model = pickle.load(open('Models\diabetes_model_1.sav','rb'))
heart_disease_model = pickle.load(open('Models\heart_disease1.sav','rb'))
liver_model = pickle.load(open('Models\liver.pkl','rb'))
kidney_model = pickle.load(open('Models\kidney.pkl','rb'))


# sidebar for navigation
with st.sidebar :
    selected = option_menu('Strategic Masters',['Diabetes Prediction','Heart Disease Prediction','Liver Disease Prediction','Kidney Disease Prediction']
            ,icons =['activity','heart','person','person']
                           ,default_index = 0)
    

# diabetes prediction page
if(selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Predictor')
    
    # getting the input data from the user
    # creating columns for better visualisation 
    col1, col2, col3 = st.columns(3)
   
    with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       
    with col2:
       Glucose = st.text_input('Glucose Level')
   
    with col3:
       BloodPressure = st.text_input('Blood Pressure value')
   
    with col1:
       SkinThickness = st.text_input('Skin Thickness value')
   
    with col2:
       Insulin = st.text_input('Insulin Level')
   
    with col3:
       BMI = st.text_input('BMI value')
   
    with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   
    with col2:
       Age = st.text_input('Age of the Person')
   
   
    # code for Prediction
    diab_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Diabetes Test Result'):
       diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
       if (diab_prediction[0] == 1):
         diab_diagnosis = 'The person is diabetic'
       
       else:
         diab_diagnosis = 'The person is not diabetic'
       
    st.success(diab_diagnosis)
    

# Heart Disease prediction page
if(selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Predictor')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex (0: Male; 1: Female)')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
      
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


# Liver Disease prediction page
if(selected == 'Liver Disease Prediction'):
    # page title
    st.title('Liver Disease Predictor')
    
    # getting the input data from the user
    # creating columns for better visualisation 
    col1, col2, col3 = st.columns(3)
   
    with col1:
       Age = st.text_input('Age (in years)')
       
    with col2:
       Gender = st.text_input('Gender (0: Male; 1: Female)')
   
    with col3:
       Total_Bilirubin = st.text_input('Total Bilirubin (in mg/dL)')
   
    with col1:
       Direct_Bilirubin = st.text_input('Conjugated Bilirubin (in mg/dL)')
   
    with col2:
       Alkaline_Phosphotase = st.text_input('Alkaline Phosphatase (in IU/L)')
   
    with col3:
       Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase (in IU/L)')
   
    with col1:
       Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase (in IU/L)')
   
    with col2:
       Total_Protiens = st.text_input('Total Proteins (in g/dL)')

    with col3:
       Albumin = st.text_input('Albumin (in g/dL)')

    with col1:
       Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')
   
   
    # code for Prediction
    liver_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Liver Diagnosis Test Result'):
       liver_prediction = liver_model.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
       
       if (liver_prediction[0] == 1):
         liver_diagnosis = 'The person is having liver disease'
       
       else:
         liver_diagnosis = 'The person is not having liver disease'
       
    st.success(liver_diagnosis)


# Kidney Disease prediction page
if(selected == 'Kidney Disease Prediction'):
    # page title
    st.title('Kidney Disease Predictor')
    
    # getting the input data from the user
    # creating columns for better visualisation 
    col1, col2, col3 = st.columns(3)
   
    with col1:
       age = st.text_input('Age (in years)')
       
    with col2:
       blood_pressure = st.text_input('Blood Pressure (in mm/Hg)')
   
    with col3:
       specific_gravity = st.text_input('Specific Gravity')
   
    with col1:
       albumin = st.text_input('Albumin (0, 1, 2, 3, 4, 5)')
   
    with col2:
       sugar = st.text_input('Sugar (0, 1, 2, 3, 4, 5)')
   
    with col3:
       red_blood_cells = st.text_input('Red Blood Cells (0: Abnormal; 1: Normal)')
   
    with col1:
       pus_cell = st.text_input('Pus Cell (0: Abnormal; 1: Normal)')
   
    with col2:
       pus_cell_clumps = st.text_input('Pus Cell Clumps (0: Not Present; 1: Present)')

    with col3:
       bacteria = st.text_input('Bacteria (0: Not Present; 1: Present)')

    with col1:
       blood_glucose_random = st.text_input('Blood Glucose Random (in mgs/dl)')

    with col2:
       blood_urea = st.text_input('Blood Urea (in mgs/dl)')

    with col3:
       serum_creatinine = st.text_input('Serum Creatinine (in mgs/dl)')

    with col1:
       sodium = st.text_input('Sodium (in mEq/L)')

    with col2:
       potassium = st.text_input('Potassium (in mEq/L)')

    with col3:
       haemoglobin = st.text_input('Haemoglobin (in gms)')

    with col1:
       packed_cell_volume = st.text_input('Packed Cell Volume')

    with col2:
       white_blood_cell_count = st.text_input('White Blood Cell Count (in cells/cumm)')

    with col3:
       red_blood_cell_count = st.text_input('Red Blood Cell Count (in millions/cmm)')

    with col1:
       hypertension = st.text_input('Hypertension (0: No; 1: Yes)')

    with col2:
       diabetes_mellitus = st.text_input('Diabetes Mellitus (0: No; 1: Yes)')

    with col3:
       coronary_artery_disease = st.text_input('Coronary Artery Disease (0: No; 1: Yes')

    with col1:
       appetite = st.text_input('Appetite (0: Good; 1: Poor)')

    with col2:
       peda_edema = st.text_input('Pedal Edema (0: No; 1: Yes)')

    with col3:
       aanemia = st.text_input('Anemia (0: No; 1: Yes)')
   
   
    # code for Prediction
    kidney_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Kidney Diagnosis Test Result'):
       kidney_prediction = kidney_model.predict([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]])
       
       if (kidney_prediction[0] == 1):
         kidney_diagnosis = 'The person is having kidney disease'
       
       else:
         kidney_diagnosis = 'The person is not having kidney disease'
       
    st.success(kidney_diagnosis)

