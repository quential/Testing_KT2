import json

input_filename = "SuperHero.json"
output_filename = "SuperHero_new.json"

try:
    with open(input_filename, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"File {input_filename} not found")
    raise SystemExit(1)

members = data["members"]

new_users = [
    {"name": "Spider-Man", "age": 23, "secretIdentity": "New York", "powers": "Shoot webs"},
    {"name": "Bananaman", "age": 98, "secretIdentity": "Banana's town", "powers": ["Fly", "Shot from bananagun", "Make banana-puree"]},
    {"name": "Мега-Тапка", "age": 4, "secretIdentity": "Мухосранск", "powers": "Тапочки"},
    {"name": "Человек сорок", "age": 957, "secretIdentity": "Махачкала", "powers": "Нападают толпой"},

]

members.extend(new_users)


sorted_users = sorted(members, key=lambda x: x["age"])


with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(sorted_users, f, ensure_ascii=False, indent=4)
print(f"\nГотово! файл {output_filename} создан\n")

print("Отсортированный список:")
for user in sorted_users:
    print(f"Имя: {user["name"]} \nВозраст: {user["age"]}\n")