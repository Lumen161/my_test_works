import random
from typing import Any


def create_check_list() -> None:
    words = ['work', 'life', 'python', 'home', 'PC',
             'Just', 'Work', 'Home', 'sun', 'moon',
             'sky', 'tell', 'about', 'think', 'blood',
             'rain', 'train', 'people', 'air', 'airplane']

    with open('upload.txt', 'w') as f:
        for i in range(50):
            for j in range(random.randint(4, 20)):
                f.write(random.choice(words) + ' ')

            f.write('\n')


def count_words(content: list, check_case=False) -> list[Any]:
    dict_words = dict()

    for word in content:
        word = word.lower() if check_case else word
        dict_words[word] = dict_words.get(word, 0) + 1
    count = len(content)
    for key, val in dict_words.items():
        dict_words[key] = (val, round(val / count, 2))

    sorted_idf_desc = sorted(dict_words.items(), key=lambda item: item[1][1])

    return sorted_idf_desc


def main():
    """ Создавалось исключительно для тестов"""
    create_check_list()

    with open('upload.txt', 'r') as f:
        content = f.read().split()
    print(count_words(content))


if __name__ == "__main__":
    main()
