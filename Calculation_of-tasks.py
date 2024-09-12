#חישוב כל המטרות מבחינת מזג האוויר כמה מתאים לתקיפה
import math
import json



def weather_score(weather):
    if weather["main"] == "Clear":
        return 150
    elif weather["main"] == "Clouds":
        return 100
    elif weather["main"] == "Rain":
        return 70
    elif weather["main"] == "Stormy":
        return 20
    else:
        return 0


def priority_score(targets):
    if targets["Priority"] == 1:
        return 40
    elif targets["Priority"] == 2:
        return 80
    elif targets["Priority"] == 3:
        return 100
    elif targets["Priority"] == 4:
        return 150
    elif targets["Priority"] == 5:
        return 200
    else:
        return 0

def speed_score(targets):
        if targets["speed"] <=1:
            return 150
        elif targets["speed"] <=3:
            return 100
        elif targets["speed"] <=5:
            return 70
        elif targets["speed"] <=7:
            return 60
        elif targets["speed"] <= 9:
            return 40
        elif targets["speed"] <= 10:
            return 0
        else:
           return 0


def cloud_score(targets):
    if targets["all"] <= 20:
        return 125
    elif targets["all"] <= 30:
        return 80
    elif targets["all"] <= 35:
        return 60
    elif targets["all"] <= 40:
        return 40
    elif targets["all"] <= 50:
        return 20
    elif targets["all"] <= 60:
        return 1
    else:
        return 0




def calculate_distance(x1, y1, x2, y2):
    # חישוב הפרשים
    delta_x = x2 - x1
    delta_y = y2 - y1
    # חישוב המרחק בעזרת נוסחת פיתגורס
    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

    return distance



def distance_score(distance):
    if distance <= 200:
        return 100
    elif distance <= 400:
        return 90
    elif distance <= 700:
        return 80
    elif distance <= 900:
        return 60
    elif distance <= 1330:
        return 50
    elif distance <= 1600:
        return 40
    elif distance <= 1600:
        return 30

    elif distance <= 2000:
        return 60
    elif distance <= 2500:
        return 50
    elif distance <= 3000:
        return 40
    else:
        return 20

def calculate_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance
# def calculate_distance(x1, y1, x2, y2):
#     delta_x = x2 - x1
#     delta_y = y2 - y1
#     return math.sqrt(delta_x ** 2 + delta_y ** 2)


# קריאת הנתונים מקובץ JSON
with open('Json_files/updated_targets_with_weather.json', 'r') as file:
    targets_data = json.load(file)

# חישוב ציונים לכל מטרה
scored_targets = {}
for target in targets_data:

    distance = calculate_distance(35.2137, 31.7683, target["Longitude"], target["Latitude"])

    score = (
            weather_score(target) +
            priority_score(target) +
            speed_score(target) +
            cloud_score(target) +
            distance_score(distance)
    )


    scored_targets[f"{target["City"]}"] = score


# שמירה של הנתונים עם ציונים לקובץ JSON חדש
with open('Json_files/scored_targets.json', 'w') as file:
    json.dump(scored_targets, file, indent=4)

# scored_targets = {}
# for target in targets_data:
#     distance = calculate_distance(35.2137, 31.7683, target["Longitude"], target["Latitude"])
#     scored_targets[target["City"]] = distance
#
# # שמירה של הנתונים עם מרחקים לקובץ JSON חדש
# with open('Json_files/target_distances.json', 'w') as file:
#     json.dump(scored_targets, file, indent=4)
# print("נתוני המטרות עם הציונים נשמרו בקובץ JSON החדש.")