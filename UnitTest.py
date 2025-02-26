import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Wellness 

class TestWeatherCodeTranslations(unittest.TestCase):
    def test_get_conditions(self):
            pass
    def test_get_category(self):
            pass

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
        def test_negative(self):
              self.assertEqual(Wellness.suggest_clothing(-1),"Temperature is in the negatives today. Avoid going outside, but if necessary, dress in heavy layers and make sure your ears, nose, and hands are covered at all times.")            
        def temp_0(self):
              self.assertEquals(Wellness.suggest_clothing(0),"The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        def temp_0_9(self):
              self.assertEquals(Wellness.suggest_clothing(1),"The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        def temp_9(self):
              self.assertEquals(Wellness.suggest_clothing(9),"The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
        def temp_10(self):
              self.assertEquals(Wellness.suggest_clothing(10),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
        def temp_between_10_32(self):
              self.assertEquals(Wellness.suggest_clothing(11),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
        def temp_32(self):
              self.assertEquals(Wellness.suggest_clothing(32),"It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
        def temp_33(self):
              self.assertEquals(Wellness.suggest_clothing(33),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
        def temp_between_33_55(self):
              self.assertEquals(Wellness.suggest_clothing(34),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
        def temp_55(self):
              self.assertEquals(Wellness.suggest_clothing(55),"The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
        def temp_56(self):
              self.assertEquals(Wellness.suggest_clothing(56),"The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
        def temp_between_56_69(self):
              self.assertEquals(Wellness.suggest_clothing(57),"The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
        def temp_69(self):
              self.assertEquals(Wellness.suggest_clothing(69),"The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
        def temp_70(self):
              self.assertEquals(Wellness.suggest_clothing(70),"The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
        def temp_between_70_84(self):
              self.assertEquals(Wellness.suggest_clothing(71),"The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
        def temp_84(self):
              self.assertEquals(Wellness.suggest_clothing(84),"The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
        def temp_greater_84(self):
              self.assertEquals(Wellness.suggest_clothing(85),"It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes.")
        def temp_greater_85(self):
              self.assertEquals(Wellness.suggest_clothing(90),"It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes.")
        

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
        s   elf.assertEqual(Wellness.suggest_activities(weather_condition),"It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
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

        def test_driving_techniques(self):
            pass
        def test_mood_weather(self):
            pass #comment for test 