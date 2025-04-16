import unittest
from WeatherCodeTranslations import WeatherCodeTranslations 
from Weather import Weather 
from Wellness import Wellness
import unittest
from Weather import Weather
from WeatherCodeTranslations import WeatherCodeTranslations

import unittest

class TestWeatherCodeTranslations(unittest.TestCase):

    def setUp(self):
        self.weatherCodeTranslations = WeatherCodeTranslations()

    def test_conditions_0_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(0.0), "Clear")

    def test_conditions_1_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(1.0), "Partly Cloudy")

    def test_conditions_2_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(2.0), "Mos")

    def test_conditions_3_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(3.0), "Cloudy")

    def test_conditions_5_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(5.0), "Haze")

    def test_conditions_10_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(10.0), "Mist")

    def test_conditions_11_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(11.0), "Fog")

    def test_conditions_12_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(12.0), "Fog")

    def test_conditions_13_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(13.0), "Lightning")

    def test_conditions_19_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(19.0), "Funnel Cloud Formation: Take Shelter")

    def test_conditions_20_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(20.0), "Rain")

    def test_conditions_21_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(21.0), "Rain")

    def test_conditions_22(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(22), "Snow")

    def test_conditions_23_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(23.0), "Wintery Mix")

    def test_conditions_24_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(24.0), "Freezing Rain")

    def test_conditions_25_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(25.0), "Rain Showers")

    def test_conditions_26_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(26.0), "Snow Showers")

    def test_conditions_27_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(27.0), "Hail")

    def test_conditions_28_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(28.0), "Fog")

    def test_conditions_29_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(29.0), "Thunderstorm")

    def test_conditions_36_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(36.0), "Drifting Snow")

    def test_conditions_38_5(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(38.5), "Drifting Snow")

    def test_conditions_39_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(39.0), "Drifting Snow")

    def test_conditions_40_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(40.0), "Fog")

    def test_conditions_45_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(45.0), "Fog")

    def test_conditions_49_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(49.0), "Fog")

    def test_conditions_50_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(50.0), "Rain")

    def test_conditions_55_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(55.0), "Rain")

    def test_conditions_59_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(59.0), "Rain")

    def test_conditions_60_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(60.0), "Rain")

    def test_conditions_65_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(65.0), "Rain")

    def test_conditions_66_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(66.0), "Freezing Rain")

    def test_conditions_67_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(67.0), "Freezing Rain")

    def test_conditions_68_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(68.0), "Rain")

    def test_conditions_69_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(69.0), "Rain")

    def test_conditions_70_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(70.0), "Snow")

    def test_conditions_75_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(75.0), "Snow")

    def test_conditions_80_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(80.0), "Light Rain")

    def test_conditions_81_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(81.0), "Rain")

    def test_conditions_82_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(82.0), "Heavy Rain")

    def test_conditions_83_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(83.0), "Light Wintery Mix")

    def test_conditions_84_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(84.0), "Heavy Wintery Mix")

    def test_conditions_85_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(85.0), "Wintery Mix")

    def test_conditions_86_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(86.0), "Heavy Snow")

    def test_conditions_87_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(87.0), "Light Small Hail")

    def test_conditions_88_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(88.0), "Heavy Small Hail")

    def test_conditions_89_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(89.0), "Light Hail")

    def test_conditions_90_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(90.0), "Heavy Hail")

    def test_conditions_91_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(91.0), "Light Rain")

    def test_conditions_92_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(92.0), "Heavy Rain")

    def test_conditions_93_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(93.0), "Light Snow")

    def test_conditions_94_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(94.0), "Heavy Snow")

    def test_conditions_95_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(95.0), "Thunderstorm and Hail")

    def test_conditions_96_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(96.0), "Heavy Thunderstorm and Hail")

    def test_conditions_97_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(97.0), "Thunderstorm")

    def test_conditions_99_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(99.0), "Heavy Thunderstorm and Hail")

    def test_conditions_6_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(6.0), "Not in Current Database")

    def test_conditions_100_0(self):
        self.assertEqual(self.weatherCodeTranslations.GetConditions(100.0), "Not in Current Database")

    def test_code_1_day(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(1, True), "Partly Cloudy")

    def test_code_1_night(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(1, False), "Partly Cloudy Night")

    def test_code_3(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(3, True), "Cloudy")

    def test_code_0_day(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(0, True), "Sunny")

    def test_code_0_night(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(0, False), "Clear")

    def test_code_20(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(20, True), "Rain")

    def test_code_21(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(21, True), "Rain")

    def test_code_25(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(25, True), "Rain")

    def test_code_60(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(60, True), "Rain")

    def test_code_65(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(65, True), "Rain")

    def test_code_68(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(68, True), "Rain")

    def test_code_80(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(80, True), "Rain")

    def test_code_82(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(82, True), "Rain")

    def test_code_91(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(91, True), "Rain")

    def test_code_92(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(92, True), "Rain")

    def test_code_14(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(14, True), "Rain")

    def test_code_16(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(16, True), "Rain")

    def test_code_51(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(51, True), "Rain")

    def test_code_53(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(53, True), "Rain")

    def test_code_5(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(5, True), "Haze")

    def test_code_11(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(11, True), "Fog")

    def test_code_12(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(12, True), "Fog")

    def test_code_28(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(28, True), "Fog")

    def test_code_40(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(40, True), "Fog")

    def test_code_49(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(49, True), "Fog")

    def test_code_13(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(13, True), "Thunderstorm")

    def test_code_17(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(17, True), "Thunderstorm")

    def test_code_19(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(19, True), "Thunderstorm")

    def test_code_29(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(29, True), "Thunderstorm")

    def test_code_95(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(95, True), "Thunderstorm")

    def test_code_99(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(99, True), "Thunderstorm")

    def test_code_22(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(22, True), "Snow")

    def test_code_23(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(23, True), "Snow")

    def test_code_26(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(26, True), "Snow")

    def test_code_70(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(70, True), "Snow")

    def test_code_79(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(79, True), "Snow")

    def test_code_86(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(86, True), "Snow")

    def test_code_88(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(88, True), "Snow")

    def test_code_93(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(93, True), "Snow")

    def test_code_94(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(94, True), "Snow")

    def test_code_85(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(85, True), "Wintery Mix")

    def test_code_not_in_database(self):
        self.assertEqual(self.weatherCodeTranslations.GetCategory(999, True), "Not in Current Database")

