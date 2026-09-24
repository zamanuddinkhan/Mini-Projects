# 📝 To-Do App

A simple **command-line To-Do App built with Python**.

This project allows users to add, update, delete, and view tasks directly from the terminal. It is a beginner-friendly Python project designed to practice basic programming concepts and CRUD operations.

---

## 📌 Features

* ➕ Add a new task
* ✏️ Update an existing task
* 🗑️ Delete a task
* 👀 View all tasks
* 🚪 Exit the application
* ⚠️ Handle invalid menu input
* 🔍 Check whether a task exists before updating or deleting it

---

## 🛠️ Technologies Used

* **Python 3**
* Python Lists
* Functions
* `for` loop
* `while` loop
* `if / elif / else`
* `try / except`
* `input()`
* `append()`
* `index()`
* `del`

No external libraries are required.

---

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

### 2. Run the Application

Open the terminal inside the project folder and run:

```bash
python todo_app.py
```

---

# 💻 How It Works

When the program starts, it displays:

```text
---- WELCOME TO THE TO-DO APP ----
```

The program asks how many tasks you want to add.

Example:

```text
Enter how many tasks you want to add = 3

Enter task 1 = Learn Python
Enter task 2 = Practice SQL
Enter task 3 = Build Project
```

These tasks are stored inside a Python list:

```python
tasks = [
    "Learn Python",
    "Practice SQL",
    "Build Project"
]
```

After that, the application displays the main menu.

---

# 📋 Menu

```text
Enter
1 - Add
2 - Update
3 - Delete
4 - View
5 - Exit/Stop
```

The user can select an option from `1` to `5`.

---

# 🧠 Python Concepts Used

## 1. Functions

The application is organized inside a function:

```python
def todo_app():
```

The function is called at the end:

```python
todo_app()
```

---

## 2. Lists

A list is used to store multiple tasks:

```python
tasks = []
```

Example:

```python
tasks = ["Learn Python", "Practice SQL"]
```

---

## 3. `append()`

`append()` adds a new task to the list:

```python
tasks.append(add)
```

Example:

```python
tasks = ["Learn Python"]

tasks.append("Practice SQL")
```

Result:

```python
["Learn Python", "Practice SQL"]
```

---

## 4. `for` Loop

The `for` loop is used to add the initial tasks:

```python
for i in range(1, total_task + 1):
    task_name = input(f"Enter task {i} = ")
    tasks.append(task_name)
```

---

## 5. `while` Loop

The menu needs to continue showing until the user chooses Exit.

Therefore, the program uses:

```python
while True:
```

The loop stops when:

```python
break
```

is executed.

---

## 6. Conditional Statements

The application uses `if`, `elif`, and `else` to determine which operation the user selected:

```python
if operation == 1:
    # Add

elif operation == 2:
    # Update

elif operation == 3:
    # Delete

elif operation == 4:
    # View

elif operation == 5:
    # Exit

else:
    # Invalid input
```

---

## 7. `index()`

The `index()` method finds the position of a task in the list.

Example:

```python
tasks = ["Python", "SQL", "JavaScript"]

index = tasks.index("SQL")

print(index)
```

Output:

```text
1
```

Python list indexing starts from `0`:

```text
Python      → 0
SQL         → 1
JavaScript  → 2
```

---

## 8. `del`

The `del` keyword removes an item from the list:

```python
del tasks[ind]
```

Example:

```python
tasks = ["Python", "SQL", "JavaScript"]

del tasks[1]
```

Result:

```python
["Python", "JavaScript"]
```

---

## 9. Exception Handling

The application uses `try` and `except` to handle invalid menu input:

```python
try:
    operation = int(input(...))
```

If the user enters something like:

```text
abc
```

instead of a number, Python would normally raise a `ValueError`.

The application handles it with:

```python
except ValueError:
    print("Invalid Input. Please enter a valid number.")
```

---

# 🔄 CRUD Operations

The To-Do App is a simple example of **CRUD operations**.

CRUD means:

| Operation  | Meaning     | To-Do App     |
| ---------- | ----------- | ------------- |
| **Create** | Add data    | Add a task    |
| **Read**   | View data   | View tasks    |
| **Update** | Modify data | Update a task |
| **Delete** | Remove data | Delete a task |
