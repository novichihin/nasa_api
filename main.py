import requests
from PIL import Image
from nasapy import Nasa


def nasa_image(user_date="2022-07-07"):
    api_key = "6ogeecSWGjDM4WX6Zu1E62baaX7g4Ng5rGDIY8TO"
    nasa = Nasa(key=api_key)
    number_of_images = 0
    current_date = nasa.epic(date=user_date)
    new_format_date = user_date.replace("-", "/")
    for index, data in enumerate(current_date):
        try:
            picture = data["image"]
            r = requests.get(
                f"https://api.nasa.gov/EPIC/archive/natural/{new_format_date}/png/{picture}.png?api_key={api_key}"
            )
            if r.status_code == 200:
                with open(f"im{str(index)}.png", "wb") as f:
                    f.write(r.content)
                number_of_images += 1

        except requests.exceptions.RequestException as err:
            print(err)
    # создание gif
    gif_list = [
        Image.open(f"im{str(number)}.png") for number in range(number_of_images)
    ]

    gif_list[0].save(
        "nasa.gif",
        save_all=True,
        append_images=gif_list[1:],
        optimize=True,
        duration=300,
    )


nasa_image()
