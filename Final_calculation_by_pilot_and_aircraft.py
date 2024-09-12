import json
import csv

with open('Json_files/target_distances.json', 'r') as file:
    target_distances= json.load(file)
    with open('Json_files/scored_targets.json', 'r') as file:
        targets_data = json.load(file)
with open('Json_files/aircrafts.json', 'r') as file:
    aircrafts_data = json.load(file)
with open('Json_files/pilots.json', 'r') as file:
    pilots_data = json.load(file)

def Calculating_Pilot_Expertise_Points(pilot):
    if pilot<=3:
        return 40
    elif pilot<=5:
        return 60
    elif pilot<=7:
        return 80
    elif pilot<=9:
        return 150
    elif pilot<=10:
        return 175
    else:
        return 0

def Percentage_test_for_distance(aircraft,distance):
    max_points = 150
    min_distance = 400  # הקטן ביותר שמטוס יכול להגיע

    # חישוב ההפרש
    distance_diff = aircraft - distance

    if distance_diff >= 0:
        return max_points  # המרחק מספיק
    else:
        # המרה של מרחק שלילי לאחוזים על סמך המינימום
        distance_percentage = (distance_diff / min_distance) * max_points
        return int( max(0, round(distance_percentage)))  # לא יורדים מ-0 נקודות


# יצירת רשימה לשמירת התוצאות
results = []

# מעבר על כל משימה
for task, distance in targets_data.items():
    # מעבר על כל טייס
    for pilot in pilots_data:
        # מעבר על כל מטוס
        for aircraft in aircrafts_data:
            # חישוב ניקוד התאמה למשימה (לדוגמה חישוב שרירותי לניקוד)
            mission_fit_score=distance+Calculating_Pilot_Expertise_Points(pilot["skill_level"])
            mission_fit_score="{:.2f}".format(mission_fit_score / 1000)
            # הוספת תוצאה לרשימה
            results.append([
                task,  # עיר היעד
                distance,  # עדיפות
                pilot["name"],  # טייס מוקצה
                aircraft["type"],  # סוג מטוס
                distance,  # מרחק בק"מ (נלקח מתוך היעד כרגע, ניתן לשנות)
                "Clear",  # תנאי מזג אוויר (נשאר קבוע כ-Clear)
                pilot["skill_level"],  # רמת מיומנות של הטייס
                aircraft["speed"],  # מהירות המטוס בקמ"ש
                aircraft["fuel_capacity"],  # קיבולת דלק בק"מ
                mission_fit_score  # ניקוד התאמה למשימה
            ])




# כתיבת התוצאות לקובץ CSV
with open('results.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # כתיבת הכותרת
    csvwriter.writerow(['Target City', 'Distance', 'Assigned Pilot', 'Assigned Aircraft', 'Distance (km)',
                        'Weather Conditions', 'Pilot Skill', 'Aircraft Speed (km/h)', 'Fuel Capacity (km)', 'Mission Fit Score'])
    # כתיבת השורות מהתוצאות
    csvwriter.writerows(results)

print("הקובץ 'results.csv' נוצר בהצלחה עם כל האפשרויות האפשריות.")