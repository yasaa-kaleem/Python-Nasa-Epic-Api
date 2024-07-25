import requests, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

def get_nasa_epic():
    API_URL = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key": api_key
    }

    try:
        response = requests.get(API_URL, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        epic_data = response.json()
        return epic_data[0]
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"