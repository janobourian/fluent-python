def find_anagrams(word, list_of_words):
    return [w for w in list_of_words if sorted(w) == sorted(word)]

print(find_anagrams('code', ["code", "deco", "ecod", "first", "strif", "frist"]))

def xor(A, B):
    return list(map(lambda x: 0 if x[0] == x[1] else 1, zip(A, B)))

print(xor([0, 0, 1, 1], [0, 1, 0, 1]))