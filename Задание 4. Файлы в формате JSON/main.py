import json
import csv

with open('./Задание 4. Файлы в формате JSON/sozvezdiya.json', 'r') as f:
    try:
        input_file = json.loads(f)
    except Exception as e:
        print(e)

# print(input_file)