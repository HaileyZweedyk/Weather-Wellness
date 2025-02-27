from Weather import Weather
from WeatherCodeTranslations import WeatherCodeTranslations

weather = Weather()
lat, long = weather.SetCurrLoc()
weatherDataCurr = weather.ViewCurrWeather(lat, long)
CurrWeatherCode = weatherDataCurr["CurrWeatherCode"]
CurrTemp = weatherDataCurr["CurrTemp"]
weather_condition = WeatherCodeTranslations.GetCategory(CurrWeatherCode)

CurrWeatherCode = weatherDataCurr.get("CurrWeatherCode", None)
CurrTemp = weatherDataCurr.get("CurrTemp", None)


class Clothing:
    @staticmethod
    def suggest_clothing(CurrTemp):
        if CurrTemp < 0:
            condition = "very_cold"
        elif 0 <= CurrTemp <= 9:
            condition = "single_digits"
        elif 10 <= CurrTemp <= 32:
            condition = "cold"
        elif 33 <= CurrTemp <= 55:
            condition = "chilly"
        elif 56 <= CurrTemp <= 69:
            condition = "moderate"
        elif 70 <= CurrTemp <= 84:
            condition = "warm"
        else:
            condition = "hot"
        clothing_suggestions = {
            "very_cold": "Temperature is in the negatives today. Avoid going outside, but if necessary, dress in heavy layers and make sure your ears, nose, and hands are covered at all times.",
            "single_digits": "The temperature is in the single digits. When outside, keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.",
            "cold": "It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.",
            "chilly": "The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and closed-toe shoes.",
            "moderate": "The temperature is moderate. Pair a light jacket or long sleeves with pants. Otherwise, a sweatshirt or thick jacket with shorts. Wear closed-toe shoes.",
            "warm": "The temperature is warm. Wear a T-shirt or tank top, shorts, and sandals or tennis shoes. If it’s sunny, consider adding sunglasses or a hat.",
            "hot": "It's very hot outside! Wear lightweight, flowy clothing, a hat, and sandals or tennis shoes."
        }

        clothing_suggestion = clothing_suggestions.get(condition)

        print(clothing_suggestion)

        return clothing_suggestion


class Activities:
    @staticmethod
    def suggest_activities(weather_condition):
        suggestions = {
            "Sunny": "Walking, hiking, biking, going to the beach, or having a picnic.",
            "Cloudy": "Visiting a café, museum, or running some errands.",
            "Rain": "Reading, watching movies, cooking, or doing a puzzle.",
            "Haze": "Go to a really scenic location and take some cool pictures! Or play a board game or watch a movie.",
            "Fog": "Pray that there is a 2 hour delay for school. Stay inside and hang out but if you're feeling it, head out for a walk still",
            "Snow": "Sledding, snowboarding, skiing, or staying inside with a book.",
            "Thunderstorm": "Staying inside and doing yoga, puzzles, or watching a movie."
        }
        suggestion = suggestions.get(weather_condition)
        print(suggestion)
        return suggestion

class Driving:
    @staticmethod
    def driving_techniques(weather_condition):
        tips = {
            "Snow": "- Slow down and increase your following distance.\n- Avoid sudden steering or braking.\n- Drive in the tire tracks of other vehicles.",
            "Ice": "- Drive much slower.\n- Avoid cruise control.\n- Brake gently to avoid skidding.",
            "Wind": "- Grip the steering wheel firmly.\n- Stay cautious around large vehicles.\n- Keep a larger distance from other vehicles.",
            "Rain": "- Reduce speed to avoid slipping.\n- Increase following distance.\n- Use headlights and windshield wipers.",
            "Thunderstorm": "- Use headlights and windshield wipers.\n- Avoid flooded areas.\n- If conditions are severe, pull over safely.",
            "Cloudy": "- No driving techniques are reccomended due to todays condition",
            "Clear": "- No driving techniques are reccomended due to todays condition",
            "Sunny": "- No driving techniques are reccomended due to todays condition"
        }
        tip = tips.get(weather_condition)
        print(tip)
        return tip

class Mood_Weather:
    @staticmethod
    def mood_weather(weather_condition):
        moods = {
            "Sunny": "Take advantage of the sunshine and soak up some vitamin D (wear sunscreen).",
            "Cloudy": "It’s a cloudy day. Keep your spirits high and make the most of it.",
            "Rainy": "Try to stay positive even though today might feel dreary.",
            "Thunderstorm": "Storms pass. Take care of yourself and relax indoors.",
            "Snow": "Snow can be gloomy, but take care of yourself and make the day cozy."
        }
        mood = moods.get(weather_condition)
        print(mood)
        return mood

        

class Mood_Forecast:
    @staticmethod
    def mood_forecast():
        pass  # Future integration for forecast-based mood predictions

Clothing.suggest_clothing(CurrTemp)
Activities.suggest_activities(weather_condition)
Driving.driving_techniques(weather_condition)
Mood_Weather.mood_weather(weather_condition)