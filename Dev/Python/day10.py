my_skills = ['Python', 'Git', 'English']
with open('skills.txt', 'w', encoding='utf-8') as file:
    for el in my_skills:
        file.write(f'Skill: {el}\n')