import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_russian_words():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find("div", id="random_word").text.strip()
        translator = Translator()
        russian_words = translator.translate(english_words, dest="ru").text
        words_definitions = soup.find("div", id="random_word_definition").text.strip()
        russian_definitions = translator.translate(words_definitions, dest="ru").text


        return {
            "russian_words": russian_words,
            "russian_definitions": russian_definitions
        }

    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру!")

    while True:
        word_dict = get_russian_words()
        word = word_dict.get("russian_words")
        word_definition = word_dict.get("russian_definitions")

        print(f"Значение слова: {word_definition}")

        user_input = input("Ваш вариант: ")

        if user_input == word:
            print("Верно!")
        else:
            print(f"Неверно! Было загадано слово: {word}")

        play_again = input("Хотите сыграть еще раз? (y/n) ")

        if play_again.lower() != "y":
            break

word_game()