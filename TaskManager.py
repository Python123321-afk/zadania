from Task import Task
class TaskManager:
    tasks=[]
    def add_tasks(self,title,description):
        self.tasks.append(Task(description,title))
    def remove_task(self,title):
        found = False
        for i in self.tasks:
            if i.title==title:
                self.tasks.remove(i)
                found = True
        if not found:
            print("Zadanie o podanym tytule nie istnieje")
    def display_tasks(self):
        for i in self.tasks:
            print(f"Tytuł: {i.title} | Status: {i.status}")
    