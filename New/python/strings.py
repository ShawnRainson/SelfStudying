def count_vowels(text):
    vowels_letters = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in text:
        if letter.lower() in vowels_letters:
            count += 1
    return count

#def is_palindrom(text):
    #Всё ещё не знаю как реализовать, помоги. Не знаю как проверять равенство букв

def count_letters(text):
    letters = {}
    count = 1
    for letter in text:
        if letter not in letters:
            letters[letter] = count
        else:
            letters[letter] += 1
    return letters

def reverse_word(text):
    splitted_text = text.split()
    #Не знаю как переставлять слова, объясни

vowel = count_vowels("hello world!")
word = count_letters("banaaaana")
print(vowel)
print(word)

word1 = reverse_word("hello world python")
print(word1)
