numbers = [5, 3, 8, 1, 2, 9]
max_number = 0
for num in numbers:
    if max_number < num:
        max_number = num

print(f'Max number: {max_number}')

word = 'programming'

letters_count = {}
count = 0
for letter in word:
    