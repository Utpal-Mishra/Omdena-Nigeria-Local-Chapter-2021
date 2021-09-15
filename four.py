import streamlit as st

import sys
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px

import pickle
import joblib


def app():
    
    st.title("OMDENA NIGERIA LOCAL CHAPTER 2021")
          
    st.write("")
    st.write("")
     
    # loading the trained model
    #pickle_in = open('classifier.pkl', 'rb') 
    classifier = joblib.load('four') 
    #classifier = pickle.load(pickle_in)
     
    
    # defining the function which will make the prediction using the data which the user inputs 
    def prediction(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11):   
     
            # Making predictions 
        prediction = classifier.predict( 
            [[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11]])
         
        if prediction == 0:
            pred = 'Employee is Not Eligible For Loan'
        else:
            pred = 'Employee is Eligible For Loan'
            
        return pred
      
    
    
    # this is the main function in which we define our webpage  
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Check Employee Loan Status</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
          
    st.write("")
    st.write("")
    
    # following lines create boxes in which user can enter data required to make prediction 
    X1 = st.number_input("What is your Gender? [0: Female; 1: Male] ")
    st.write("")
    X2 = st.number_input("Are you Married? [0: No; 1: Yes]")
    st.write("")
    X3 = st.number_input("How many Dependents you have?")
    st.write("")
    X4 = st.number_input("Are you a Graduate? [0: Graduate; 1: Not Graduate]")
    st.write("")
    X5 = st.number_input("Are you Self-Employed?")
    st.write("")
    X6 = st.number_input("How much is your Income?")
    st.write("")
    X7 = st.number_input("How much is the Income of your Loan Partner?")
    st.write("")
    X8 = st.number_input("How much is the Loan Amount?")
    st.write("")
    X9 = st.number_input("How much is the tenure of Loan? [In Months]")
    st.write("")
    X10 = st.number_input("How much is the tenure of your Credit History?")
    st.write("")
    X11 = st.number_input("In which Area do you live? [0: Urban; 1: Rural]")
              
    st.write("")
    st.write("")
    
    result = ""
          
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11) 
        st.success('Prediction: {}'.format(result))
        print(result)