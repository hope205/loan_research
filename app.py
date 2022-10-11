import streamlit as st
import datetime 
import requests
import time
import pickle

import  model_files.process as ml
# import os



ft_acc = ['loannumber','loanamount','totaldue','termdays','bank_account_type','longitude_gps','latitude_gps',
          'bank_name_clients','employment_status_clients'
          ]


dic = {}


nav = st.sidebar.radio( "Navigation", ['Home','About','Predictions'])

if nav == 'Home':
    st.title("Customers loan default")
    st.markdown("##### *Know your customers behaviour* " )
    

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
    - Loan number : The number of the loans that we want to make our predictions on
    - Loan amount : Loan value taken
    - Total due : Total repayment required to settle the loan - this is the capital loan value disbursed + interest and fees
    - Term days : Term of loan
    - Bank account type : Type of primary bank account
    - GPS longitude : Number of teenagers in the customer's household
    - GPS latitude : Date of customer's enrollment with the company
    - Client bank name : Name of the bank
    - Client employment status : Type of employment that customer has
    
                ''',)
    
    

if nav == 'Predictions':
    
    
    st.title("Customer's Details")

    st.text("")

    st.text("")


    third,last = st.columns(2)

    

    dic["loannumber"] = last.number_input("Loan number",step= 1)  

    dic["loanamount"] = third.number_input('Loan amount',step= 1) 
    
    dic["birthdate"] = str(st.date_input('Birth date',value = datetime.date(2012, 1, 1)))


    one,two,three = st.columns(3)

    dic["bank_account_type"] = one.selectbox("Bank account type",('Savings','Current','Other',))  

    dic["bank_name_clients"] = two.selectbox('Client bank name',('Diamond Bank', 'GT Bank', 'EcoBank', 'First Bank','Access Bank', 'UBA', 'Union Bank', 'FCMB', 'Zenith Bank',
       'Stanbic IBTC', 'Fidelity Bank', 'Wema Bank', 'Sterling Bank',
       'Skye Bank', 'Keystone Bank', 'Heritage Bank', 'Unity Bank',
       'Standard Chartered'))
    
    dic["employment_status_clients"] = three.selectbox('Client employment status',('Permanent', 'Unemployed', 'Self-Employed', 'Student','Retired', 'Contract'))
    


    one,two = st.columns(2)

    dic["totaldue"] = one.number_input("Total due",step= 1) 

    dic["termdays"] = two.number_input("Term days",step=1) 
    st.text("")



    st.text("")
        
    first,second = st.columns([2,1])  

    dic["longitude_gps"] = first.number_input('GPS longitude',step= 0.001)   

    dic["latitude_gps"] = second.number_input('GPS latitude',step= 0.001)  

    st.text("")  
    
     

    first,second = st.columns(2)
    
    a =  str(first.date_input('Creation date',value = datetime.date(2017, 7, 1), min_value= datetime.date(2017, 7, 1), max_value= datetime.date(2017, 8, 1)))

    b = str(second.time_input('Creation time'))
    
    dic["creationdate"] = a + ' ' + b
    
    three,four= st.columns(2)
    
    c = three.date_input('Approved date',value = datetime.date(2017, 7, 2), min_value= datetime.date(2017, 7, 1), max_value= datetime.date(2017, 8, 1))

    d =  four.time_input('Approved time')
    
    dic["approveddate"] = str(c) + ' ' + str(d)
    
    


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

       
        
    
    
    
        



