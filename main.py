import csv

# רשימת המשימות עם ציונים
tasks = {
    "Tehran": 1000,
    "Baghdad": 920,
    "Damascus": 950,
    "Kabul": 950,
    "Sanaa": 720,
    "Riyadh": 920,
    "Cairo": 820,
    "Beirut": 870,
    "Amman": 870,
    "Tripoli": 411,
    "Khartoum": 571,
    "Mosul": 800,
    "Fallujah": 740,
    "Kandahar": 790,
    "Marrakesh": 710
}

# רשימת הטייסים
pilots = [
    {"name": "John Doe", "skill_level": 8},
    {"name": "Jane Smith", "skill_level": 6},
    {"name": "Michael Johnson", "skill_level": 7},
    {"name": "Emily Davis", "skill_level": 9},
    {"name": "Robert Brown", "skill_level": 5},
    {"name": "Sarah Wilson", "skill_level": 8},
    {"name": "David Lee", "skill_level": 6},
    {"name": "Chris Walker", "skill_level": 7},
    {"name": "Jessica Miller", "skill_level": 10},
    {"name": "Daniel Harris", "skill_level": 4}
]

# רשימת המטוסים
jets = [
    {"type": "F-16", "speed": 2400, "fuel_capacity": 5000},
    {"type": "F-35", "speed": 3000, "fuel_capacity": 6000},
    {"type": "MiG-29", "speed": 2450, "fuel_capacity": 4500},
    {"type": "Su-27", "speed": 2500, "fuel_capacity": 5200},
    {"type": "Eurofighter Typhoon", "speed": 2495, "fuel_capacity": 5600},
    {"type": "Rafale", "speed": 2130, "fuel_capacity": 4700},
    {"type": "F/A-18", "speed": 1915, "fuel_capacity": 4900}
]

# יצירת רשימה לשמירת התוצאות
results = []

# מעבר על כל משימה
for task, distance in tasks.items():
    # מעבר על כל טייס
    for pilot in pilots:
        # מעבר על כל מטוס
        for jet in jets:
            # חישוב ניקוד התאמה למשימה (לדוגמה חישוב שרירותי לניקוד)
            mission_fit_score = round((pilot["skill_level"] / 10) * (jet["speed"] / 3000) * (jet["fuel_capacity"] / 6000), 2)
            # הוספת תוצאה לרשימה
            results.append([
                task,  # עיר היעד
                distance,  # עדיפות
                pilot["name"],  # טייס מוקצה
                jet["type"],  # סוג מטוס
                distance,  # מרחק בק"מ (נלקח מתוך היעד כרגע, ניתן לשנות)
                "Clear",  # תנאי מזג אוויר (נשאר קבוע כ-Clear)
                pilot["skill_level"],  # רמת מיומנות של הטייס
                jet["speed"],  # מהירות המטוס בקמ"ש
                jet["fuel_capacity"],  # קיבולת דלק בק"מ
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
