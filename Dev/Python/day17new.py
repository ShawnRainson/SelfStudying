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
    

class Deadline(Task):
    def __init__(self, title, deadline):
        super().__init__(title)
        self.deadline = deadline
    
    def __str__(self):
        if self._is_complete:
            return f'[X] {self.title}. Deadline: {self.deadline}'
        else:
            return f'[] {self.title}. Deadline: {self.deadline}'


my_deadline = Deadline('New task', '01.01.2027')
print(my_deadline)
my_deadline.complete()
print(my_deadline)
    

