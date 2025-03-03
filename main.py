import streamlit as st
import pickle
import numpy as np



dataset = pickle.load(open("BANK_CHURN_DATASET.pkl", "rb"))
pipe = pickle.load(open("pipe_BANK_CHURN.pkl", "rb"))





st.header("BANK CUSTOMER CHURN PREDICTION")



col1 , col2  = st.columns(2)




with col1:
    #customer name
    name = st.text_input("Customer Name")






with col2:
    #customer id
    cus_id = st.text_input("Customer ID")





col1 , col2  = st.columns(2)




with col1:
    #age
    age = st.number_input("Age" , min_value= 18 , max_value=100)





with col2:
    #gender
    gender = st.selectbox("Gender" , dataset["Gender"].unique() )


col1 , col2  = st.columns(2)



with col1:
    #customer location
    cus_location = st.selectbox("Location" , dataset["Geography"].unique())




with col2:
    #CREDITSCCORE
    credit_score = st.number_input("Creditscore" , min_value=0  )


col1 , col2  = st.columns(2)

with col1:
    #balance
    balance = st.number_input("Bank Balance" , min_value= 0.0)

with col2:
    #estimates salsary
    esti_salary = st.number_input("Estimated Salary" , min_value=0.0)

#tenure
tenure = st.number_input("How many years does the customer been a client of the bank?" , min_value=0)


#num of products
num_products = st.number_input("How many products did the customer purchase through bank?" , min_value=0)

#active memeber
active_member = st.selectbox("Is the customer a active member of the bank?" , [ "","Yes","No"])

if active_member == "Yes":
    active_member = 1
else:
    active_member = 0

#has credit card
credit_card = st.selectbox("Does the customer own a credit card?" , ["" , "Yes" , "No"])

if credit_card == "Yes":
    credit_card = 1
else:
    credit_card = 0


if credit_card == 1:

    #card type
    card_type = st.selectbox("What is the credit card type?" , dataset["Card Type"].unique())

    #points earned
    points_earned = st.number_input("How many points have the customer earned by using the credit card?", min_value=0)


if credit_card == 0:
    #card_type = dataset["Card Type"][12]
    card_type = "SILVER"

    points_earned = 225.967846



#complain
complain = st.selectbox("Did anything the customer complained about the bank service?" , ["" , "Yes" , "No"])

if complain == "Yes":
    complain = 1
else:
    complain = 0



if complain == 1:

    #satisfaction score
    satisfactory_score = st.number_input( "What was the score provided by the customer for their complain resolution?" , min_value=0)

if complain == 0:
    satisfactory_score =  1

if st.button("Predict"):

    query = np.array([credit_score,cus_location,gender,age,tenure ,
                      balance, num_products , credit_card , active_member,
                      esti_salary,complain,satisfactory_score,card_type,
                      points_earned])



    query = query.reshape(1, 14)

    x = pipe.predict(query)[0]

    if x == 1:
        st.header( name + " is more likely to QUIT the bank services")

    else:
        st.header( name +  " will CONTINUE with the bank services")



