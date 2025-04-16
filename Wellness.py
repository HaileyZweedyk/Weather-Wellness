
class Wellness:

    def __init__(self):
        self.journal = {}


    def suggest_clothing(self, temp):
        if temp < 0:
            return "Temperature is in the negatives today. Avoid going outside, but if necessary, dress in heavy layers and make sure your ears, nose, and hands are covered at all times."
        elif 0 < temp < 9:
            return "The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots."
        elif 10 <= temp <= 32:
            return "It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat."
        elif 33 <= temp <= 55:
            return "The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes."
        elif 56 <= temp <= 69:
            return "The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes."
        elif 70 <= temp <= 84:
            return "The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat."
        else:
            return "It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes."


    def suggest_activities(self, weather_condition):
        if weather_condition == "Sunny":
            return "Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one."
        elif weather_condition == "Cloudy" or weather_condition == "Haze" or weather_condition == "Fog" or weather_condition == "Mostly Cloudy":
            return "It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one."
        elif weather_condition == "Partly Sunny":
            return "It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo."
        elif weather_condition == "Rain":
            return "It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. "
        elif weather_condition == "Snow" or weather_condition == "Wintery Mix":
            return "It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book."
        elif weather_condition == "Thunderstorm":
            return "Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie."
        else:
            return "Weather condition not recognized. Check the forecast for more information."


    def driving_techniques(self, weather_condition):
        if weather_condition == "snow":
            return "Tips for driving in the snow:\n- Slow down and reduce your speed.\n- Increase your following distance.\n- Drive in the tire tracks of other vehicles if possible.\n- Avoid sudden steering or braking to prevent loss of control.\n- Keep headlights on for better visibility."
        elif weather_condition == "rain":
            return "Tips for driving in the rain:\n- Slow down and reduce speed to avoid slipping.\n- Increase your following distance to give yourself more stopping time.\n- Use your headlights and windshield wipers for better visibility.\n- Avoid driving through large puddles or flooded areas.\n- Turn off cruise control to maintain full control of your vehicle."
        elif weather_condition == "thunderstorm":
            return "Tips for driving in a thunderstorm:\n- Use your headlights and windshield wipers to maximize visibility.\n- Avoid driving through flooded areas to prevent hydroplaning.\n- Be aware of sudden gusts of wind and potential debris on the road.\n-If conditions are severe pull over in a covered area to let the storm pass."
        else:
            return "Driving Conditions Safe. Practice defensive driving techniques."


# we need to resonsider this probs need input statments
    def mood_weather(self, weather_condition):
        if weather_condition == "Sunny" or weather_condition == "Partly Cloudy":
            return "The sun is shining out! Take advantage of this beautiful sunshine and soak up some vitamin D (not too much though, wear your sunscreen)."
        elif weather_condition == "Clear":
            return "The moon is out and the sky is dark! You might start to feel tired, so prioritize getting some sleep, but also enjoy some of the feelings of nighttime activities."
        elif weather_condition == "Cloudy" or weather_condition == "Haze" or weather_condition == "Foggy" or weather_condition == "Mostly Cloudy":
            return "There is no sun today. You might be feeling a little down today, but don't let that stop you from having a great day."
        elif weather_condition == "Rainy":
            return "It's a rainy one today. Try to keep your spirits high even though today might seem dreary."
        elif weather_condition == "Thunderstorm":
            return "It's storming out. If you're up for it, watch the storms roll through. Otherwise, take care of yourself because sunny days are inevitable."
        elif weather_condition == "Snowy":
            return "It's snowing outside. Snow can really bring down our mood sometimes, so it is important to take care of yourself today."
        else:
            return "Weather condition not recognized. Please enter a valid condition (sunny, cloudy, snowy, rain, or thunderstorm)."

    

    

    