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
    
    @staticmethod
    def filter_completed_tasks(tasks_list):
        new_list = []
        for task in tasks_list:
            if task._is_complete:
                new_list.append(task)
        return new_list

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
    
    def get_overdue_tasks(task_list):
        new_list = []
        for task in task_list:
            if task.is_overdue() == True:
                new_list.append(task)
        return new_list

my_deadline = Deadline('New task', date(2026, 12, 20))
print(my_deadline)
print(my_deadline.is_overdue())

deadline1 = Deadline('First task', date(2023, 11, 11))
deadline2 = Deadline('Second task', date(2026, 11, 11))
deadline3 = Deadline('Third task', date(2024, 11, 11))

deadline1.is_overdue()
deadline2.is_overdue()
deadline3.is_overdue()

tasks_list = []
tasks_list.append(deadline1)
tasks_list.append(deadline2)
tasks_list.append(deadline3)

result = Deadline.get_overdue_tasks(tasks_list)

for res in result:
    print(res)
    
    






    

