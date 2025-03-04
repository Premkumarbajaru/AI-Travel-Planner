import streamlit as st
from api_handler import handle_api_key
from travel_assistant import generate_travel_plan

st.title("AI Travel Agent Tool")

# Load API Key
api_key = handle_api_key()

# Generate Travel Plan
generate_travel_plan(api_key)
