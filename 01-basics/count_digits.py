numbers = input("Enter a text: ")
count_digits = 0
for number in numbers:
    if number in "0123456789":
        count_digits += 1

print(count_digits)