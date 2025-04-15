import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Wellness

class TestWeatherCodeTranslations(unittest.TestCase):

    def __init__(self):
        self.wellness = Wellness()
        self.weatherTranslations = WeatherCodeTranslations()

    def test_get_conditions(self):
        self.assertEqual(self.weatherTranslations.GetConditions(0), "Clear")
        self.assertEqual(self.weatherTranslations.GetConditions(6), "Not in Current Database")
        self.assertEqual(self.weatherTranslations.GetConditions(11), "Fog")
        self.assertEqual(self.weatherTranslations.GetConditions(22), "Snow")
        self.assertEqual(self.weatherTranslations.GetConditions(81), "Rain")
        self.assertEqual(self.weatherTranslations.GetConditions(85), "Light Snow")
        self.assertEqual(self.weatherTranslations.GetConditions(97), "Thunderstorm")
    
    def test_get_category(self):
        self.assertEqual(self.weatherTranslations.GetCategory(3, True), "Cloudy")
        self.assertEqual(self.weatherTranslations.GetCategory(0, True), "Sunny") 
        self.assertEqual(self.weatherTranslations.GetCategory(81, False), "Rain")    
        self.assertEqual(self.weatherTranslations.GetCategory(5, True), "Haze")  
        self.assertEqual(self.weatherTranslations.GetCategory(43, True), "Fog")
        self.assertEqual(self.weatherTranslations.GetCategory(3, False), "Cloudy")
        self.assertEqual(self.weatherTranslations.GetCategory(29, False), "Thunderstorm")
        self.assertEqual(self.weatherTranslations.GetCategory(26, True), "Snow")
        self.assertEqual(self.weatherTranslations.GetCategory(100, False), "Not in Current Database")

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

    