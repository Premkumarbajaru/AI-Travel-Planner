import datetime
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

def setup_chat_model(api_key):
    return ChatGoogleGenerativeAI(
        api_key=api_key, 
        model="gemini-2.0-flash-exp", 
        temperature=1
    )

def create_prompt():
    return ChatPromptTemplate(
        messages=[
            ('system', """You are an AI-powered travel assistant. 
                          Your task is to provide multiple travel options (cab, train, bus, flight) for a given source, destination, and travel date/time. 
                          Include estimated costs, travel durations, and relevant details such as ticket availability, class options, and layovers. 
                          Additionally, suggest an optimized itinerary covering must-visit places along the journey, organizing them by date and time for a well-structured trip."""),

            ('human', """I am traveling from {source} to {destination} from {start_date} to {end_date}. 
                         Provide me with multiple travel options, including estimated cost, duration, and key details. 
                         Additionally, create a structured itinerary to explore famous attractions during my trip, organized by date and time.""")
        ]
    )

def get_travel_details():
    source = st.text_input("Enter your source location", key="source")
    destination = st.text_input("Enter your destination location", key="destination")

    today = datetime.date.today()
    min_days = 1
    max_days = 28  # 4 weeks

    duration = st.date_input(
        "Select your vacation dates (1 to 28 days only)",
        (today, today + datetime.timedelta(days=1)),  # Default: 1 day from today
        min_value=today,
        max_value=today + datetime.timedelta(days=365),  # Limit to 1 year ahead
    )

    if isinstance(duration, tuple) and len(duration) == 2:
        start_date, end_date = duration
        trip_days = (end_date - start_date).days

        if trip_days < min_days or trip_days > max_days:
            st.error(f"Please select a duration between **1 day to 28 days (4 weeks)**. Your selection: **{trip_days} days**.")
            st.stop()

        # Format dates to DD-MM-YY for processing
        formatted_start_date = start_date.strftime("%d-%m-%y")
        formatted_end_date = end_date.strftime("%d-%m-%y")

        # Display selected dates in DD-MM-YY format for clarity
        st.write(f"**Selected Start Date:** {formatted_start_date}")
        st.write(f"**Selected End Date:** {formatted_end_date}")

        return source, destination, formatted_start_date, formatted_end_date
    else:
        st.error("Please select a valid date range.")
        st.stop()

def generate_travel_plan(api_key):
    chat_model = setup_chat_model(api_key)
    prompt = create_prompt()
    output_str = StrOutputParser()

    source, destination, start_date, end_date = get_travel_details()

    left, middle, right = st.columns(3)
    if middle.button("Submit Travel Plan", key="travel_submit_button", use_container_width=True):
        chain = prompt | chat_model | output_str
        location = {
            "source": source, 
            "destination": destination, 
            "start_date": start_date,
            "end_date": end_date,
        }
        output = chain.invoke(location)
        st.write(output)

def handle_api_key():
    api_key = None
    with st.sidebar:
        google_api_key = st.radio(
            ":blue[Select the method for Inserting Gemini API Key]",
            ["API_Key Input", "Env_API_Key"],
            captions=["Input the API key", "API key stored in .env file"]
        )
        if google_api_key == "Env_API_Key":
            api_key = st.secrets.get("GOOGLE_API_KEY")
        elif google_api_key == "API_Key Input":
            user_input_key = st.text_input("Enter your Gemini API Key", type="password")

        if st.button("Submit API Key", key="api_submit_button", use_container_width=True):
                    if google_api_key == "API_Key Input" and user_input_key:
                        st.session_state["API_Key"] = str(user_input_key)
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
    
# Run the application
if __name__ == "__main__":
    st.set_page_config(page_title="AI Travel Assistant", page_icon="✈️", layout="wide")
    st.title("AI Travel Assistant")
    api_key = handle_api_key()
    generate_travel_plan(api_key)