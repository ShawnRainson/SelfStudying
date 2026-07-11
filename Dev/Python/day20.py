from datetime import date

class Task:
    def __init__(self, title):
        self._is_complete = False
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, text):
        if not Task.valid_title(text):
            print('Error: Title too short or empty!')
        else:
            self._title = text

    
    def complete(self):
        self._is_complete = True
    
    def __str__(self):
        if self._is_complete:
            return f'[X] {self.title}'
        else:
            return f'[] {self.title}'
    
    @staticmethod
    def valid_title(title_text):
        title_length = len(title_text)
        if title_length < 3:
            return False
        else:
            return True

class Deadline(Task):
    def __init__(self, title, deadline):
        super().__init__(title)
        self.deadline = deadline
    
    def __str__(self):
        return f'{super().__str__()}. Deadline: {self.deadline}'
    
    def is_overdue(self):
        if date.today() > self.deadline:
            return True
        else:
            return False

def filter_completed_tasks(tasks_list):
        new_list = []
        for task in tasks_list:
            if task._is_complete:
                new_list.append(task)
        return new_list

def get_overdue_tasks(task_list):
        new_list = []
        for task in task_list:
            if isinstance(task, Deadline) and task.is_overdue():
                new_list.append(task)
        return new_list

task1 = Task('First task');
task1.complete()
task2 = Deadline('Second task', date(2025, 12, 12))
task2.is_overdue()
task3 = Deadline('Third task', date(2026, 10, 23))
task3.is_overdue()
task4 = Task('Fourth task')
task5 = Deadline('Fifth', date(2022, 2, 22))
task5.is_overdue()

tasks = []
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)
tasks.append(task4)
tasks.append(task5)

complete = filter_completed_tasks(tasks)
overdue = get_overdue_tasks(tasks)

for comp in complete:
    print(f'Complete: {complete}')

for over in overdue:
    print(f'Overdue: {over}')