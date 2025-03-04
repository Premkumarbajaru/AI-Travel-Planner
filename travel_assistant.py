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
    max_days = 28

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

        return source, destination, start_date, end_date
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
            "start_date": start_date.strftime(r"%d-%m-%Y"),
            "end_date": end_date.strftime(r"%d-%m-%Y"),
        }
        output = chain.invoke(location)
        st.write(output)
