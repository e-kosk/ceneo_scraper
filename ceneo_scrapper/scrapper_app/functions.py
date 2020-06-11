
def extract_feature(opinion, selector, attribute=None):
    try:
        return opinion.select(selector).pop(0)[attribute].strip()
    except KeyError:
        return opinion.select(selector).pop(0).text.strip()
    except IndexError:
        return None


def clean_string(string, replacements):
    for sign, replacement in replacements.items():
        try:
            string = string.replace(sign, replacement)
        except AttributeError:
            break
    return string
