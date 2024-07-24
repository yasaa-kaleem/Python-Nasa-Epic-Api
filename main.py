import nasa_api, webbrowser

epic_image = nasa_api.get_nasa_epic_image_data("2024", "07", "21", "png")
print("Opening Image...")
webbrowser.open(epic_image)
print("Image opened! Exiting program...")