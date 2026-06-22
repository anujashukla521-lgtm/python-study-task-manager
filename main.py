from task import Task
from study_manager import StudyManager


def create_task(task_number):
        title = input(f"\nEnter title of task {task_number}: ")
        sub = input(f"Enter subject of task {task_number}: ")
        priority = input(f"Enter priority of task {task_number}: ")

        t = Task(title,sub,priority)
        return t

def show_menu():
    try:
        manager = StudyManager()
        while True:
            choice = int(input("""====PERSONAL STUDY MANAGER====
            1. Add Task
            2. View Tasks
            3. Complete Task
            4. Delete Task
            5. Search Task
            6. Exit\n
            Enter your choice: 
            """))
            match choice:
                case 1:
                    task1 = create_task(1)
                    manager.add_task(task1)

                case 2:
                    manager.view_tasks()    

                case 3:
                    title = input("Enter title to mark as complete: ")
                    print(manager.complete_task(title))

                case 4:
                    title = input("Enter title to mark as delete: ")
                    print(manager.delete_task(title))
                
                case 5:
                    title = input("Enter title to search: ")
                    print(manager.search_task(title))

                case 6:
                    print("Exit")
                    break
                case _:
                    print("Invalid input")


    except ValueError as e:
        print(e)


if __name__ == "__main__":
    show_menu()
