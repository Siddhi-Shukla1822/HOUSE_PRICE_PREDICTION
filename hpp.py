import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = r'C:\Users\suyas\Downloads\model (1).pkl'  # Use the correct file path
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title("House Price Prediction Web App")
st.write("Enter the house details to predict the price.")

# Input Fields
area = st.number_input("Area (sq. ft.)", min_value=500, max_value=5000, value=1500)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
stories = st.number_input("Number of Stories", min_value=1, max_value=3, value=1)

# Binary Inputs (Yes/No)
mainroad = st.radio("Main Road (Yes/No)", ('Yes', 'No')) == 'Yes'
guestroom = st.radio("Guestroom (Yes/No)", ('Yes', 'No')) == 'Yes'
basement = st.radio("Basement (Yes/No)", ('Yes', 'No')) == 'Yes'
hotwaterheating = st.radio("Hot Water Heating (Yes/No)", ('Yes', 'No')) == 'Yes'
airconditioning = st.radio("Air Conditioning (Yes/No)", ('Yes', 'No')) == 'Yes'
parking = st.number_input("Parking Space (Number of Vehicles)", min_value=0, max_value=10, value=1)

# Categorical Input for Furnishing Status
furnishingstatus = st.selectbox("Furnishing Status", ('Unfurnished', 'Semi-Furnished', 'Furnished'))

# Binary Input for Preferred Area
prefarea = st.radio("Preferred Area (Yes/No)", ('Yes', 'No')) == 'Yes'

# Prepare input for the model and make prediction
if st.button("Predict"):
    input_data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                            hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])
    
    # Handle categorical feature (furnishingstatus) encoding (if necessary)
    input_data_encoded = np.array([[
        area, 
        bedrooms, 
        bathrooms, 
        stories, 
        int(mainroad), 
        int(guestroom), 
        int(basement), 
        int(hotwaterheating), 
        int(airconditioning), 
        parking, 
        int(prefarea), 
        furnishingstatus == 'Furnished'  # Assuming this needs encoding for the model
    ]])

    prediction = model.predict(input_data_encoded)[0]  # Predict using the loaded model
    st.write(f"### Predicted Price: ${prediction:,.2f}")
