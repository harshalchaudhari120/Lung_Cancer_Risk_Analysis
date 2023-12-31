#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pickle

# Load the saved model
model = pickle.load(open("model/lung_cancer.pkl", "rb"))

st.title('Prediction Web App')
st.write("This is an interactive web page where you can select/input data to understand your chances of having lung cancer.")
st.write("Please Note that excluding gender and age all the other variables are categorical i.e. 1 means negilgible and then as the number increases,the factor affecting the risk increases.")
# Input variables (you can customize these based on your model's input features)
gender_input = st.radio("Select Gender:", ("Male", "Female"))
Age = st.number_input('Enter Age:', min_value=1, max_value=75, step=1)
Air_Pollution = st.slider('Air_Pollution', min_value=1, max_value=8, step=1)
Smoking = st.slider('Smoking', min_value=1, max_value=8, step=1)
Chest_Pain = st.slider('Chest_Pain', min_value=1, max_value=9, step=1)
Fatigue = st.slider('Fatigue ', min_value=1, max_value=9, step=1)
Weight_Loss = st.slider('Weight_Loss', min_value=1, max_value=8, step=1)
Shortness_of_Breath = st.slider('Shortness_of_Breath', min_value=1, max_value=9, step=1)
Wheezing = st.slider('Wheezing', min_value=1, max_value=8, step=1)
Swallowing_Difficulty = st.slider('Swallowing_Difficulty', min_value=1, max_value=8, step=1)
Clubbing_of_Finger_Nails = st.slider('Clubbing_of_Finger_Nails', min_value=1, max_value=9, step=1)
Frequent_Cold = st.slider('Frequent Cold', min_value=1, max_value=7, step=1)
Dry_Cough = st.slider('Dry_Cough', min_value=1, max_value=7, step=1)
Snoring = st.slider('Snoring', min_value=1, max_value=7, step=1)

if gender_input == "Male":
    gender = 1  
else:
    gender = 2
if st.button("Predict"):
    user_inputs = [[ Age,gender,Air_Pollution,Smoking,Chest_Pain,Fatigue,Weight_Loss,Shortness_of_Breath,Wheezing,Swallowing_Difficulty,Clubbing_of_Finger_Nails,Frequent_Cold,Dry_Cough,Snoring]]

    predicted_value = model.predict(user_inputs)
    if predicted_value[0]==1:
        st.write('You are at a low risk of having lung cancer.')
    elif predicted_value[0]==2:
        st.write('You are at a medium risk of having lung cancer.')
    else:
        st.write('You are at a high risk of having lung cancer.')

# In[ ]:




