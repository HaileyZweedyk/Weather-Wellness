from Weather import Weather

class WeatherCodeTranslations:

    def __init__(self):
        pass

    
    def GetConditions(self, CurrWeatherCode):

        conditionText = ""

            
        if CurrWeatherCode == 0.0:
            conditionText = "Clear"
        elif CurrWeatherCode == 1.0:
            conditionText = "Clouds Dissapating"
        elif CurrWeatherCode == 2.0:
            conditionText = "Conditions Remain Same"
        elif CurrWeatherCode == 3.0:
            conditionText = "Clouds Developing"
        elif CurrWeatherCode == 5.0:
            conditionText = "Haze"
        elif CurrWeatherCode == 10.0:
            conditionText = "Mist"
        elif CurrWeatherCode == 11.0:
            conditionText = "Fog"
        elif CurrWeatherCode == 12.0:
            conditionText = "Fog"
        elif CurrWeatherCode == 13.0:
            conditionText = "Lightning"
        elif CurrWeatherCode == 19.0:
            conditionText = "Funnel Cloud Formation: Take Shelter"
        elif CurrWeatherCode == 20.0:
            conditionText = "Drizzle"
        elif CurrWeatherCode == 21.0:
            conditionText = "Rain"
        elif CurrWeatherCode == 22:
            conditionText = "Snow"
        elif CurrWeatherCode == 23.0:
            conditionText = "Wintery Mix"
        elif CurrWeatherCode == 24.0:
            conditionText = "Freezing Rain"
        elif CurrWeatherCode == 25.0:
            conditionText = "Rain Showers"
        elif CurrWeatherCode == 26.0:
            conditionText = "Snow Showers"
        elif CurrWeatherCode == 27.0:
            conditionText = "Hail"
        elif CurrWeatherCode == 28.0:
            conditionText = "Fog"
        elif CurrWeatherCode == 29.0:
            conditionText = "Thunderstorm"
        elif CurrWeatherCode == 80.0: 
            conditionText = "Light Rain"
        elif CurrWeatherCode == 81.0:
            conditionText = "Rain"
        elif CurrWeatherCode == 82.0:
            conditionText = "Heavy Rain"
        elif CurrWeatherCode == 83.0:
            conditionText = "Light Wintery Mix"
        elif CurrWeatherCode == 84.0:
            conditionText = "Heavy Wintery Mix"
        elif CurrWeatherCode == 85.0:
            conditionText = "Light Snow"
        elif CurrWeatherCode == 86.0:
            conditionText = "Heavy Snow"
        elif CurrWeatherCode == 87.0:
            conditionText = "Light Small Hail"
        elif CurrWeatherCode == 88.0:
            conditionText = "Heavy Small Hail"
        elif CurrWeatherCode == 89.0:
            conditionText = "Light Hail"
        elif CurrWeatherCode == 90.0:
            conditionText = "Heavy Hail"
        elif CurrWeatherCode == 91.0:
            conditionText = "Light Rain"
        elif CurrWeatherCode == 92.0:
            conditionText = "Heavy Rain"
        elif CurrWeatherCode == 93.0:
            conditionText = "Light Snow"
        elif CurrWeatherCode == 94.0:
            conditionText = "Heavy Snow"
        elif CurrWeatherCode == 95.0:
            conditionText = "Thunderstorm and Hail"
        elif CurrWeatherCode == 96.0:
            conditionText = "Heavy Thunderstorm and Hail"
        elif CurrWeatherCode == 97.0:
            conditionText = "Thunderstorm"
        elif CurrWeatherCode == 99.0:
            conditionText = "Heavy Thunderstorm and Hail"

        
        elif 36.0 <= CurrWeatherCode <= 39.0:
            conditionText = "Drifting Snow"
        elif 40.0 <= CurrWeatherCode <= 49.0:
            conditionText = "Fog"
        elif 50.0 <= CurrWeatherCode <= 59.0:
            conditionText = "Drizzle"
        elif 60.0 <= CurrWeatherCode <= 65.0 or 68.0 <= CurrWeatherCode <= 69.0:
            conditionText = "Rain"
        elif 65.0 <= CurrWeatherCode <= 67.0:
            conditionText = "Freezing Rain"
        elif 70.0 <= CurrWeatherCode <= 75.0:
            conditionText = "Snow"
        else:
            conditionText = "Not in Current Database"

        return conditionText
    

    def GetCategory(CurrWeatherCode, isDay):

        # Will return simplified categories for Wellness

        conditionCat = ""
        curr = CurrWeatherCode

        if curr == 3 or curr == 1:
            conditionCat = "Cloudy"
        elif curr == 0:
            if isDay:
                conditionCat = "Sunny"
            else:
                conditionCat = "Clear"
        elif 20 <= curr <= 21 or curr == 25 or 60 <= curr <= 65 or 80 <= curr <= 82 or 91 <= curr <= 92 or 14 <= curr <= 16:
            conditionCat = "Rain"
        elif curr == 5:
            conditionCat = "Haze"
        elif 11 <= curr <= 12 or curr == 28 or 40 <= curr <= 49:
            conditionCat = "Fog"
        elif curr == 13 or curr == 17 or curr == 19 or curr == 29 or 95 <= curr <= 99:
            conditionCat = "Thunderstorm"
        elif curr == 20 or 22 <= curr <= 23 or curr == 26 or 70 <= curr <= 79 or 85 <= curr <= 88 or 93 <= curr <= 94:
            conditionCat = "Snow"
        else:
            conditionCat = "Not in Current Database"

        return conditionCat
    


