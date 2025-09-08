# app.py
import streamlit as st
import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load iris dataset to get class names
iris = load_iris()
class_names = iris.target_names

st.title("Iris Flower Prediction")

# Input features
sepal_length = st.number_input("Sepal Length", 0.0, 10.0)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0)
petal_length = st.number_input("Petal Length", 0.0, 10.0)
petal_width = st.number_input("Petal Width", 0.0, 10.0)

if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Class: {class_names[prediction]}")
