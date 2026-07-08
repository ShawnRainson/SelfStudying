class Task:
    def __init__(self, title):
        self._is_complete = False
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, text):
        if text == "":
            print('Error: Title is empty!')
        else:
            self._title = text
    
    def complete(self):
        self._is_complete = True
    
    def __str__(self):
        if self._is_complete:
            return f'[X] {self.title}'
        else:
            return f'[] {self.title}'
    
    

my_task = Task("My first task")
my_task.title = ""
print(my_task.title)
my_task.title = 'New task'
print(my_task.title)

