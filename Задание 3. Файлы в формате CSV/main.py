import csv

path = 'D:/Code/storage_architecture_py/Задание 3. Файлы в формате CSV'
summ = 0
k = 0

with open(f'{path}/var2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
        print(row[0].split(';'))
        row[0] = row[0].split(';')
        print(row[0][0][2:], row[0][0][3:])
        if (row[0][0][2:] or row[0][0][3:]) in ('сентябрь', 'октябрь', 'ноябрь'):
            summ += int(row[0][2])
            k += 1
        

# sr = summ / k
# print(sr)
