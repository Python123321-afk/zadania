class Task():
    def __init__(self,description,name):
        self.title=name
        self.description=description
        self.status="TODO"
    def mark_as_done(self):
        self.status="DONE"
    def display_task(self):
        print(f"Tytuł: {self.title} | Opis: {self.description} | Status: {self.status}")    