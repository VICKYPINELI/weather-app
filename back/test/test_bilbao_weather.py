from src.bilbao_weather import get_weather


def test_should_return_rainy_always():
    result = get_weather()
    expected = {"city": "Bilbao",
                "clouds": 1,
                "rain_probability": 0.99,
                "temperature": 15}

    assert expected == result
