sentence = input("Sentence likhein: ")

# Sab alphabets ko chota kar liya taake check karna asaan ho
sentence = sentence.lower()

vowels = 0
consonants = 0

for char in sentence:
    if char.isalpha():  # Sirf agar wo alphabet hai (spaces ya numbers nahi)
        if char in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)