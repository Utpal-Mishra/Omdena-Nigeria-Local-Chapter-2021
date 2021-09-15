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
    classifier = joblib.load('five') 
    #classifier = pickle.load(pickle_in)
     
    
    # defining the function which will make the prediction using the data which the user inputs 
    def prediction(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10):   
     
            # Making predictions 
        prediction = classifier.predict( 
            [[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]])
         
        if prediction == 0:
            pred = 'Eligible to Open Bank Account'
        else:
            pred = 'Not Eligible to Open Bank Account'
            
        return pred
      
    
    
    # this is the main function in which we define our webpage  
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Check Bank Account Eligibility</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
          
    st.write("")
    st.write("")
    
    # following lines create boxes in which user can enter data required to make prediction 
    X1 = st.number_input("In which East African country you live? [0: Rwanda; 1: Tanzania; 2: Kenya; 3: Uganda]")
    st.write("")
    X2 = st.number_input("Which area you belong to? [0: Rural; 1: Urban]")
    st.write("")
    X3 = st.number_input("Do you have cellphone accessibility? [0: No; 1: Yes]")
    st.write("")
    X4 = st.number_input("What is the size of your family?")
    st.write("")
    X5 = st.number_input("What is your age?")
    st.write("")
    X6 = st.number_input("What is your gender? [0: Female; 1: Male]")
    st.write("")
    st.write("")
    X7 = st.number_input("What is your relation with your family head? [0. Head of Household; 1: HSpouse; 2: HChild; 3: HParent; 4: HOther relative; 5: HOther non-relatives]")   
    st.write("")
    X8 = st.number_input("What is your marital status? [0: Married/Living together; 1: Single/Never Married; 2: Widowed; 3: Divorced/Seperated; 4: Dont know/ Other]")
    st.write("")
    X9 = st.number_input("What is your education level? [0: Primary education; 1: No formal education; 2: Secondary education; 3: Tertiary education; 4: Vocational/Specialised training; 5: Other/Dont know/RTA]")
    st.write("")
    X10 = st.number_input("What is your job type? [0: Self Employed; 1: Informally employed; 2: Farming and Fishing; 3: Remittance Dependent; 4: Other Income; 5: Formally employed Private; 6: No Income; 7: Formally employed Government; 8: Government Dependent; 9: Dont Know/Refuse to answer] ")

    st.write("")
    st.write("")
    
    result = ""
          
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10) 
        st.success('Prediction: {}'.format(result))
        print(result)