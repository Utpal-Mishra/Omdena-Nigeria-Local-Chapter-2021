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
    classifier = joblib.load('one') 
    #classifier = pickle.load(pickle_in)
     
    
    # defining the function which will make the prediction using the data which the user inputs 
    def prediction(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10):   
     
            # Making predictions 
        prediction = classifier.predict( 
            [[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]])
         
        if prediction == 0:
            pred = 'Crisis Period'
        else:
            pred = 'No Crisis Period'
            
        return pred
          
      
    
    # this is the main function in which we define our webpage         
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Check Economic Crisis Status</h1> 
    </div> 
    """
          
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
          
    st.write("")    
    st.write("")
    
    # following lines create boxes in which user can enter data required to make prediction 
    X1 = st.number_input("Year")
    st.write("")
    X2 = st.number_input("Systematic Crisis") 
    st.write("")
    X3 = st.number_input("Currency Exchange (in USD)")
    st.write("")
    X4 = st.number_input("Domestic Debts")
    st.write("")
    X5 = st.number_input("Sovereign External Debts")
    st.write("")
    X6 = st.number_input("Weighted GDP")
    st.write("")
    X7 = st.number_input("Annual Inflation CPI")
    st.write("")
    X8 = st.number_input("Independence")
    st.write("")
    X9 = st.number_input("Currency Crisis")
    st.write("")
    X10 = st.number_input("Inflation Crisis")
              
    st.write("")
    st.write("")
    
    result = ""
          
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10) 
        st.success('Prediction: {}'.format(result))
        print(result)
