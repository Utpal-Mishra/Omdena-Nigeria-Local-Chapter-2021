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
    classifier = joblib.load('three') 
    #classifier = pickle.load(pickle_in)
     
    
    # defining the function which will make the prediction using the data which the user inputs 
    def prediction(X1, X2, X3, X4, X5):   
     
            # Making predictions 
        prediction = classifier.predict( 
            [[X1, X2, X3, X4, X5]])
         
        if prediction == 0:
            pred = 'Crisis Period'
        else:
            pred = 'No Crisis Period'
            
        return pred
          
      
    
    
    # this is the main function in which we define our webpage  
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Check Student Loan Status</h1> 
    </div> 
    """
          
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
          
    st.write("")
    st.write("")
    
    # following lines create boxes in which user can enter data required to make prediction 
    X1 = st.number_input("Principal Amount")
    st.write("")
    X2 = st.number_input("Terms/ Duration") 
    st.write("")
    X3 = st.number_input("Past Due Days")
    st.write("")
    X4 = st.number_input("Age")
    st.write("")
    X5 = st.number_input("Education [0: High School or Above; 1: Bachelors; 2: College; 3: Master's or Above]")
    
    st.write("")
    st.write("")
    
    
    result = ""
          
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(X1, X2, X3, X4, X5) 
        st.success('Prediction: {}'.format(result))
        print(result)