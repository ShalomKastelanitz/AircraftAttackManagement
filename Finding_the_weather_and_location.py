import requests
import json
from datetime import datetime, timezone

# #לקיחת הפרטים מהמיקום ולשים בקובץ חדש
# # המפתח ל-OpenWeatherMap API
# api_key = "683e89824b304dc79927246bad29c1ef"
#
# # קריאת הנתונים מקובץ ה-JSON הקיים
# with open('Json_files/targets.json', 'r') as file:
#     targets_data = json.load(file)
#
#
# # פונקציה לקבלת קו אורך ורוחב של עיר
# def get_coordinates(city, api_key):
#     url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
#     response = requests.get(url)
#     data = response.json()
#
#     if data:
#         lat = data[0]["lat"]
#         lon = data[0]["lon"]
#         return lat, lon
#     return None, None
#
#
# # עדכון המבנה עם קווי אורך ורוחב
# for target in targets_data:
#     city = target["City"]
#     lat, lon = get_coordinates(city, api_key)
#
#     if lat and lon:
#         target["Latitude"] = lat
#         target["Longitude"] = lon
#
# # # שמירת הנתונים המעודכנים לקובץ JSON
# # with open('Json_files/targets_with_coordinates.json', 'w') as f:
# #     json.dump(targets_data, f, indent=4)
#
# print("הערים עודכנו עם קווי אורך ורוחב")


#לקיחת הפרטים של מזג האוויר ולשים במשתנה

# המפתח ל-OpenWeatherMap API
api_key = "683e89824b304dc79927246bad29c1ef"

# קריאת הנתונים מקובץ JSON הקיים
with open('Json_files/targets_with_coordinates.json', 'r') as file:
    targets_data = json.load(file)

# פונקציה לקבלת פרטי מזג האוויר של עיר
def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:  # אם הבקשה הצליחה
        # נתוני מזג האוויר של השעה 12 בלילה
        target_time = "00:00:00"
        for item in data["list"]:
            dt_txt = item["dt_txt"]
            if dt_txt.endswith(target_time):  # אם השעה מתאימה
                return {
                    "dt_txt": dt_txt,
                    "all": item["clouds"]["all"],
                    "speed": item["wind"]["speed"],
                    "main": item["weather"][0]["main"]
                }
    return None

# משתנה לשמירה של הנתונים המעודכנים
updated_targets_data = []

# עדכון המבנה עם פרטי מזג האוויר
for target in targets_data:
    city = target["City"]
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        updated_target = target.copy()  # יוצרתי עותק של המילון המקורי
        updated_target.update(weather_data)  # עדכון המילון עם נתוני מזג האוויר
        updated_targets_data.append(updated_target)  # הוספת הנתונים המעודכנים לרשימה

# הדפסת הנתונים המעודכנים
print("נתוני הערים עם פרטי מזג האוויר:")
for data in updated_targets_data:
    print(data)