def learning_words(list_of_words: list) -> list:
    list_by_word = sorted(list_of_words, key= lambda x: x[::-1])
    dict_with_length = {word: len(word) for word in list_by_word}
    list_by_word = sorted(dict_with_length, key=lambda x: dict_with_length[x])
    return list_by_word

current_list = ["west", "tax", "size", "sea", "use", "think", "yard", "word", "town"]

print("List sorted by length of words:", learning_words(current_list))