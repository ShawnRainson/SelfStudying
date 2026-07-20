word = 'banana'
letters = {}
count = 1
for letter in word:
    if letter not in letters:
        letters[letter] = count
    elif letter in letters:
        letters[letter] = count + 1
for let, val in letters.items():
    if val == 1:
        print(f'Letter: {let}')

numbers = [5, 2, 8, 5, 3, 2, 9]
num_dict = {}
num_count = 1
for num in numbers:
    if num not in num_dict:
        num_dict[num] = count
    elif num in num_dict:
        num_dict[num] = count + 1

for number, val in num_dict.items():
    if val > 1:
        print(f'Repeated number: {number}')
