import nasa_api, webbrowser
epic_image = nasa_api.get_nasa_epic_image_data("2015", "10", "31", "epic_1b_20151031074844", "png")
webbrowser.open(epic_image)