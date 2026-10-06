import json


# 1. Читаем исходный файл
input_filename = "2file.json"
output_filename = "new3file.json"

try:
    with open(input_filename, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Ошибка: Файл {input_filename} не найден!")
    raise SystemExit(1)

if isinstance(data, dict):
    data = [data]


# 2. Добавляем новых пользователей
new_users = [
    {"name": "Spider-Man", "age": 23, "city": "New York"},
    {"name": "Batman", "age": 42, "city": "Gotham"},
    {"name": "Wonder Woman", "age": 5000, "city": "Themyscira"},
]

data.extend(new_users)


# 3. Сортируем по возрасту (по возрастанию)
sorted_data = sorted(data, key=lambda x: x["age"])


# 4. Сохраняем в новый файл
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=4)

print(f"Готово! Файл {output_filename} создан.")
print("Отсортированный список:")
for user in sorted_data:
    print(f"- {user['name']} ({user['age']} лет)")
