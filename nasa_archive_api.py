import nasa_epic_api, requests

def get_splitted_date(epic_data):
    # Original date time from response
    date_time_str = epic_data["date"]

    # Splitting date and time
    date_str = date_time_str.split(" ")[0]

    # Splitting year month and day
    splitted_date = date_str.split("-")
    return splitted_date

def get_nasa_epic_image_data():
    API_URL = "https://epic.gsfc.nasa.gov/archive/natural/"
    image_type = "png"

    # Getting response
    epic_data = nasa_epic_api.get_nasa_epic()
    epic_data_dict = dict(epic_data)

    # Image name from response
    file_name = epic_data_dict["image"]

    # Getting splitted date
    splitted_date = get_splitted_date(epic_data)

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