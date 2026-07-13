from datetime import date

class Task:
    def __init__(self, title):
        self._is_complete = False
        self._title = title
    
    def get_info(self):
        return f'Task: {self._title}'
    
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

class Loggable:
    def log(self):
        print(f'Log: {self.title}')

class Deadline(Task, Loggable):
    def __init__(self, title, deadline):
        super().__init__(title)
        self.deadline = deadline
    
    def get_info(self):
        return f'HOT TASK: {self._title}. DEADLINE: {self.deadline}'
    
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


my_deadline = Deadline('Task', date(2026, 12, 12))
my_deadline.log()
print(Deadline.__mro__)