import json

class Pilot:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def __repr__(self):
        return f"Pilot(name={self.name}, skill_level={self.skill_level})"

# קריאת הנתונים מקובץ JSON
with open('Json_files/pilots.json', 'r') as file:
    pilots_data = json.load(file)

# יצירת אובייקטים של מחלקת Pilot
pilots_objects = [Pilot(pilot["name"], pilot["skill_level"]) for pilot in pilots_data]

# הדפסת הנתונים
for pilot in pilots_objects:
    print(pilot)
