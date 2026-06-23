import streamlit as st
import pandas as pd
import pickle

# Page setup
st.set_page_config(
    page_title="Car Price Prediction App",
    layout="wide"
)

# Load trained model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Custom CSS
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
}
.subtitle {
    font-size: 18px;
    color: #9CA3AF;
}
.card {
    background-color: #111827;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #374151;
    margin-bottom: 20px;
}
.price-box {
    background-color: #064E3B;
    padding: 24px;
    border-radius: 16px;
    text-align: center;
}
.price-text {
    font-size: 36px;
    font-weight: 700;
    color: white;
}
.label {
    color: #9CA3AF;
    font-size: 14px;
}
.value {
    font-size: 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Vehicle Information")
st.sidebar.write("Enter the car details below.")

year = st.sidebar.slider("Manufacturing Year", 2000, 2024, 2015)
kms_driven = st.sidebar.slider("Kilometers Driven", 0, 500000, 30000)
fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.sidebar.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])

# Convert user inputs to model format
fuel_type_diesel = 1 if fuel_type == "Diesel" else 0
fuel_type_petrol = 1 if fuel_type == "Petrol" else 0
seller_type_individual = 1 if seller_type == "Individual" else 0
transmission_manual = 1 if transmission == "Manual" else 0

input_data = pd.DataFrame({
    "Year": [year],
    "Kms_Driven": [kms_driven],
    "Fuel_Type_Diesel": [fuel_type_diesel],
    "Fuel_Type_Petrol": [fuel_type_petrol],
    "Seller_Type_Individual": [seller_type_individual],
    "Transmission_Manual": [transmission_manual]
})

# Prediction
prediction = model.predict(input_data)[0]

# Header
st.markdown('<div class="main-title">Car Price Prediction App</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A machine learning web application that estimates the selling price of a used car.</div>',
    unsafe_allow_html=True
)

st.divider()

# Layout
left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Vehicle Details")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="label">Manufacturing Year</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="value">{year}</p>', unsafe_allow_html=True)

        st.markdown('<p class="label">Fuel Type</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="value">{fuel_type}</p>', unsafe_allow_html=True)

        st.markdown('<p class="label">Transmission</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="value">{transmission}</p>', unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="label">Kilometers Driven</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="value">{kms_driven:,} km</p>', unsafe_allow_html=True)

        st.markdown('<p class="label">Seller Type</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="value">{seller_type}</p>', unsafe_allow_html=True)

        st.markdown('<p class="label">Model Used</p>', unsafe_allow_html=True)
        st.markdown('<p class="value">Random Forest Regressor</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="price-box">', unsafe_allow_html=True)
    st.markdown("### Estimated Selling Price")
   
    st.markdown(f'<div class="price-text">${prediction:.2f}k</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.info(
        "This prediction is an estimated value based on historical car data. "
        "Actual prices may vary depending on market condition, car condition, and location."
    )

st.divider()

# About section
st.subheader("About This Project")

st.write(
    """
    This project uses a Random Forest Regressor to predict used car selling prices.
    The model was trained using features such as manufacturing year, kilometers driven,
    fuel type, seller type, and transmission type.
    """
)

st.write("**Technologies Used:** Python, Pandas, Scikit-learn, Streamlit")