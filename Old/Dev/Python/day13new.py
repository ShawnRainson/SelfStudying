class Task:
    def __init__(self, title):
        self.is_complete = False
        print(f'Task state: {self.is_complete}')
        print(f'Task: {title}')
    
    def complete(self):
        self.is_complete = True
        print(f'Task state: {self.is_complete}')

my_task = Task('Learn OOP')
my_task.complete()

