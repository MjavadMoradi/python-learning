text = input("Enter a text: ")
reverse_text = ""

for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]

print(reverse_text)