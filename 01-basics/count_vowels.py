word = input("Enter a text: ") 
count_vowels = 0
for ch in word:
    if ch in "aeiou":
        count_vowels += 1
        
print(count_vowels) 