eng_level = input('Какой у тебя уровент английского? (A1, A2, B1, B2): ')
eng_level1 = eng_level.upper()
if (eng_level1 == 'A1') | (eng_level1 == 'A2'):
    print('Тебе нужно учить базовую грамматику!')
elif (eng_level1 == 'B1') | (eng_level1 == 'B2'):
    print('Отлично! Пора практиковать разговорную речь!')
else:
    print('Я не знаю такого уровня.')