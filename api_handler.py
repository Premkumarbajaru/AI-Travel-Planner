import streamlit as st
from config import load_api_key

def handle_api_key():
    api_key = None
    
    with st.sidebar:
        google_api_key = st.radio(
            ":blue[Select the method for Inserting Gemini API Key]",
            ["API_Key Input", "Env_API_Key"],
            captions=["Input the API key", "API key stored in .env file"]
        )

        if google_api_key == "Env_API_Key":
            api_key = load_api_key()

        elif google_api_key == "API_Key Input":
            user_input_key = st.text_input("Enter your API Key", type="password")

        if st.button("Submit API Key", key="api_submit_button", use_container_width=True):
            if google_api_key == "API_Key Input" and user_input_key:
                st.session_state["API_Key"] = user_input_key
                st.success("API Key attached successfully!")
            elif google_api_key == "Env_API_Key" and api_key:
                st.session_state["API_Key"] = api_key
                st.success("API Key loaded from environment!")
            else:
                st.error("API key not found. Please provide a valid key.")

    if "API_Key" not in st.session_state or not st.session_state["API_Key"]:
        st.warning("Please enter and submit your API Key before proceeding.")
        st.stop()

    return st.session_state["API_Key"]
