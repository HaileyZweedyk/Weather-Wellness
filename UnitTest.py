import unittest
import Weather from Weather
import Wellness from Wellness

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
    def test_suggest_clothing(self, temp):
        pass
    def test_suggest_activities(self,weather_conditions):
        pass
    def test_driving_techniques(self,weather_conditions):
        pass
    def test_mood_weather(self):
        pass