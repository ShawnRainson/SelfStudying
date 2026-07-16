try:
    file_name = input('Enter file name: ')
    # Открываем оба файла ОДИН раз (Python позволяет делать это через запятую)
    with open(file_name, 'r', encoding='utf-8') as file, \
         open('errors.txt', 'w', encoding='utf-8') as err_file:
         
        for err_str in file:
            if 'ERROR' in err_str:
                err_file.write(err_str) # Запишет все ошибки по очереди
                
except FileNotFoundError:
    print('Error: File does not exist!')
