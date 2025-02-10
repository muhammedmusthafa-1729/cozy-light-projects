import requests
import random

# url = "https://random-word-api.herokuapp.com/word"
# words_lengths = {(5, 15), (6, 15), (7, 8), (4, 7)}
# all_words = []
# for word_length, num_words in words_lengths:
#     response = requests.get(url=url, params={"number": num_words, "length": word_length})
#     words = response.json()
#     all_words.extend(words)

# print(all_words)

# all_words = []
# api_key = 0
# for i in range(25):
#     url = "https://api.api-ninjas.com/v1/randomword"
#     headers = {"X-Api-Key": api_key}
#     response = requests.get(url=url, params={"type": "noun"}, headers=headers)
#     all_words.append(response.json()["word"][0])

# print(all_words)

with open("./test.txt", mode="r") as file:
    stored_words = file.readlines()
    stored_words = [word.split("\n")[0] for word in stored_words]

all_words = random.choices(stored_words, k=50)
print(all_words)

google_api_key = 0 # add your own api key


def translate_words_to_malayalam(words, api_key):
    """
    Translate a list of English words into Malayalam using Google Translation API.

    Args:
        words (list): List of English words to translate.
        api_key (str): Your Google Cloud Translation API key.

    Returns:
        dict: Dictionary with English words as keys and Malayalam translations as values.
    """
    url = "https://translation.googleapis.com/language/translate/v2"
    translations = {}

    for word in words:
        params = {
            "q": word,
            "target": "ml",  # Malayalam language code
            "key": api_key
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            translation = response.json().get('data', {}).get('translations', [])[0].get('translatedText', '')
            translations[word] = translation
        else:
            translations[word] = "Error: Unable to translate"

    return translations


# Example usage
words_to_translate = all_words

translations = translate_words_to_malayalam(words_to_translate, google_api_key)
for i, j in translations.items():
    print(i, j)
