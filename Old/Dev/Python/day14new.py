class Task:
    def __init__(self, title):
        self.is_complete = False
        self.title = title
    
    def complete(self):
        self.is_complete = True
    
    def __str__(self):
        if self.is_complete == True:
            return f'[X] {self.title}'
        else:
            return f'[] {self.title}'
    

my_task = Task('Learn OOP')
print(my_task)
my_task.complete()
print(my_task)

