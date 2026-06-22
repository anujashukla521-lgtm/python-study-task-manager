# Personal Study Manager

## Overview

Personal Study Manager is a menu-driven Python application designed to help students organize and manage their study tasks efficiently. The project is built using Object-Oriented Programming (OOP) principles and allows users to add, view, search, complete, and delete study tasks through a simple command-line interface.

This project was created to practice Python OOP concepts, data validation, exception handling, and multi-file project organization.

---

## Features

* Add new study tasks
* View all existing tasks
* Mark tasks as completed
* Delete tasks
* Search tasks by title
* Priority validation (High, Medium, Low)
* Menu-driven user interface
* Exception handling for invalid inputs

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Properties and Setters
* Exception Handling
* Lists
* Functions
* Match-Case Statements

---

## Project Structure

```text
personal-study-manager/
│
├── main.py
├── task.py
├── study_manager.py
└── README.md
```

### File Description

#### main.py

Handles user interaction, menu navigation, and connects all project components.

#### task.py

Contains the `Task` class responsible for task creation, validation, task status management, and task display.

#### study_manager.py

Contains the `StudyManager` class responsible for managing multiple tasks and performing operations such as viewing, searching, completing, and deleting tasks.

---

## Concepts Practiced

### Object-Oriented Programming

* Classes and Objects
* Constructors (`__init__`)
* Encapsulation
* Properties (`@property`)
* Setters (`@setter`)

### Python Fundamentals

* Functions
* Lists
* Loops
* Conditional Statements
* User Input Handling
* Exception Handling

### Project Design

* Multi-file project structure
* Separation of concerns
* CRUD-style operations

---

## How to Run

1. Clone the repository:

```bash
git clone <repository-link>
```

2. Navigate to the project directory:

```bash
cd personal-study-manager
```

3. Run the application:

```bash
python main.py
```

---

## Sample Menu

```text
==== PERSONAL STUDY MANAGER ====

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Search Task
6. Exit

Enter your choice:
```

---

## Key Learnings

* Managing objects using another class
* Building menu-driven applications
* Implementing CRUD operations
* Applying OOP concepts in a real project
* Structuring Python projects across multiple files
* Writing reusable and maintainable code

---

## Future Improvements

* Save tasks to a file
* Load tasks from a file
* Filter tasks by priority
* Display completed and pending tasks separately
* Add due dates and reminders
* Generate task statistics

---

## Author

**Anuja Shukla**

Built as part of my Python learning journey to strengthen Object-Oriented Programming and project development skills.
