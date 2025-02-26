from Weather import Weather

weather = Weather() 
lat, long = weather.SetCurrLoc() 
weatherDataCurr = weather.ViewCurrWeather(lat, long) 
CurrWeatherCode = weatherDataCurr["CurrWeatherCode"]


class WeatherCodeTranslations:

    def GetConditions():

        conditionText = ""

        match(CurrWeatherCode):
            
            case "0":
                conditionText = "Clear"
            case "1":
                conditionText = "Clouds Dissapating"
            case "2":
                conditionText = "Conditions Remain Same"
            case "3":
                conditionText = "Clouds Developing"
            case "5":
                conditionText = "Haze"
            case "10":
                conditionText = "Mist"
            case "11":
                conditionText = "Fog"
            case "12":
                conditionText = "Fog"
            case "13":
                conditionText = "Lightning"
            case "19":
                conditionText = "Funnel Cloud Formation: Take Shelter"
            case "20":
                conditionText = "Drizzle"
            case "21":
                conditionText = "Rain"
            case "22":
                conditionText = "Snow"
            case "23":
                conditionText = "Wintery Mix"
            case "24":
                conditionText = "Freezing Rain"
            case "25":
                conditionText = "Rain Showers"
            case "26":
                conditionText = "Snow Showers"
            case "27":
                conditionText = "Hail"
            case "28":
                conditionText = "Fog"
            case "29":
                conditionText = "Thunderstorm"
            case "80": 
                conditionText = "Light Rain"
            case "81":
                conditionText = "Rain"
            case "82":
                conditionText = "Heavy Rain"
            case "83":
                conditionText = "Light Wintery Mix"
            case "84":
                conditionText = "Heavy Wintery Mix"
            case "85":
                conditionText = "Light Snow"
            case "86":
                conditionText = "Heavy Snow"
            case "87":
                conditionText = "Light Small Hail"
            case "88":
                conditionText = "Heavy Small Hail"
            case "89":
                conditionText = "Light Hail"
            case "90":
                conditionText = "Heavy Hail"
            case "91":
                conditionText = "Light Rain"
            case "92":
                conditionText = "Heavy Rain"
            case "93":
                conditionText = "Light Snow"
            case "94":
                conditionText = "Heavy Snow"
            case "95":
                conditionText = "Thunderstorm and Hail"
            case "96":
                conditionText = "Heavy Thunderstorm and Hail"
            case "97":
                conditionText = "Thunderstorm"
            case "99":
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
    

    def GetCategory():

        # Will return simplified categories for Wellness

        conditionCat = ""
        curr = CurrWeatherCode

        if curr == 3 or curr == 1:
            conditionCat = "Cloudy"
        elif curr == 0:
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