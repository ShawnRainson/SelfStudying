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
        if self._is_complete:
            return f'[X] {self.title}. Deadline: {self.deadline}'
        else:
            return f'[] {self.title}. Deadline: {self.deadline}'


task1 = Task('First task')
task2 = Task('Second task')
task3 = Task('Third task')
task4 = Task('Fourth task')
task5 = Task('Fifth task')
task1.complete()
task5.complete()
tasks = []
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)
tasks.append(task4)
tasks.append(task5)

result = Task.filter_completed_tasks(tasks)
for completed_task in result:
    print(completed_task)



    

