sentence = "Python is great and Python is easy"
words = sentence.split()
search_word = input("Enter a word: ")
frequency = 0
for word in words:
    if word == search_word:
        frequency += 1
print(frequency)