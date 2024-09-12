import json
class FighterJet:
    def __init__(self, jet_type, speed, fuel_capacity):
        self.jet_type = jet_type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

    def __repr__(self):
        return (f"FighterJet(type={self.jet_type}, speed={self.speed}, "
                f"fuel_capacity={self.fuel_capacity})")
    # קריאת הנתונים מקובץ JSON


with open('Json_files/aircrafts.json', 'r') as file:
    aircrafts_data = json.load(file)

    # יצירת אובייקטים של מחלקת FighterJet
jets_objects = [FighterJet(jet["type"], jet["speed"], jet["fuel_capacity"]) for jet in aircrafts_data]

# הדפסת הנתונים
for jet in jets_objects:
    print(jet)