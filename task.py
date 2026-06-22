class Task:
    def __init__(self,title,subject,priority):
        self._title = title
        self._subject = subject
        self.priority = priority
        self._status = "Pending"

    @property
    def title(self):
        return self._title

    @property
    def subject(self):
        return self._subject

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self,value):
        if value.lower() in ["high","medium","low"]:
            self._priority = value.capitalize()
        else:
            raise ValueError("Priority must be high, medium or low")

    @property
    def status(self):
        return self._status

    def mark_completed(self):
        self._status = "Completed"
        return "Task marked as completed"

    def display(self):
        print("\n========DISPLAYING TASK========")
        print("Task Title:",self.title)
        print("Subject:",self.subject)
        print("Priority:",self.priority)
        print("Status:",self.status)


