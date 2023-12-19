import streamlit as st
import datetime 
import requests
import time
import pickle

import  model_files.process as ml
# import os



ft_acc = [
    "Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount",
    "Loan_Amount_Term","Credit_History","Property_Area"				
          ]

dic = {}


nav = st.sidebar.radio( "Navigation", ['Home','About','Predictions'])


if nav == 'Home':
    st.title("Customers loan default")

    

    st.text("")
    
    st.text("")
    
    
    st.image(
            "https://new-media.dhakatribune.com/en/uploads/2022/06/14/bigstock-loan-default-word-on-note-with-3721537211.jpeg",
           
            # Manually Adjust the width of the image as per requirement
        )
    
    
if nav == 'About':
    st.title("Project Description")
    # st.markdown("##### *Know your customers behaviour* " )
    
    st.write(
        """
        
        This project makes use of an Artificial Intelligence(AI) algorithm to predict if customers are eligible for loan collection 
        based on their performance of previous loans they have collected and some personal attributes
        
        
        """
             )
    
    st.text("")
    
    st.text("")
    
    st.text("")
    
    st.markdown("##### *Here is an outine of customers details and their meanings*")

    
    st.info(
    ''' 
     
    - Gender : The gender of the customer wether male or female
    - Loan amount : Loan value taken
    - Applicant Income : The amount of income of the applicant 
    - Coapplicant Income : The amount of income of the co applicant 
    - Loan amount term : Duration of the loan 
    - Credit history : Historyof credit teh customer already has
    - Property area : Where is the customers property located
    - Married : Marital status
    - Education : Heighest type of education that customer has
    - Self employed : Is the customer self employed or not
    
                ''',)
    
    

if nav == 'Predictions':
    
    
    st.title("Customer's Details")

    st.text("")

    st.text("")


  

    one,two,three = st.columns(3)

    dic["Married"] = one.selectbox("Married",('No', 'Yes'))  

    dic["Education"] = two.selectbox('Education',('Graduate', 'Not Graduate'))
    
    dic["Self_Employed"] = three.selectbox('Self_Employed',('No', 'Yes'))
    


    one,two  = st.columns(2)

    dic["ApplicantIncome"] = one.number_input("Applicant Income",step= 1) 

    dic["CoapplicantIncome"] = two.number_input("Coapplicant Income",step=1) 
    
    
    
    st.text("")

    dic["Gender"] = st.selectbox("Gender",('Male', 'Female')) 

    st.text("")
        
    first,second = st.columns([2,1])  

    dic["LoanAmount"] = first.number_input('Loan Amount')   

    dic["Loan_Amount_Term"] = second.number_input('Loan Amount Term')  

    st.text("") 
    
    met,bet = st.columns(2)

    dic["Credit_History"] = met.number_input("Credit History",step= 1) 

    dic["Property_Area"] = bet.selectbox("Property Area",('Urban', 'Rural', 'Semiurban'))  
    
    st.text("")
    
    


    with open('./model_files/loan_model.sav', 'rb') as fa:
        model = pickle.load(fa)
        fa.close()

        
    if st.button("Submit"):
        
        
        
        prediction = ml.predict(dic,model)
        
        with st.spinner('Wait for it...'):
            time.sleep(2)
        
        
        print('New prediction: ', prediction)
        
        if prediction == 1:
            st.success('This customer is eligible for this loan')
        else:
            st.success('This customer is not eligible for this loan') 

       
        
    
    
    
        



