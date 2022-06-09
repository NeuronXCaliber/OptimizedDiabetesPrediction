import numpy as np
import pickle
import streamlit as st


load_model=pickle.load(open('C:/OptimizedDiabetesPrediction/trained_model (1).sav','rb'))

# creating a function for prediction

def diabetes_prediction(input):
    
    input_as_numpy=np.asarray(input)
    input_reshape=input_as_numpy.reshape(1,-1)
    prediction=load_model.predict(input_reshape)
    print(prediction)
    if (prediction[0] == 0):
      return" Patient has no diabetes"
    else:
      return" Patient has diabetes"
      
# create main function 
def main():
    st.set_page_config(
        page_title="diabetes prediction",
        layout="centered")
    st.title("An optimized Diabetes Prediction System")
    st.sidebar.subheader("Enter patient's details")
    name1=st.sidebar.text_input("Enter your first Name")
    name2=st.sidebar.text_input("Enter your last name")
    email=st.sidebar.text_input("Enter your Email Id")
    ph_no=st.sidebar.text_input("Enter your Phone Number")
    selectbox=st.sidebar.selectbox("Select gender ", 
                           ["Male","Female","Other"])
   
    
    st.write(f"First name : {name1}")
    st.write(f"Last name : {name2}")
    st.write(f"Phone number : {ph_no}")
    st.write(f"Email Id : {email}")
    st.write(f"Gender : {selectbox}")
    st.subheader("Fill up the required fields :")
    
    
    
    Pregnancies = st.text_input("Enter no. of Pregnancies")
    Glucose = st.text_input("Number of Glucose level")
    BloodPressure = st.text_input('BP level')
    SkinThickness = st.text_input(" Skin thickness")
    Insulin = st.text_input('Insulin')
    BMI = st.text_input(" BMI ")
    DiabetesPedigreeFunction = st.text_input("Diabets pedigree function rate")
    Age = st.text_input("Age")
    
    # code for prediction
    
    diagnosis = ''
    
    if st.button("Result"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness,
                                         Insulin, BMI,
                                         DiabetesPedigreeFunction,Age ])
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    