class TestWellness(unittest.TestCase):

    def setUp(self):
        self.wellness = Wellness()

    def test_suggest_clothing_negative_temp(self):
        self.assertEqual(self.wellness.suggest_clothing(-5), "Temperature is in the negatives today. Avoid going outside, but if necessary, dress in heavy layers and make sure your ears, nose, and hands are covered at all times.")

    def test_suggest_clothing_single_digits(self):
        self.assertEqual(self.wellness.suggest_clothing(5), "The temperature is in the single digits. When outside keep your ears, nose, and hands covered. Wear heavy winter clothing, including a thick coat, gloves, hat, scarf, and boots.")
    
    def test_suggest_clothing_cold(self):
        self.assertEqual(self.wellness.suggest_clothing(15), "It's cold but not in the single digits yet. Wear a winter coat, gloves, and a hat.")
    
    def test_suggest_clothing_chilly(self):
        self.assertEqual(self.wellness.suggest_clothing(45), "The temperature is chilly. Wear layers, like a jacket or sweater, long pants, and close toed shoes.")
    
    def test_suggest_clothing_moderate(self):
        self.assertEqual(self.wellness.suggest_clothing(60), "The temperature is moderate. Pair a light jacket or longsleeves with pants. Otherwise a sweatshirt or thick jacket with shorts. Wear closed toed shoes.")
    
    def test_suggest_clothing_hot(self):
        self.assertEqual(self.wellness.suggest_clothing(80), "The temperature is hot. Wear a tee shirt or tank top, shorts and sandals or tennis shoes. If it sunny think about adding sunglasses or a hat.")
    
    def test_suggest_clothing_very_hot(self):
        self.assertEqual(self.wellness.suggest_clothing(95), "It's very hot outside! Wear lightweight flowy clothing, a hat and sandals or tennis shoes.")

    def test_suggest_activities_sunny(self):
        self.assertEqual(self.wellness.suggest_activities("Sunny"), "Hooray it's sunny outside! Walking, hiking, biking, going to the beach, or having a picnic in the park are great to do on sunny days like this one.")
    
    def test_suggest_activities_cloudy(self):
        self.assertEqual(self.wellness.suggest_activities("Cloudy"), "It’s cloudy outside today. Going to a café, visting a muesuem or running some errands are some things to do on cloudy days like this one.")
    
    def test_suggest_activities_partly_sunny(self):
        self.assertEqual(self.wellness.suggest_activities("Partly Sunny"), "It is partly sunny today. Take a walk, do some yard work or take a trip to the zoo.")
    
    def test_suggest_activities_rain(self):
        self.assertEqual(self.wellness.suggest_activities("Rain"), "It's rainy out. Some indoor activities to do are reading, watching movies, cooking, or doing a puzzle. ")
    
    def test_suggest_activities_snow(self):
        self.assertEqual(self.wellness.suggest_activities("Snow"), "It's snowing today. You could brave the snow and go sledding, snowboarding, or skiing. Otherwise, stay inside build a fire, play board games, watch movies or read a book.")
    
    def test_suggest_activities_thunderstorm(self):
        self.assertEqual(self.wellness.suggest_activities("Thunderstorm"), "Uh oh, it's thunderstorming! Stay inside and do a puzzle, try at home yoga, or watch a movie.")
    
    def test_suggest_activities_unknown(self):
        self.assertEqual(self.wellness.suggest_activities("Unknown"), "Weather condition not recognized. Check the forecast for more information.")
    
    def test_driving_techniques_snow(self):
        self.assertEqual(self.wellness.driving_techniques("snow"), "Tips for driving in the snow: ")

    def test_driving_techniques_rain(self):
        self.assertEqual(self.wellness.driving_techniques("rain"), "Tips for driving in the rain: ")

    def test_driving_techniques_thunderstorm(self):
        self.assertEqual(self.wellness.driving_techniques("thunderstorm"), "Tips for driving in a thunderstorm: ")

    def test_driving_techniques_clear(self):
        self.assertEqual(self.wellness.driving_techniques("clear"), "Driving Conditions Safe.")
    
    def test_mood_weather_sunny(self):
        self.assertEqual(self.wellness.mood_weather("Sunny"), "The sun is shining out! Take advantage of this beautiful sunshine and soak up some vitamin D (not too much though, wear your sunscreen).")
    
    def test_mood_weather_clear(self):
        self.assertEqual(self.wellness.mood_weather("Clear"), "The moon is out and the sky is dark! You might start to feel tired, so prioritize getting some sleep, but also enjoy some of the feelings of nighttime activities.")
    
    def test_mood_weather_cloudy(self):
        self.assertEqual(self.wellness.mood_weather("Cloudy"), "There is no sun today. You might be feeling a little down today, but don't let that stop you from having a great day.")
    
    def test_mood_weather_rainy(self):
        self.assertEqual(self.wellness.mood_weather("Rainy"), "It's a rainy one today. Try to keep your spirits high even though today might seem dreary.")
    
    def test_mood_weather_thunderstorm(self):
        self.assertEqual(self.wellness.mood_weather("Thunderstorm"), "It's storming out. If you're up for it, watch the storms roll through. Otherwise, take care of yourself because sunny days are inevitable.")
    
    def test_mood_weather_snowy(self):
        self.assertEqual(self.wellness.mood_weather("Snowy"), "It's snowing outside. Snow can really bring down our mood sometimes, so it is important to take care of yourself today.")
    
    def test_mood_weather_unknown(self):
        self.assertEqual(self.wellness.mood_weather("Unknown"), "Weather condition not recognized. Please enter a valid condition (sunny, cloudy, snowy, rain, or thunderstorm).")

if __name__ == '__main__':
    unittest.main()

