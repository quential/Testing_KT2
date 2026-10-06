import csv
from pathlib import Path

from main import calculate_average, get_letter_grade


def test_letter_grade_matches_csv():
    csv_file = Path(__file__).with_name("grades.csv")
    averages = calculate_average(csv_file)

    with csv_file.open(mode="r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert len(averages) == len(rows)

    for row, average in zip(rows, averages):
        actual_grade = get_letter_grade(average)
        expected_grade = row["Grade"].strip().strip('"')

        assert actual_grade == expected_grade, (
            f"{row['Last name'].strip()}: "
            f"expected {expected_grade}, got {actual_grade}; "
            f"average = {average:.2f}"
        )
