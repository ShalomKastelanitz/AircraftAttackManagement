#חישוב כל המטרות מבחינת מזג האוויר כמה מתאים לתקיפה
import math
import json



def weather_score(weather):
    if weather["main"] == "Clear":
        return 200
    elif weather["main"] == "Clouds":
        return 170
    elif weather["main"] == "Rain":
        return 40
    elif weather["main"] == "Stormy":
        return 20
    else:
        return 0


def Priority_score(targets):
    if targets["Priority"] == 1:
        return 70
    elif targets["Priority"] == 2:
        return 100
    elif targets["Priority"] == 3:
        return 150
    elif targets["Priority"] == 4:
        return 200
    elif targets["Priority"] == 5:
        return 250
    else:
        return 0

def all_score(targets):
        if targets["speed"] <=1:
            return 150
        elif targets["speed"] <=3:
            return 120
        elif targets["speed"] <=5:
            return 100
        elif targets["speed"] <=7:
            return 70
        elif targets["speed"] <= 9:
            return 50
        elif targets["speed"] <= 10:
            return 0
        else:
           return 0


def all_score(targets):
    if targets["all"] <= 20:
        return 200
    elif targets["all"] <= 30:
        return 150
    elif targets["all"] <= 35:
        return 100
    elif targets["all"] <= 40:
        return 50
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



def all_score(distance):
    if distance <= 200:
        return 200
    elif distance <= 400:
        return 180
    elif distance <= 700:
        return 160
    elif distance <= 900:
        return 140
    elif distance <= 1330:
        return 120
    elif distance <= 1600:
        return 100
    elif distance <= 1600:
        return 70

    elif distance <= 2000:
        return 60
    elif distance <= 2500:
        return 50
    elif distance <= 3000:
        return 40
    else:
        return 20


