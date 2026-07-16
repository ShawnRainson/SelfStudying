project = {"title": "my-project", "language": "Python", "status": "planned"}
while True:
    question = input('Что вы хотите узнать о проекте? (title, language, status, exit): ')
    answer = question.lower()
    if answer == 'title':
        print(f'Название проекта: {project["title"]}')
    elif answer == 'language':
        print(f'Язык разработки: {project["language"]}')
    elif answer == 'status':
        print(f'Статус проекта: {project["status"]}')
    elif answer == 'exit':
        print('Пока-пока!')
        break
    else:
        print('Такого параметра не существует!')