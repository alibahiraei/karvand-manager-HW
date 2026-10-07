import json
import os

path_karvand="data/karvands.json"
path_report="data/report.json"

# شرط اینکه اگر پوشه دیتا ساخته نشده بود با این دستور ساخته شود
if not os.path.exists("data"):
    os.makedirs("data")

#شرط ساختن فایل های جیسون که اگر وجود نداشتند ساخته شوند
if not os.path.exists(path_karvand):
    with open(path_karvand, "w", encoding="utf-8") as file:
        json.dump(
            {
                "bootcamp": {
                    "title": "Karvand Python",
                    "year": 2026
                },
                "karvands": []
            },
            file,
            ensure_ascii=False,
            indent=4
        )
if not os.path.exists(path_report):
    with open(path_report, "w", encoding="utf-8") as file:
        json.dump([], file)

#ایجاد تابع ها

def read_karvand_json() -> dict:
    try:
        with open(path_karvand, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except json.JSONDecodeError:
        print("JSON database is corrupted.")
        return {
            "bootcamp": {
                "title": "Karvand Python",
                "year": 2026
            },
            "karvands": []
        }

    except FileNotFoundError:
        print("Karvand file not found.")
        return {
            "bootcamp": {
                "title": "Karvand Python",
                "year": 2026
            },
            "karvands": []
        }


def save_karvands(data):
    try:
        with open(path_karvand, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    except Exception as e:
        print(f"Exception occured while saving karvands: {e}.")

def add_karvands():
    try:
        data = read_karvand_json()

        full_name = input("Enter full name: ").strip()
        email = input("Enter email: ").strip()
        city = input("Enter city: ").strip()
        degree = input("Enter degree: ").strip()
        field = input("Enter field: ").strip()
        skill_name = input("Enter skill name: ").strip()
        skill_level = input("Enter skill level: ").strip()
        skill_score = float(input("Enter skill score: "))

        if data["karvands"]:
            new_id = max(
                karvand["id"]
                for karvand in data["karvands"]
            ) + 1
        else:
            new_id = 1

        new_karvand = {
            "id": new_id,
            "full_name": full_name,
            "email": email,
            "city": city,
            "education": {
                "degree": degree,
                "field": field
            },
            "skills": [
                {
                    "name": skill_name,
                    "level": skill_level,
                    "score": skill_score
                }
            ]
        }

        data["karvands"].append(new_karvand)

        save_karvands(data)

        print("Karvand added successfully.")

    except ValueError:
        print("Score must be a number.")

    except Exception as e:
        print(f"Error: {e}")

def show_all_karvand():
    try:
        data = read_karvand_json()

        if not data["karvands"]:
            print("No Karvand has been added yet.")
            return

        for karvand in data["karvands"]:

            print("-------------------------")

            print(f"ID: {karvand['id']}")
            print(f"Name: {karvand['full_name']}")
            print(f"Email: {karvand['email']}")
            print(f"City: {karvand['city']}")

            print(
                f"Degree: "
                f"{karvand['education']['degree']}"
            )

            print(
                f"Field: "
                f"{karvand['education']['field']}"
            )

            print("Skills:")

            for skill in karvand["skills"]:
                print(
                    f"  {skill['name']} - "
                    f"{skill['level']} - "
                    f"{skill['score']}"
                )

    except Exception as e:
        print(f"Error: {e}")


# اجرای برنامه -----------------------------------------------------------
while True:
    print("\n--- Karvand Manager ---")
    print("1. Add Karvand")
    print("2. show_all")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_karvands()

    elif choice == "2":
        show_all_karvand()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


        

    

            







        