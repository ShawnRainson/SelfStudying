grades_list = {"Shawn": 4.14, "Rachel": 5.0, "Molly": 4.04, "Jason": 3.13, "Sarah": 4.89}
def get_best_student(grades):
    max_grade = 0
    best_student = ""
    for name, grade in grades.items():
        if grade > max_grade:
            max_grade = grade
            best_student = name
    
    print(f'Best student: {best_student}')

get_best_student(grades_list)