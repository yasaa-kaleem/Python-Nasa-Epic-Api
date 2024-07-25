import requests, os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

def get_nasa_epic(api_key):
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


def get_nasa_epic_image_data():
    API_URL = "https://epic.gsfc.nasa.gov/archive/natural/"
    image_type = "png"

    # Getting response
    epic_data = get_nasa_epic(api_key)
    epic_data_dict = dict(epic_data)

    # Image name from response
    file_name = epic_data_dict["image"]

    # Original date time from response
    date_time_str = epic_data_dict["date"]

    # Splitting date and time
    date_str = date_time_str.split(" ")[0]

    # Splitting year month and day
    splitted_date = date_str.split("-")

    # setting variables
    year = splitted_date[0]
    month = splitted_date[1]
    day = splitted_date[2]

    try:
        response = requests.get(API_URL+f"{year}/{month}/{day}/{image_type}/{file_name}.{image_type}")
        response.raise_for_status()
        return response.url
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"