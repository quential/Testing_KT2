import csv

def get_letter_grade(average: float) -> str:
    if average >= 95:
        return "A+"
    elif average >= 90:
        return "A"
    elif average >= 85:
        return "A-"
    elif average >= 80:
        return "B+"
    elif average >= 75:
        return "B"
    elif average >= 70:
        return "B-"
    elif average >= 65:
        return "C+"
    elif average >= 60:
        return "C"
    elif average >= 55:
        return "C-"
    elif average >= 50:
        return "D+"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "D-"
    return "F"


def calculate_average(filename):
    test_columns = ("Test1", "Test2", "Test3", "Test4", "Final")
    averages = []

    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            scores = [float(row[column]) for column in test_columns]
            average = sum(scores) / len(scores)
            averages.append(average)

    return averages
