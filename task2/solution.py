import requests
import csv
from collections import Counter
import time

API_URL = "https://ru.wikipedia.org/w/api.php"
CATEGORY = "Категория:Животные_по_алфавиту"

def get_animals_by_letter():
    letter_counts = Counter()
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": CATEGORY,
        "cmlimit": "500",
        "format": "json"
    }
    session = requests.Session()
    while True:
        resp = session.get(API_URL, params=params)
        data = resp.json()
        for page in data["query"]["categorymembers"]:
            title = page["title"]
            if title:
                first = title[0].upper()
                letter_counts[first] += 1
        if "continue" in data:
            params["cmcontinue"] = data["continue"]["cmcontinue"]
            time.sleep(0.2)  # чтобы не спамить API
        else:
            break
    return letter_counts

def save_to_csv(counter, filename='beasts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for letter, count in sorted(counter.items()):
            writer.writerow([letter, count])

if __name__ == '__main__':
    counts = get_animals_by_letter()
    save_to_csv(counts) 