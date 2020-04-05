import json


def save_to_file(data):
    opinions = [opinion.__dict__ for opinion in data]
    with open('opinions.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(opinions, indent=4, ensure_ascii=False))
