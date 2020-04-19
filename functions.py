import json


def save_to_file(data, product_id):
    opinions = [opinion.__dict__ for opinion in data]
    with open(f'opinions/{product_id}.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(opinions, indent=4, ensure_ascii=False))


def extract_feature(opinion, selector, attribute=None):
    try:
        return opinion.select(selector).pop()[attribute].strip()
    except KeyError:
        return opinion.select(selector).pop().text.strip()
    except IndexError:
        return None


def clean_string(string, *signs):
    for sign in signs:
        try:
            string = string.replace(sign, ' ')
        except AttributeError:
            break
    return string
