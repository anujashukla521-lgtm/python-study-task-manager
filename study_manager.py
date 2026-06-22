from task import Task

class StudyManager:
    def __init__(self):
        self.tasks = []

    
    def add_task(self,task):
        self.tasks.append(task)
        return "Task added successfully"


    def view_tasks(self):
        if not self.tasks:
            print("No task found")
            return

        for task in self.tasks:
            task.display()

    def complete_task(self,title):
        for task in self.tasks:
            if title.lower() == task.title.lower():
                task.mark_completed()
                return f"{task.title} marked as completed"
    
        return "Task not found"


    def delete_task(self,title):
        for task in self.tasks:
            if title.lower() == task.title.lower():
                self.tasks.remove(task)
                return f" Task {task.title} deleted successfully"

        return "Task not found"

    def search_task(self,title):
        for task in self.tasks:
            if title.lower() == task.title.lower():
                task.display()
                return f"{task.title} displayed"
                
        return "Task not found"