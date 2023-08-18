import requests

API_KEY = "308edbdf7df00fd0334543aa27e7a063"


def get_data(place, fdays, dat):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*fdays]
    if dat=="Temperature":
        filtered_data = [dict['main']["temp"] for dict in filtered_data]
    if dat=="Sky":
        filtered_data = [dict['weather'][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Delhi", fdays=3, dat= "Temperature"))