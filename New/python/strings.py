def count_vowels(text):
    vowels_letters = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in text:
        if letter.lower() in vowels_letters:
            count += 1
    return count

def is_palindrom(text):
    #Не знаю как сделать проверку палиндрома без встроенных функций
