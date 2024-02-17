class Parents():
    def __init__(self):
        self.Age = 36

class Me(Parents):
    def __init__(self):
        self.Age = 12
        print(self.Age)
        super().__init__()
        print(self.Age)
cl = Me()
