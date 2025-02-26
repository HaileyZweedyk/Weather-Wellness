import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Clothing, Activites, Driving, Mood_Weather, Mood_Forecast

class TestWeatherCodeTranslations(unittest.TestCase):
    def test_get_conditions(self):
        self.assertEqual(WeatherCodeTranslations.GetConditions(0), "Clear")
        self.assertEqual(WeatherCodeTranslations.GetConditions(6), "Not in Current Database")
        self.assertEqual(WeatherCodeTranslations.GetConditions(11), "Fog")
        self.assertEqual(WeatherCodeTranslations.GetConditions(22), "Snow")
        self.assertEqual(WeatherCodeTranslations.GetConditions(81), "Rain")
        self.assertEqual(WeatherCodeTranslations.GetConditions(85), "Light Snow")
        self.assertEqual(WeatherCodeTranslations.GetConditions(97), "Thunderstorm")
    
    def test_get_category(self):
        self.assertEqual(WeatherCodeTranslations.GetCategory(3), "Cloudy")
        self.assertEqual(WeatherCodeTranslations.GetCategory(0), "Clear") 
        self.assertEqual(WeatherCodeTranslations.GetCategory(81), "Rain")    
        self.assertEqual(WeatherCodeTranslations.GetCategory(5), "Haze")  
        self.assertEqual(WeatherCodeTranslations.GetCategory(43), "Fog")
        self.assertEqual(WeatherCodeTranslations.GetCategory(3), "Cloudy")
        self.assertEqual(WeatherCodeTranslations.GetCategory(29), "Thunderstorm")
        self.assertEqual(WeatherCodeTranslations.GetCategory(26), "Snow")
        self.assertEqual(WeatherCodeTranslations.GetCategory(100), "Not in Current Database")

class TestWeather(unittest.TestCase):
    def test_forecast_daily(self):
        pass
    def test_forecast_hourly(self):
        pass
    def test_view_curr_weather(self):
        pass
    def test_set_curr_location(self):
        pass

