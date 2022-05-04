# define las funciones del servidor web.
# ejecutar servidor: python app.py

from flask import Flask, jsonify
from flask_cors import CORS
from src.bilbao_weather import get_weather, get_weather_forecast

app = Flask("weather-app")
CORS(app)


@app.route("/", methods=["GET"])
def hello_word():
    return "<h1>...magic!</h1>"


@app.route("/bilbao", methods=["GET"])
def bilbao():
    result = get_weather()
    return jsonify(result)


@app.route("/bilbao/<isodate>", methods=["GET"])
def bilbao_forecast(isodate):
    result = get_weather_forecast(isodate)
    return jsonify(result)
