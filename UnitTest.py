import unittest
import WeatherCodeTranslations from WeatherCodeTranslations
import Weather from Weather
import Wellness from Wellness

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
        self.assertEqual(WeatherCodeTranslations.getCategory(3), "Cloudy")
        self.assertEqual(WeatherCodeTranslations.getCategory(0), "Clear") 
        self.assertEqual(WeatherCodeTranslations.getCategory(81), "Rain")    
        self.assertEqual(WeatherCodeTranslations.getCategory(5), "Haze")  
        self.assertEqual(WeatherCodeTranslations.getCategory(43), "Fog")
        self.assertEqual(WeatherCodeTranslations.getCategory(3), "Cloudy")
        self.assertEqual(WeatherCodeTranslations.getCategory(29), "Thunderstorm")
        self.assertEqual(WeatherCodeTranslations.getCategory(26), "Snow")
        self.assertEqual(WeatherCodeTranslations.getCategory(100), "Not in Current Database")

class TestWeather(unittest.TestCase):
    def test_forcast_daily(self):
            pass
    def test_forecast_hourly(self):
            pass
    def test_view_current_weather(self):
            pass
    def test_set_current_location(self):
            pass

class TestWellness(unittest.TestCase):
    def test_suggest_clothing(self, temp):
            pass
    def test_below_zero(self, temp):
            pass
    def test_at_zero(self, temp):
            pass
    def test_above_zero_less_nine(self, temp);
            pass
    def test_at_nine(self, temp):
            pass
    def test_at_9(self,temp);
            pass
    def test_between_ten_and32(self, temp):
            pass
    def exactly_at_33(self, temp):
            pass
    def temp_between_70_84(self, temp):
            pass
    def test_greater_84(self,temp):
            pass
    def test_negative_test(self,temp):
            pass

    def test_suggest_activities(self,weather_conditions):
        weather_condition = "sunny"
        self.assertEqual(Wellness.suggest_activities(weather_condition),"Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
    def test_suggest_activities_not_sunny(self,weather_conditions):
        weather_condition != "sunny"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
    def test_suggest_activities_cloudy(self,weather_conditions):
        weather_condition = "cloudy"
        self.assertEqual(Wellness.suggest_activities(weather_condition),"It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
    def test_suggest_activities_not_cloudy(self,weather_conditions):
        weather_condition != "cloudy"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
    def test_suggest_activities_partly_sunny(self,weather_conditions):
        weather_condition = "partly sunny"
        self.assertEqual(Wellness.suggest_activities(weather_condition), "It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo.")
    def test_suggest_activities_not_partly_sunny(self,weather_conditions):
        weather_condition != "partly sunny"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo.")
    def test_suggest_activities_rainy(self,weather_conditions):
        weather_condition = "rainy"
        self.assertEqual(Wellness.suggest_activities(weather_condition),"It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
    def test_suggest_activities_not_rainy(self,weather_conditions):
        weather_condition != "rainy"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
    def test_suggest_activities_windy(self,weather_conditions):
        weather_condition = "windy"
        self.assertEqual(Wellness.suggest_activities(weather_condition),"Look out it's windy today! You could go to the mall, do some chores inside, or try flying a kite.")
    def test_suggest_activities_not_windy(self,weather_conditions):
        weather_condition != "windy"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"Look out it's windy today! You could go to the mall, do some chores inside, or try flying a kite.")
    def test_suggest_activities_snowy(self,weather_conditions):
        weather_condition = "snowy"
        self.assertEqual(Wellness.suggest_activities(weather_condition),"It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
    def test_suggest_activities_not_snowy(self,weather_conditions):
        weather_condition != "snowy"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
    def test_suggest_activities_thunderstorms(self,weather_conditions):
        weather_condition = "thunderstorms"
        self.assertEqual(Wellness.suggest_activities(weather_condition),"Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie.")
    def test_suggest_activities_not_thunderstorms(self,weather_conditions):
        weather_condition != "thunderstorms"
        self.assertNotEqual(Wellness.suggest_activities(weather_condition),"Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie.")
    def test_suggest_activities_not_valid(self,weather_conditions):
        if weather_condition not in ["sunny", "cloudy", "rainy", "partly sunny", "snowy", "thunderstorms"]:
            self.assertEqual(Wellness.suggest_activities(weather_condition),"Weather condition not recognized. Check the forecast for more information.")

    def test_driving_techniques(self,weather_conditions):
            pass
    def test_mood_weather(self):
            pass #comment for test 