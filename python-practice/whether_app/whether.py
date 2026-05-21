import os
import requests
from dotenv import load_dotenv

# =====================================================================
# 1. SETUP INITIALIZATION & VARIABLES
# =====================================================================
# Load your secret key from the local .env file
load_dotenv()
API_KEY = os.environ.get("whether_API_KEY")

# Safety Gatekeeper: Warn if the .env file is missing or misconfigured
if not API_KEY:
    print("❌ Error: API Key not found. Please check your local .env file setup!")
    exit()

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# =====================================================================
# 2. STEP B: CONSTRUCT THE REQUEST ENGINE
# =====================================================================
print("========================================")
print("          WEATHER DATA GATEWAY          ")
print("========================================")
city_name = input("Enter city name (e.g., Bhimavaram, London): ").strip()

if not city_name:
    print("❌ Error: City name cannot be empty.")
    exit()

query_parameters = {
    "q": city_name,
    "appid": API_KEY,
    "units": "metric"  # Ensures Celsius calculation natively
}

# Execute the HTTP network call
print(f"\n📡 Connecting to OpenWeather servers for '{city_name}'...")
response = requests.get(API_ENDPOINT, params=query_parameters)

# =====================================================================
# 3. STEP C: CHECK HTTP STATUS CODES
# =====================================================================
if response.status_code == 200:
    # 4. STEP D: DATA EXTRACTION (JSON Response Handling)
    weather_data = response.json()  # Translate JSON string into Python Dictionary
    
    # Extract values from specific structural layers of the dictionary
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["description"].title()
    country = weather_data["sys"]["country"]
    actual_city_name = weather_data["name"]

    # =====================================================================
    # DISPLAY POLISHED VISUAL RESULTS
    # =====================================================================
    print("\n" + "="*40)
    print(f"🌍 WEATHER PROFILE: {actual_city_name}, {country}")
    print("="*40)
    print(f"🌡️  Temperature : {temperature}°C")
    print(f"💧 Humidity    : {humidity}%")
    print(f"☁️  Condition   : {condition}")
    print("="*40)

elif response.status_code == 404:
    print("\n❌ Error: City not found. Please verify spelling spelling and retry.")
elif response.status_code == 401:
    print("\n❌ Error: Unauthorized connection. Your API key is invalid or pending server activation.")
else:
    print(f"\n❌ Error: Server responded with HTTP code {response.status_code}")




# import os


# import requests
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.environ.get('Whether_API_KEY')

# API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# city_name = input("Enter the City Name : ").strip()



# query_parameter = {
#     'q' : city_name,
#     'appid' : api_key,
#     'units' : 'metric'
# }

# print(f'Packaging request and seding to the whether for : {city_name}...')

# response = requests.get(API_ENDPOINT, query_parameter)