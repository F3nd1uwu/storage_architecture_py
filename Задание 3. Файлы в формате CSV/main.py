import csv

# Вычисление среднего значения
def calculate_average(data, column):
    total = sum(float(row[column]) for row in data)
    return total / len(data)

# Вычисление процентного соотношения
def calculate_percentage(data, column, values):
    count = sum(1 for row in data if row[column] in values)
    return (count / len(data)) * 100

# Фильтрация данных и запись их в новый файл
def filter_and_write_to_csv(data, filename):
    header = data[0].keys()
    filtered_data = [row for row in data if float(row['Температура']) > 0]
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(filtered_data)

weather_data = []
filename = './Задание 3. Файлы в формате CSV/var2.csv'
with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            weather_data.append(row)

# Задание 1: Среднее количество осадков за сутки в осенние месяцы
autumn_days = ['сентября', 'октября', 'ноября']
autumn_rainfall = [float(row['Осадки']) for row in weather_data if row['Дата'].split()[1].lower() in autumn_days]
if len(autumn_rainfall) > 0:
    average_autumn_rainfall = sum(autumn_rainfall) / len(autumn_rainfall)
    print("Среднее количество осадков в осенние месяцы:", average_autumn_rainfall)
else:
    print("Нет данных о осенних осадках.")

# Задание 2: Средняя температура в дни, когда дул северный ветер
north_wind_temperatures = [float(row['Температура']) for row in weather_data if row['Ветер'] == 'С']
average_north_wind_temperature = sum(north_wind_temperatures) / len(north_wind_temperatures)
print("Средняя температура в дни с северным ветром:", average_north_wind_temperature)

# Задание 3: Процентное соотношение количества дней с ветрами 'В', 'СВ' и 'ЮВ'
directions_of_interest = ['В', 'СВ', 'ЮВ']
percentage_of_interest_directions = calculate_percentage(weather_data, 'Ветер', directions_of_interest)
print("Процентное соотношение ветров 'В', 'СВ', 'ЮВ':", percentage_of_interest_directions)

# Задание 4: Создание файла с данными о днях с температурой выше нуля градусов
output_filename = './Задание 3. Файлы в формате CSV/res.csv'
filter_and_write_to_csv(weather_data, output_filename)
print("Файл res.csv успешно создан.")