class TestWellness(unittest.TestCase):
    def test_suggest_clothing_negative(self):
        self.assertEqual(Clothing.suggest_clothing(-1),"Temperature is in the negatives today. Avoid going outside, but if necessary, dress in heavy layers and make sure your ears, nose, and hands are covered at all times.")            
        
    def test_suggest_clothing__0(self):
        self.assertEquals(Clothing.suggest_clothing(0),"The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        
    def test_suggest_clothing__0_9(self):
        self.assertEquals(Clothing.suggest_clothing(1),"The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        
    def test_suggest_clothing__9(self):
        self.assertEquals(Clothing.suggest_clothing(9),"The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
    
    def test_suggest_clothing__10(self):
        self.assertEquals(Clothing.suggest_clothing(10),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing__between_10_32(self):
        self.assertEquals(Clothing.suggest_clothing(11),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing__32(self):
        self.assertEquals(Clothing.suggest_clothing(32),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing__33(self):
        self.assertEquals(Wellness.suggest_clothing(33),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
    
    def test_suggest_clothing__between_33_55(self):
        self.assertEquals(Clothing.suggest_clothing(34),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
    
    def test_suggest_clothing__55(self):
        self.assertEquals(Clothing.suggest_clothing(55),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
    
    def test_suggest_clothing__56(self):
        self.assertEquals(Clothing.suggest_clothing(56),"The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
    
    def test_suggest_clothing__between_56_69(self):
        self.assertEquals(Clothing.suggest_clothing(57),"The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
    
    def test_suggest_clothing__69(self):
        self.assertEquals(Clothing.suggest_clothing(69),"The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
    
    def test_suggest_clothing__70(self):
        self.assertEquals(Clothing.suggest_clothing(70),"The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
    
    def test_suggest_clothing__between_70_84(self):
        self.assertEquals(Clothing.suggest_clothing(71),"The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
    
    def test_suggest_clothing__84(self):
        self.assertEquals(Clothing.suggest_clothing(84),"The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
    
    def test_suggest_clothing__greater_84(self):
        self.assertEquals(Clothing.suggest_clothing(85),"It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes.")
    
    def test_suggest_clothing__greater_85(self):
        self.assertEquals(Clothing.suggest_clothing(90),"It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes.")
    

    
    def test_suggest_activities_sunny(self):
        self.assertEqual(Activites.suggest_activities("sunny"),"Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
    
    def test_suggest_activities_not_sunny(self):
        self.assertNotEqual(Activites.suggest_activities("rainy"),"Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
    
    def test_suggest_activities_cloudy(self):
        self.assertEqual(Activites.suggest_activities("cloudy"),"It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
    
    def test_suggest_activities_not_cloudy(self):
        self.assertNotEqual(Activites.suggest_activities("sunny"),"It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
    
    def test_suggest_activities_partly_sunny(self):
        self.assertEqual(Activites.suggest_activities("partly sunny"), "It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo.")
    
    def test_suggest_activities_not_partly_sunny(self):
        self.assertNotEqual(Activites.suggest_activities("snowy"),"It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo.")
    
    def test_suggest_activities_rainy(self):
        self.assertEqual(Activites.suggest_activities("rainy"),"It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
    
    def test_suggest_activities_not_rainy(self):
        self.assertNotEqual(Activites.suggest_activities("partly sunny"),"It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
    
    def test_suggest_activities_windy(self):
        self.assertEqual(Activites.suggest_activities("windy"),"Look out it's windy today! You could go to the mall, do some chores inside, or try flying a kite.")
    
    def test_suggest_activities_not_windy(self):
        self.assertNotEqual(Activites.suggest_activities("snowy"),"Look out it's windy today! You could go to the mall, do some chores inside, or try flying a kite.")
    
    def test_suggest_activities_snowy(self):
        self.assertEqual(Activites.suggest_activities("snowy"),"It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
    
    def test_suggest_activities_not_snowy(self):
        self.assertNotEqual(Activites.suggest_activities("thunderstorms"),"It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
    
    def test_suggest_activities_thunderstorms(self):
        self.assertEqual(Activites.suggest_activities("thunderstorms"),"Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie.")
    
    def test_suggest_activities_not_thunderstorms(self):
        self.assertNotEqual(Activites.suggest_activities("sunny"),"Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie.")
    
    def test_suggest_activities_not_valid(self):
        self.assertEqual(Activites.suggest_activities("partly cloudy"),"Weather condition not recognized. Check the forecast for more information.")

    
    def test_driving_techniques_snow(self):
        out = (
        "Tips for driving in the snow:"
        "- Slow down and reduce your speed."
        "- Increase your following distance."
        "- Drive in the tire tracks of other vehicles if possible."
        "- Avoid sudden steering or braking to prevent loss of control."
        "- Keep headlights on for better visibility."
    )
        self.assertEqual(Driving.driving_techniques("snow"), out)

    def test_driving_techniques_ice(self):
        out = (
        "Tips for driving in icy conditions: "
        "- Drive at a much slower speed."
        "- Avoid using cruise control."
        "- Brake gently and avoid sudden movements that could cause skidding."
        "- Increase following distance significantly."
        "- Stay in your lane and avoid abrupt steering."
        )
        self.assertEqual(Driving.driving_techniques("ice"), out)
    
    def test_driving_techniques_wind(self):
        out = (
        "Tips for driving in windy conditions: "
        "- Grip the steering wheel firmly and use both hands."
        "- Be aware of large gusts of wind that could move the car."
        "- Stay cautious around large vehicles like trucks and buses."
        "- Keep a larger distance from other vehicles to avoid being pushed by wind."
        )
        self.assertEqual(Driving.driving_techniques("wind"), out)
    
    def test_driving_techniques_rain(self):
        out = (
        "Tips for driving in the rain: "
        "- Slow down and reduce speed to avoid slipping."
        "- Increase your following distance to give yourself more stopping time."
        "- Use your headlights and windshield wipers for better visibility."
        "- Avoid driving through large puddles or flooded areas."
        "- Turn off cruise control to maintain full control of your vehicle."
        )
        self.assertEqual(Driving.driving_techniques("rain"), out)
    
    def test_driving_techniques_thunderstorms(self):
        out = (
        "Tips for driving in a thunderstorm: "
        "- Use your headlights and windshield wipers to maximize visibility."
        "- Avoid driving through flooded areas to prevent hydroplaning."
        "- Be aware of sudden gusts of wind and potential debris on the road."
        "-If conditions are severe pull over in a covered area to let the storm pass."
        )
        self.assertEqual(Driving.driving_techniques("thunderstorms"), out)
    
    def test_driving_techniques_not_vaild_partly_cloudy(self):
        self.assertEquals(Driving.driving_techniques("partly cloudy"), "Weather condition not recognized. Please enter a valid condition (snow, ice, wind, rain, or thunderstorm).")
    
    def test_driving_techniques_not_vaild_sunny(self):
        self.assertEquals(Driving.driving_techniques("sunny"), "Weather condition not recognized. Please enter a valid condition (snow, ice, wind, rain, or thunderstorm).") 
                            
    
    
    def test_mood_weather_sunny(self):
        self.assertEqual(Mood_Weather.mood_weather("sunny"),"The sun is shining out! Take advantage of this beautiful sunshine and soak up some vitamin D (not too much though, wear your sunscreen).") 
    
    def test_mood_weather_not_sunny(self):
        self.assertNotEqual(Mood_Weather.mood_weather("rainy"),"The sun is shining out! Take advantage of this beautiful sunshine and soak up some vitamin D (not too much though, wear your sunscreen).")    
    
    def test_mood_weather_cloudy(self):
        self.assertEqual(Mood_Weather.mood_weather("cloudy"),"There is no sun today. You might be feeling a little down today, but don't let that stop you from having a great day.")
    
    def test_mood_weather_not_cloudy(self):
        self.assertNotEqual(Mood_Weather.mood_weather("sunny"),"There is no sun today. You might be feeling a little down today, but don't let that stop you from having a great day.")    
    
    def test_mood_weather_rainy(self):
        self.assertEqual(Mood_Weather.mood_weather("rainy"),"It's a rainy one today. Try to keep your spirits high even though today might seem dreary.")
    
    def test_mood_weather_not_rainy(self):
        self.assertNotEqual(Mood_Weather.mood_weather("snowy"),"It's a rainy one today. Try to keep your spirits high even though today might seem dreary.")    
    
    def test_mood_weather_snow(self):
        self.assertEqual(Mood_Weather.mood_weather("snowy"),"It's snowing outside. Snow can really bring down our mood sometimes, so it is important to take care of yourself today.")
    
    def test_mood_weather_not_snowy(self):
        self.assertNotEqual(Mood_Weather.mood_weather("rainy"),"It's snowing outside. Snow can really bring down our mood sometimes, so it is important to take care of yourself today.")   
    
    def test_mood_weather_thunderstorms(self):
        self.assertEqual(Mood_Weather.mood_weather("thunderstorms"),"It's storming out. If you're up for it, watch the storms roll through. Otherwise, take care of yourself because sunny days are inevitable.")
    
    def test_mood_weather_not_thunderstorms(self):
        self.assertNotEqual(Mood_Weather.mood_weather("sunny"),"It's storming out. If you're up for it, watch the storms roll through. Otherwise, take care of yourself because sunny days are inevitable.")   
    
    def test_mood_weather_not_valid_partly_sunny(self):
        self.assertEqual(Mood_Weather.mood_weather("partly sunny"),"Weather condition not recognized. Please enter a valid condition (sunny, cloudy, snowy, rain, or thunderstorm).")
    
    def test_mood_weather_not_valid_ice(self):
        self.assertEqual(Mood_Weather.mood_weather("ice"),"Weather condition not recognized. Please enter a valid condition (sunny, cloudy, snowy, rain, or thunderstorm).")

    def test_mood_forecast(self):
        pass