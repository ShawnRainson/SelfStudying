try:
    file_name = input('Enter file name (example.txt): ')
    with open(file_name, 'r', encoding='utf-8') as file:
        first_line = file.readline()
        first_line = first_line.strip()
        print(f'First line: {first_line}')
        
except FileNotFoundError:
    print('File missed!')