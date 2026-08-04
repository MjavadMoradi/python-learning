sentence = "I love Python programming"
words = sentence.split()

search_word = input("Enter a word to find: ")

found = False

for word in words:
    if word == search_word:
        found = True

if found:
    print("Found")
else:
    print("Not Found")