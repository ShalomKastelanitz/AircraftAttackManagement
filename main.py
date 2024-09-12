
import  json
#שמירת הגיסון במבנה נתונים סטנדרטי  דיפולטיבי של פייתון
def load_json_from_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


# הפיכת הקובץ של מטוסים למבנה נתונים
file_path = 'Json_files/aircrafts.json'
aircrafts = load_json_from_file(file_path)
# הצגת התוצאה
print(aircrafts)
# הפיכת הקובץ של טיסים למבנה נתונים
file_path = 'Json_files/pilots.json'
pilots = load_json_from_file(file_path)
# הצגת התוצאה
print(pilots)
# הפיכת הקובץ של מטרות (בסיסי) למבנה נתונים
file_path = 'Json_files/targets.json'
targets = load_json_from_file(file_path)
# הצגת התוצאה
print(targets)

