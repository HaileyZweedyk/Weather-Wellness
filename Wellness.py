def suggest_clothing(temp):
   if 0 < temp < 9:
       print("The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
   elif 10 < temp < 32:
       print("It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
   elif 33 <= temp <= 55:
       print("The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
   elif 56 <= temp <= 69:
       print("The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
   elif 70 <= temp <= 84:
       print("The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
   else:
       print("It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes.")


def suggest_activities(weather_condition):
   if weather_condition == "sunny":
       print("Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
   elif weather_condition == "cloudy":
       print("It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
   elif weather_condition == "partly sunny":
       print("It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo.")
   elif weather_condition == "rainy":
       print("It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
   elif weather_condition == "windy":
       print("Look out it's windy today! You could go to the mall, do some chores inside, or try flying a kite.")
       elif weather_condition == "snowy":
       print("It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
   elif weather_condition == "thunderstorms":
       print("Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie.")
   else:
       print("Weather condition not recognized. Check the forecast for more information.")


def driving_techniques(weather_condition):
   if weather_condition == "snow":
       print("Tips for driving in the snow: ")
       print("- Slow down and reduce your speed.")
       print("- Increase your following distance.")
       print("- Drive in the tire tracks of other vehicles if possible.")
       print("- Avoid sudden steering or braking to prevent loss of control.")
       print("- Keep headlights on for better visibility.")
   elif weather_condition == "ice":
       print("Tips for driving in icy conditions: ")
       print("- Drive at a much slower speed.")
       print("- Avoid using cruise control.")
       print("- Brake gently and avoid sudden movements that could cause skidding.")
       print("- Increase following distance significantly.")
       print("- Stay in your lane and avoid abrupt steering.")
   elif weather_condition == "wind":
       print("Tips for driving in windy conditions: ")
       print("- Grip the steering wheel firmly and use both hands.")
       print("- Be aware of large gusts of wind that could move the car.")
       print("- Stay cautious around large vehicles like trucks and buses.")
       print("- Keep a larger distance from other vehicles to avoid being pushed by wind.")
   elif weather_condition == "rain":
       print("Tips for driving in the rain: ")
       print("- Slow down and reduce speed to avoid slipping.")
       print("- Increase your following distance to give yourself more stopping time.")
       print("- Use your headlights and windshield wipers for better visibility.")
       print("- Avoid driving through large puddles or flooded areas.")
       print("- Turn off cruise control to maintain full control of your vehicle.")
   elif weather_condition == "thunderstorm":
       print("Tips for driving in a thunderstorm: ")
       print("- Use your headlights and windshield wipers to maximize visibility.")
       print("- Avoid driving through flooded areas to prevent hydroplaning.")
       print("- Be aware of sudden gusts of wind and potential debris on the road.")
       print("-If conditions are severe pull over in a covered area to let the storm pass.")
   else:
       print("Weather condition not recognized. Please enter a valid condition (snow, ice, wind, rain, or thunderstorm).")


def mood_weather(weather_condition):
    if weather_condition == "sunny":
        print("The sun is shining out! Carry this positivity and enthusimum from the beautiful sunshine into whatever you may do today to keep the good vibes going.")
    elif weather_condition == "cloudy":
        print("There is no sun today. You may be feeling a little down and unmotivated with out the sunshine.")
    elif weather_condition == "rainy":
        print("Oh no, not the rain! Watch out for the rainy day blues, this weather may have you feeling sad.")
    elif weather_condition == "thunderstorms":
        print("It's storming out. Don't be shocked if you are feeling down or shaken at times today.")
    elif weather_condition == "snowy":
        print("It's snowing outside. Look out for the chill in the air and a low spritied mood today.")
    else:
       print("Weather condition not recognized. Please enter a valid condition (sunny, cloudy,snowy, rain, or thunderstorm).")

def mood_forecast():
    pass
    # Generate forecast from Weather.py
    # print(f"{day}: mood_weather(weather_condition)", end="")
    