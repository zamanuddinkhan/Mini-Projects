# 🔐 Secure Password Generator

A simple **password generator built with Python**.

This program asks the user for a password length and generates a random password using:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

The program uses Python's `secrets` module, which is designed for generating secure random values.

---

## 📌 Project Overview

The program works in four basic steps:

```text
User enters password length
          ↓
Program creates a collection of characters
          ↓
Program randomly selects characters
          ↓
Generated password is displayed
```

For example:

```text
Enter password length: 12

Your password: G7@kP!2xQ#m9
```

The generated password will be different each time.

---

## 🛠️ Technologies Used

* **Python 3**
* `secrets` module
* `string` module

Both `secrets` and `string` are part of Python's standard library, so no external packages are required.

---

## 💻 Source Code

```python
import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter password length: "))

password = ""

for a in range(length):
    password += secrets.choice(chars)

print("Your password:", password)
```

---

# 🔍 Code Explanation

## 1. Import `secrets`

```python
import secrets
```

`secrets` is a Python module used for generating **cryptographically strong random values**.

It is more appropriate than the regular `random` module when generating passwords, tokens, and other security-sensitive values.

---

## 2. Import `string`

```python
import string
```

The `string` module provides useful predefined groups of characters.

Instead of manually typing every letter and number, we can use these built-in values.

---

## 3. Create the character collection

```python
chars = string.ascii_letters + string.digits + string.punctuation
```

This combines three character groups.

### `string.ascii_letters`

Contains:

```text
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### `string.digits`

Contains:

```text
0123456789
```

### `string.punctuation`

Contains common punctuation and special characters such as:

```text
! " # $ % & ' ( ) * + , - . / ...
```

The `+` operator combines all three strings.

So `chars` becomes one large collection of possible password characters.

---

## 4. Ask the user for the password length

```python
length = int(input("Enter password length: "))
```

`input()` asks the user to enter a value.

For example:

```text
Enter password length: 10
```

The value received from `input()` is initially a string:

```python
"10"
```

`int()` converts it into an integer:

```python
10
```

So:

```python
length = 10
```

---

## 5. Create an empty password

```python
password = ""
```

At this point, the password contains nothing.

```text
password
   ↓
""
```

Characters will be added to it one by one.

---

# 🔄 6. Generate the password

```python
for a in range(length):
    password += secrets.choice(chars)
```

This is the main part of the program.

Suppose the user enters:

```text
length = 5
```

Then:

```python
range(length)
```

becomes:

```python
range(5)
```

The loop runs 5 times.

---

## What happens inside the loop?

This line:

```python
secrets.choice(chars)
```

randomly selects **one character** from `chars`.

For example, it might select:

```text
G
7
@
k
P
```

Each selected character is added to `password`.

### First iteration

```text
password = ""
random character = G

password = "" + "G"

password = "G"
```

### Second iteration

```text
password = "G"
random character = 7

password = "G" + "7"

password = "G7"
```

### Third iteration

```text
password = "G7"
random character = @

password = "G7" + "@"

password = "G7@"
```

### Fourth iteration

```text
password = "G7@"
random character = k

password = "G7@" + "k"

password = "G7@k"
```

### Fifth iteration

```text
password = "G7@k"
random character = P

password = "G7@k" + "P"

password = "G7@kP"
```

The final password is:

```text
G7@kP
```

---

# 🖨️ 7. Display the password

```python
print("Your password:", password)
```

This prints the generated password.

Example:

```text
Your password: G7@kP
```

---

# 🧠 Important Python Concepts

This project teaches several useful Python concepts.

### Variables

```python
length = 10
password = ""
```

Variables store information.

---

### User Input

```python
input()
```

Allows the user to provide information to the program.

---

### Type Conversion

```python
int()
```

Converts a string into an integer.

---

### Strings

```python
chars = "abc123"
```

A string is a sequence of characters.

---

### String Concatenation

```python
password += secrets.choice(chars)
```

Adds a character to the existing string.

This:

```python
password += character
```

is equivalent to:

```python
password = password + character
```

---

### For Loop

```python
for a in range(length):
```

Repeats a block of code a specific number of times.

---

### Random Selection

```python
secrets.choice(chars)
```

Selects one character from the available characters.

---

# 🔐 Why `secrets` Instead of `random`?

An earlier version of this project could use:

```python
import random
```

and:

```python
random.choice(chars)
```

However, Python's documentation recommends the `secrets` module for generating random values intended to be difficult to predict, such as passwords and security tokens.

Therefore, this project uses:

```python
secrets.choice(chars)
```

instead of:

```python
random.choice(chars)
```

---

# ⏱️ Time Complexity

Let `n` be the requested password length.

The loop runs `n` times:

```python
for a in range(length):
```

Therefore, the basic generation process performs `n` selections.

```text
Time Complexity: O(n)
```

---

# 💾 Space Complexity

The generated password contains `n` characters.

Therefore, the password requires space proportional to its length.

```text
Space Complexity: O(n)
```

The `chars` string is also stored in memory, but its size is fixed for this program.

---

# ▶️ How to Run

## Step 1: Install Python

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

---

## Step 2: Create the Python file

Create:

```text
pass.py
```

Add the program code to the file.

---

## Step 3: Open the terminal

Navigate to the folder containing `pass.py`.

---

## Step 4: Run the program

```bash
python pass.py
```

---

## Step 5: Enter the desired length

Example:

```text
Enter password length: 16
```

Possible output:

```text
Your password: xQ7@pL#2m$K9!wR4
```

The output will be different each time.

---

# 📚 What I Learned

By building this project, I practiced:

* Importing Python modules
* Using the `secrets` module
* Using the `string` module
* Working with strings
* Taking user input
* Converting strings to integers
* Using `for` loops
* Using `range()`
* Using `choice()`
* String concatenation
* Basic time complexity
* Basic space complexity