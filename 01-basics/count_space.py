spaces = input("Enter a text: ")
count_spaces = 0
for ch in spaces:
    if ch == " ":
        count_spaces += 1
print(count_spaces)