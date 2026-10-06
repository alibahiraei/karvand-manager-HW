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




        

    

            







        