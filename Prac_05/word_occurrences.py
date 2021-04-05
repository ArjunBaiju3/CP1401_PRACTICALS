"""Word occurrences in a string"""

count_words = {}
text = input("Enter text: ")

words = text.split()
for word in words:
    word_frequency = count_words.get(word, 0)
    count_words[word] = word_frequency + 1

words = list(count_words.keys())

max_length_of_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length_of_word,
                              count_words[word]))
words.sort()