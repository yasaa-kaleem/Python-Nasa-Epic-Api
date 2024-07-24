import requests, os
from dotenv import load_dotenv

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
        return epic_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"


def get_nasa_epic_image_data(year, month, day, file_name, image_type):
    # epic_data = get_nasa_epic(api_key)
    # epic_data_dict = dict(epic_data[0])

    API_URL = "https://epic.gsfc.nasa.gov/archive/natural/"

    try:
        response = requests.get(API_URL+f"{year}/{month}/{day}/{image_type}/{file_name}.{image_type}")
        response.raise_for_status()
        return response.url
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"

#2015/10/31/png/epic_1b_20151031074844.png
#print(epic_data_dict["date"])
# print(epic_data_dict)
# print(epic_data_dict["image"])
# print(epic_data_dict["date"])
# print(epic_data_dict["image"])
#epic_image = get_nasa_epic_image_data("2015", "10", "31", "png", "epic_1b_20151031074844.png")

# open the epic image in a browser
#