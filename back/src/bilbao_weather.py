
RAINY = {
    "city": "Bilbao",
    "clouds": 1,
    "rain_probability": 0.99,
    "temperature": 15
}
NOT_SO_RAINY = {
    "city": "Bilbao",
    "clouds": 0.25,
    "rain_probability": 0.5,
    "temperature": 25
}


def get_weather():
    return RAINY


def get_weather_forecast(date_text):
    month_text = date_text.split('-')[1]

    if month_text == '07':
        return NOT_SO_RAINY

    return RAINY
