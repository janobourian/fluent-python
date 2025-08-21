import collections

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
value = collections.Counter(fruits)
print(value)

words = 'apple banana cherry date elderberry fig grape apple banana cherry'
counter_words = collections.Counter(words)
print(counter_words)