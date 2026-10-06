import csv

def calculate_average(filename):
    total = 0
    count = 0

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row['grade'])
            count += 1


    if count == 0:
        return 0

    return total / count