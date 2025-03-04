# AI Travel Planner

AI Travel Planner is a **Streamlit-based application** that helps users plan their trips by providing various travel options (cab, train, bus, flight) along with optimized itineraries for sightseeing. It uses **Google Gemini AI** to generate structured travel plans.

---

## 🚀 Features
- **Multiple travel options** (flight, train, bus, cab) with estimated cost & duration.
- **AI-powered itinerary generation** based on user inputs.
- **Easy API key management** using direct input.
- **User-friendly UI** built with **Streamlit**.

---

## 🛠️ Setup Instructions

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/Premkumarbajaru/AI-Travel-Planner.git
```

### 2️⃣ **Create a Virtual Environment**
It’s recommended to create a virtual environment to manage dependencies.

#### 📌 **For Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

#### 📌 **For macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

---

### 4️⃣ **Set Up API Key**
To use **Google Gemini AI**, you need to add an API key.

#### 🔹 **Method 1(a): Using `.env` File**
1. Create a `.env` file in the project root:
```sh
touch .env
```
2. Add your API key inside `.env`:
```
API_KEY=your_google_gemini_api_key_here
```
### or running using streamlit cloud deployement

#### 🔹 **Method 1(b): Using `secrets.toml` File (Recommended)**
1. Create a .streamlit/secrets.toml file.
```sh
touch .streamlit/secrets.toml
```
2. Add your API key inside `secrets.toml`:
```
GOOGLE_API_KEY = "your_google_api_key_here"
```

#### 🔹 **Method 2: Direct Input in App**
You can also enter the API key manually in the Streamlit sidebar when running the app.

---

### 5️⃣ **Run the Application**
```sh
streamlit run app.py
```

This will start the **AI Travel Agent Tool** in your browser.

---

### Running the Cloud Deployed Version

[Click here to access the deployed version](link)



## 📁 Project Structure
```
AI_Travel_Agent/
│── app.py                  # Main Streamlit application
│── config.py               # Configuration file for API keys
│── api_handler.py          # Functions for API key handling
│── streamlit_file.py       # Complete code for streamlit cloud deployment
│── travel_assistant.py     # Core logic for travel planning
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

---

## ⚡ Contributing
Feel free to contribute by opening issues and pull requests.

---

## 🔒 License
This project is licensed under the **MIT License**.

