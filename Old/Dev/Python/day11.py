with open('skills.txt', 'r', encoding='utf-8') as file:
    for line in file:
        clean_line = line.strip()
        print('! ' + clean_line)