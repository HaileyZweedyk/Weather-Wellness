import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Wellness

class TestWeatherCodeTranslations(unittest.TestCase):

    def __init__(self):
        self.wellness = Wellness()
        self.weatherTranslations = WeatherCodeTranslations()

import unittest
from Weather import Weather
from WeatherCodeTranslations import WeatherCodeTranslations

class TestWeatherCodeTranslations(unittest.TestCase):

    def setUp(self):
        self.weatherCodeTranslations = WeatherCodeTranslations()

    def test_get_conditions(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(0.0), "Clear")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(1.0), "Partly Cloudy")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(2.0), "Conditions Remain Same")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(3.0), "Cloudy")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(5.0), "Haze")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(10.0), "Mist")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(11.0), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(12.0), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(13.0), "Lightning")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(19.0), "Funnel Cloud Formation: Take Shelter")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(20.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(21.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(22), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(23.0), "Wintery Mix")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(24.0), "Freezing Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(25.0), "Rain Showers")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(26.0), "Snow Showers")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(27.0), "Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(28.0), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(29.0), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(36.0), "Drifting Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(38.5), "Drifting Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(39.0), "Drifting Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(40.0), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(45.0), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(49.0), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(50.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(55.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(59.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(60.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(65.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(66.0), "Freezing Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(67.0), "Freezing Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(68.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(69.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(70.0), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(75.0), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(80.0), "Light Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(81.0), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(82.0), "Heavy Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(83.0), "Light Wintery Mix")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(84.0), "Heavy Wintery Mix")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(85.0), "Wintery Mix")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(86.0), "Heavy Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(87.0), "Light Small Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(88.0), "Heavy Small Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(89.0), "Light Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(90.0), "Heavy Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(91.0), "Light Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(92.0), "Heavy Rain")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(93.0), "Light Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(94.0), "Heavy Snow")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(95.0), "Thunderstorm and Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(96.0), "Heavy Thunderstorm and Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(97.0), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(99.0), "Heavy Thunderstorm and Hail")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(6.0), "Not in Current Database")
        self.assertEqual(self.weatherCodeTranslations.GetConditions(100.0), "Not in Current Database")

    def test_get_category(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(1, True), "Partly Cloudy")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(1, False), "Partly Cloudy Night")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(3, True), "Cloudy")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(0, True), "Sunny")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(0, False), "Clear")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(20, True), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(21, False), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(25, False), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(61, False), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(65, False), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(68, True), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(91, True), "Rain")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(5, False), "Haze")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(11, True), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(12, False), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(28, False), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(40, True), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(45, False), "Fog")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(13, True), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(17, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(19, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(29, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(95, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(96, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(97, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(99, False), "Thunderstorm")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(22, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(23, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(26, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(70, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(75, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(86, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(88, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(93, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(94, False), "Snow")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(85, False), "Wintery Mix")
        self.assertEqual(self.weatherCodeTranslations.GetCategory(100, False), "Not in Current Database")


class TestWellness(unittest.TestCase):
    def test_suggest_CLothing_negative(self):
        self.assertEqual(self.wellness.suggest_Wellness(-1),"Temperature is in the negatives today. Avoid going outside, but if necessary, dress in heavy layers and make sure your ears, nose, and hands are covered at all times.")            
        
    def test_suggest_clothing__0(self):
        self.assertEqual(self.wellness.suggest_clothing(0),"The temperature is in the single digits. When outside, keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        
    def test_suggest_clothing__0_9(self):
        self.assertEqual(self.wellness.suggest_clothing(1),"The temperature is in the single digits. When outside, keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        
    def test_suggest_clothing__9(self):
        self.assertEqual(self.wellness.suggest_clothing(9),"The temperature is in the single digits. When outside, keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
    
    def test_suggest_clothing__10(self):
        self.assertEqual(self.wellness.suggest_clothing(10),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing__between_10_32(self):
        self.assertEqual(self.wellness.suggest_clothing(11),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing__32(self):
        self.assertEqual(self.wellness.suggest_clothing(32),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing__33(self):
        self.assertEqual(self.wellness.suggest_clothing(33),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and closed-toe shoes.")
    
    def test_suggest_clothing__between_33_55(self):
        self.assertEqual(self.wellness.suggest_clothing(34),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and closed-toe shoes.")
    
    def test_suggest_clothing__55(self):
        self.assertEqual(self.wellness.suggest_clothing(55),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and closed-toe shoes.")
    
    def test_suggest_clothing__56(self):
        self.assertEqual(self.wellness.suggest_clothing(56),"The temperature is moderate. Pair a light jacket or long sleeves with pants. Otherwise, a sweatshirt or thick jacket with shorts. Wear closed-toe shoes.")
    
    def test_suggest_clothing__between_56_69(self):
        self.assertEqual(self.wellness.suggest_clothing(57),"The temperature is moderate. Pair a light jacket or long sleeves with pants. Otherwise, a sweatshirt or thick jacket with shorts. Wear closed-toe shoes.")
    
    def test_suggest_clothing__69(self):
        self.assertEqual(self.wellness.suggest_clothing(69),"The temperature is moderate. Pair a light jacket or long sleeves with pants. Otherwise, a sweatshirt or thick jacket with shorts. Wear closed-toe shoes.")
    
    def test_suggest_clothing__70(self):
        self.assertEqual(self.wellness.suggest_clothing(70),"The temperature is warm. Wear a T-shirt or tank top, shorts, and sandals or tennis shoes. If it’s sunny, consider adding sunglasses or a hat.")
    
    def test_suggest_clothing__between_70_84(self):
        self.assertEqual(self.wellness.suggest_clothing(71),"The temperature is warm. Wear a T-shirt or tank top, shorts, and sandals or tennis shoes. If it’s sunny, consider adding sunglasses or a hat.")
    
    def test_suggest_clothing__84(self):
        self.assertEqual(self.wellness.suggest_clothing(84),"The temperature is warm. Wear a T-shirt or tank top, shorts, and sandals or tennis shoes. If it’s sunny, consider adding sunglasses or a hat.")
    
    def test_suggest_clothing__greater_84(self):
        self.assertEqual(self.wellness.suggest_clothing(85),"It's very hot outside! Wear lightweight, flowy clothing, a hat, and sandals or tennis shoes.")
    
    def test_suggest_clothing__greater_85(self):
        self.assertEqual(self.wellness.suggest_clothing(90),"It's very hot outside! Wear lightweight, flowy clothing, a hat, and sandals or tennis shoes.")
    

    def test_suggest_activities_sunny(self):
        self.assertEqual(self.wellness.suggest_activities("Sunny"),"Walking, hiking, biking, going to the beach, or having a picnic.")
    
    def test_suggest_activities_not_sunny(self):
        self.assertNotEqual(self.wellness.suggest_activities("Rain"),"Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
    
    def test_suggest_activities_cloudy(self):
        self.assertEqual(self.wellness.suggest_activities("Cloudy"),"Visiting a café, museum, or running some errands.")
    
    def test_suggest_activities_not_cloudy(self):
        self.assertNotEqual(self.wellness.suggest_activities("Sunny"),"It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
    
    def test_suggest_activities_rainy(self):
        self.assertEqual(self.wellness.suggest_activities("Rain"),"Reading, watching movies, cooking, or doing a puzzle.")
    
    def test_suggest_activities_not_rainy(self):
        self.assertNotEqual(self.wellness.suggest_activities("Sunny"),"It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
    
    def test_suggest_activities_snowy(self):
        self.assertEqual(self.wellness.suggest_activities("Snow"),"Sledding, snowboarding, skiing, or staying inside with a book.")
    
    def test_suggest_activities_not_snowy(self):
        self.assertNotEqual(self.wellness.suggest_activities("Thunderstorm"),"Walking, hiking, biking, going to the beach, or having a picnic.")
    
    def test_suggest_activities_thunderstorms(self):
        self.assertEqual(self.wellness.suggest_activities("Thunderstorm"),"Staying inside and doing yoga, puzzles, or watching a movie.")
    
    def test_suggest_activities_not_thunderstorms(self):
        self.assertNotEqual(self.wellness.suggest_activities("Sunny"),"Staying inside and doing yoga, puzzles, or watching a movie.")
    
    def test_suggest_activities_not_valid(self):
        self.assertNotEqual(self.wellness.suggest_activities("Cloudy"),"Weather condition not recognized. Check the forecast for more information.")

    
    def test_driving_techniques_snow(self):
        out = (
        "- Slow down and increase your following distance.\n- Avoid sudden steering or braking.\n- Drive in the tire tracks of other vehicles."
        )
        self.assertEqual(self.wellness.driving_techniques("Snow"), out)

    def test_driving_techniques_ice(self):
        out = (
        "- Drive much slower.\n- Avoid cruise control.\n- Brake gently to avoid skidding."
        )
        self.assertEqual(self.wellness.driving_techniques("Ice"), out)
    
    def test_driving_techniques_wind(self):
        out = (
        "- Grip the steering wheel firmly.\n- Stay cautious around large vehicles.\n- Keep a larger distance from other vehicles."
        )
        self.assertEqual(self.wellness.driving_techniques("Wind"), out)
    
    def test_driving_techniques_rain(self):
        out = (
        "- Reduce speed to avoid slipping.\n- Increase following distance.\n- Use headlights and windshield wipers."
        )
        self.assertEqual(self.wellness.driving_techniques("Rain"), out)
    
    def test_driving_techniques_thunderstorms(self):
        out = (
        "- Use headlights and windshield wipers.\n- Avoid flooded areas.\n- If conditions are severe, pull over safely."
        )
        self.assertEqual(self.wellness.driving_techniques("Thunderstorm"), out)
    
    """def test_driving_techniques_not_vaild_partly_cloudy(self):
        self.assertEquals(Driving.driving_techniques("partly cloudy"), "Weather condition not recognized. Please enter a valid condition (snow, ice, wind, rain, or thunderstorm).")
    
    def test_driving_techniques_not_vaild_sunny(self):
        self.assertEquals(Driving.driving_techniques("sunny"), "Weather condition not recognized. Please enter a valid condition (snow, ice, wind, rain, or thunderstorm).") """
                            
    
    
    def test_mood_weather_sunny(self):
        self.assertEqual(self.wellness.mood_weather("Sunny"),"Take advantage of the sunshine and soak up some vitamin D (wear sunscreen).") 
    
    def test_mood_weather_not_sunny(self):
        self.assertNotEqual(self.wellness.mood_weather("Rain"),"The sun is shining out! Take advantage of this beautiful sunshine and soak up some vitamin D (not too much though, wear your sunscreen).")    
    
    def test_mood_weather_cloudy(self):
        self.assertEqual(self.wellness.mood_weather("Cloudy"),"It’s a cloudy day. Keep your spirits high and make the most of it.")
    
    def test_mood_weather_not_cloudy(self):
        self.assertNotEqual(self.wellness.mood_weather("Sunny"),"There is no sun today. You might be feeling a little down today, but don't let that stop you from having a great day.")    
    
    def test_mood_weather_rainy(self):
        self.assertEqual(self.wellness.mood_weather("Rain"),"Try to stay positive even though today might feel dreary.")
    
    def test_mood_weather_not_rainy(self):
        self.assertNotEqual(self.wellness.mood_weather("Snow"),"It's a rainy one today. Try to keep your spirits high even though today might seem dreary.")    
    
    def test_mood_weather_snow(self):
        self.assertEqual(self.wellness.mood_weather("Snow"),"Snow can be gloomy, but take care of yourself and make the day cozy.")
    
    def test_mood_weather_not_snowy(self):
        self.assertNotEqual(self.wellness.mood_weather("Rain"),"It's snowing outside. Snow can really bring down our mood sometimes, so it is important to take care of yourself today.")   
    
    def test_mood_weather_thunderstorms(self):
        self.assertEqual(self.wellness.mood_weather("Thunderstorm"),"Storms pass. Take care of yourself and relax indoors.")
    
    def test_mood_weather_not_thunderstorms(self):
        self.assertNotEqual(self.wellness.mood_weather("Sunny"),"It's storming out. If you're up for it, watch the storms roll through. Otherwise, take care of yourself because sunny days are inevitable.")   

    