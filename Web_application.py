# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 09:30:58 2025
"""

import streamlit as st
import pickle
import numpy as np

loaded_model = pickle.load(open("C:/Users/KIRTAN/Desktop/Lucky codes/MachineLEarning/House_price_pridictor.sav", 'rb'))

def predict_price(input_data):
    input_np = np.array([input_data], dtype=float)
    prediction = loaded_model.predict(input_np)
    return prediction[0]


def main():
    st.set_page_config(page_title="Mumbai House Price Predictor", layout="centered")
    st.title("🏠 Mumbai House Price Predictor")

    st.markdown("### Fill the following details:")

    # BHK
    bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=2)

    # Type
    type_map = {'Apartment': 0, 'Independent House': 1}
    type_selected = st.selectbox("Type of House", list(type_map.keys()))
    type_encoded = type_map[type_selected]

    # Locality
    locality = st.text_input("Locality", "Andheri West")

    # Area
    area = st.number_input("Area in sq.ft", min_value=100, max_value=10000, value=650)

    # Region
    region_options = [
        'Andheri West', 'Borivali West', 'Panvel', 'Naigaon East',
        'Mira Road East', 'Kandivali East', 'Thane West', 'Goregaon East',
        'Vasai West', 'Mulund West', 'Other'
    ]
    region_selected = st.selectbox("Region", region_options)
    region_encoded = region_options.index(region_selected)  # example encoding

    # Status
    status_map = {'Ready to move': 0, 'Under Construction': 1}
    status_selected = st.selectbox("Construction Status", list(status_map.keys()))
    status_encoded = status_map[status_selected]

    # Age
    age = st.slider("Age of the house (in years)", min_value=0, max_value=50, value=5)

    if st.button("Predict Price"):
        try:
            input_data = [bhk, type_encoded, age, area, region_encoded, status_encoded, 0]  # 0 for dummy locality 
            predicted_price = predict_price(input_data)
            st.success(f"💰 Estimated House Price: ₹ {round(predicted_price):,}")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    main()
