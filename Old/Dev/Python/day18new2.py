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
        if self._is_complete:
            return f'[X] {self.title}. Deadline: {self.deadline}'
        else:
            return f'[] {self.title}. Deadline: {self.deadline}'


valid_text = Task('New task')
valid_text.title = 'Easy task'
print(valid_text)
valid_text.title = ''

    

