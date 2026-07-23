text = "banana"
letters = {}
for letter in text:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1
for letter, val in letters.items():
    if val == 1:
        print(letter)


numbers = [3, 7, 1, 9, 2]
max_number = -1
second_mac_number = -1
for number in numbers:
    if max_number < number:
        max_number = number

for number in numbers:
    if second_mac_number < max_number and second_mac_number < number and number != max_number:
        second_mac_number = number

print(second_mac_number)