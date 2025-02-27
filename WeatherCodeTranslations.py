from Weather import Weather

weather = Weather() 
lat, long = weather.SetCurrLoc() 
weatherDataCurr = weather.ViewCurrWeather(lat, long) 
CurrWeatherCode = weatherDataCurr["CurrWeatherCode"]
IsDay = weatherDataCurr["CurrIsDay"]

print(f"Debug: CurrWeatherCode = {CurrWeatherCode}")
class WeatherCodeTranslations:
    @staticmethod
    def GetConditions(CurrWeatherCode):

        conditionText = ""

        match(CurrWeatherCode):
            
            case "0.0":
                conditionText = "Clear"
            case "1.0":
                conditionText = "Clouds Dissapating"
            case "2.0":
                conditionText = "Conditions Remain Same"
            case "3.0":
                conditionText = "Clouds Developing"
            case "5.0":
                conditionText = "Haze"
            case "10.0":
                conditionText = "Mist"
            case "11.0":
                conditionText = "Fog"
            case "12.0":
                conditionText = "Fog"
            case "13.0":
                conditionText = "Lightning"
            case "19.0":
                conditionText = "Funnel Cloud Formation: Take Shelter"
            case "20.0":
                conditionText = "Drizzle"
            case "21.0":
                conditionText = "Rain"
            case "22":
                conditionText = "Snow"
            case "23.0":
                conditionText = "Wintery Mix"
            case "24.0":
                conditionText = "Freezing Rain"
            case "25.0":
                conditionText = "Rain Showers"
            case "26.0":
                conditionText = "Snow Showers"
            case "27.0":
                conditionText = "Hail"
            case "28.0":
                conditionText = "Fog"
            case "29.0":
                conditionText = "Thunderstorm"
            case "80.0": 
                conditionText = "Light Rain"
            case "81.0":
                conditionText = "Rain"
            case "82.0":
                conditionText = "Heavy Rain"
            case "83.0":
                conditionText = "Light Wintery Mix"
            case "84.0":
                conditionText = "Heavy Wintery Mix"
            case "85.0":
                conditionText = "Light Snow"
            case "86.0":
                conditionText = "Heavy Snow"
            case "87.0":
                conditionText = "Light Small Hail"
            case "88.0":
                conditionText = "Heavy Small Hail"
            case "89.0":
                conditionText = "Light Hail"
            case "90.0":
                conditionText = "Heavy Hail"
            case "91.0":
                conditionText = "Light Rain"
            case "92.0":
                conditionText = "Heavy Rain"
            case "93.0":
                conditionText = "Light Snow"
            case "94.0":
                conditionText = "Heavy Snow"
            case "95.0":
                conditionText = "Thunderstorm and Hail"
            case "96.0":
                conditionText = "Heavy Thunderstorm and Hail"
            case "97.0":
                conditionText = "Thunderstorm"
            case "99.0":
                conditionText = "Heavy Thunderstorm and Hail"

        
        if 36 <= CurrWeatherCode <= 39:
            conditionText = "Drifting Snow"
        elif 40 <= CurrWeatherCode <= 49:
            conditionText = "Fog"
        elif 50 <= CurrWeatherCode <= 59:
            conditionText = "Drizzle"
        elif 60 <= CurrWeatherCode <= 65 or 68 <= CurrWeatherCode <= 69:
            conditionText = "Rain"
        elif 65 <= CurrWeatherCode <= 67:
            conditionText = "Freezing Rain"
        elif 70 <= CurrWeatherCode <= 75:
            conditionText = "Snow"
        else:
            conditionText = "Not in Current Database"

        return conditionText
    

    def GetCategory(CurrWeatherCode):

        # Will return simplified categories for Wellness

        conditionCat = ""
        curr = CurrWeatherCode

        if curr == 3 or curr == 1:
            conditionCat = "Cloudy"
        elif curr == 0:
            conditionCat = "Clear"
            if IsDay:
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