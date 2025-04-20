
## 📘 11.1 Introduction to Functions

### 11.1.1 Topics:
- What is a function?

A function is a block of organized, reusable code used to perform a single, related action.

- Importance of functions

Functions help in breaking a large program into smaller and modular chunks, making the code more manageable, reusable, and readable.

- Types of functions (built-in vs user-defined)

`Built-in functions:` Predefined in Python (e.g., print(), len()).

`User-defined functions:` Defined by the user using the def keyword.

- Modularity and code reuse

Functions help in structuring code logically. Reusing functions avoids code duplication and enhances maintainability.

### 11.1.2 Learning Objectives:
- Understand how functions enhance code structure and readability.

Functions allow you to divide a program into smaller, logical parts. This makes the code easier to read, test, debug, and reuse. For example, instead of repeating code blocks, you can create a function and call it wherever needed.

- Define and invoke functions.

You will learn how to create functions using the def keyword, give them a name, optionally pass parameters, and write the code block that performs a task. You’ll also learn how to call or "invoke" these functions to execute the code inside them.
```python
def greet():
    print("Hello")

greet() 
```
- Differentiate between returning and printing in a function.

`print()` simply displays output on the screen; it does not give back a value to the caller.

`return` sends a result back to the caller so it can be stored or used in further calculations.
```python
def show():
    print("Hello") 
def get_message():
    return "Hello" 
show()               # Output: Hello
msg = get_message()
print(msg)           # Output: Hello
```
## 🧱 11.2 Function Definition

### Notes:

```python
def greet():
    print("Hello, world!")
```

- `def` keyword starts function definition.
- `greet()` is the function name.
- `()` encloses optional parameters.

### 🔍 Key Points:

- The body is indented.
- Function definitions do not execute until called.

---

## 🚀 11.3 Function Invocation

### Notes:

```python
greet()
```

- This executes the function body.
- A function can be called multiple times.

---

## 🎯 11.4 Function Parameters

### Notes:

```python
def greet(name):
    print("Hello", name)
greet("Alice")
```

- Parameters are placeholders for input.
- Arguments are actual values passed.

---

## 🎁 11.5 Returning a Value from a Function

### Notes:

```python
def add(x, y):
    return x + y
result = add(3, 4)
```

- `return` sends a value back to the caller.
- Use the result further in your code.

---

## 👩‍💻 11.6 Decoding a Function

### Practice:

Break down and explain:

```python
def mystery(a, b):
    c = a * b
    print("Sum is", a + b)
    return c
```

---

## 📏 11.7 Type Annotations

### Notes:

```python
def add(x: int, y: int) -> int:
    return x + y
```

- Helps with readability and debugging.
- Not enforced at runtime.

---

## 🧮 11.8 A Function That Accumulates

### Notes:

```python
def accumulate(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

- Used in summation, averages, etc.

---

## 🎯 11.9 Variables and Parameters are Local

### Notes:

```python
def func(x):
    x = x + 1
    print(x)

x = 10
func(x)
print(x)  # Still 10
```

- Variables inside functions are local unless declared global.

---

## 🌍 11.10 Global Variables

### Notes:

```python
count = 0
def increment():
    global count
    count += 1
```

- Use `global` to modify global variables inside a function.

---

## 🔁 11.11 Functions Can Call Other Functions (Composition)

### Notes:

```python
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)
```

- Break large problems into smaller, reusable parts.

---

## 🧭 11.12 Flow of Execution Summary

### Key Ideas:

- Python reads from top to bottom.
- Function body executes **only** when called.
- Each function call starts a new local scope.

---

## 👩‍💻 11.13 Print vs Return

### Notes:

- `print()` outputs to console, used for user-facing messages.
- `return` sends data back to the caller.

```python
def f():
    print("Hi")  # Side effect

def g():
    return "Hi"  # Pure function
```

---

## 🔄 11.14 Passing Mutable Objects

### Notes:

```python
def modify_list(lst):
    lst.append(10)

my_list = [1, 2]
modify_list(my_list)
print(my_list)  # [1, 2, 10]
```

- Mutable objects (lists, dicts) can be changed inside functions.

---

## 💥 11.15 Side Effects

### Notes:
- Any modification of external state (printing, modifying global or mutable objects) is a side effect.

A `side effect` is any observable change made by a function that goes beyond just returning a value.
Common examples include:
- Printing to the console (print())
- Modifying a global variable
- Changing a mutable data structure like a list or dictionary
- Writing to a file or database

💡 Why It Matters:

Pure functions have no side effects — they always return the same output for the same input and don't alter anything outside their scope. This makes them easier to test and debug.

Functions with side effects can be more powerful, but also more difficult to reason about, especially in larger programs.


# 📘 In-depth Assignments:
# 🧠 Level 1 – Basic Understanding

` Focus:` Syntax, simple usage, function calls, return values

1. **Create a function `welcome()` that prints "Welcome to Python!" and call it three times.**
```python
def welcome():
    print("Welcome to Python");
welcome();
welcome();
welcome();
```
2. **Write a function `square(n)` that takes a number `n` and returns its square.**
```python
def square(n):
    return n*n;
print(square(2));
```
3. **Write a function `is_even(num)` that returns `True` if a number is even, else `False`.**
```python
def is_even(num):
    if num%2==0:
        return True
    else :
        return False
print(is_even(2));
```
4. **Define a function `full_name(first, last)` that returns the full name as a string.**
```python
def full_name(first,last):
    return first +" "+ last;
print(full_name("Astha","Singh"));
```
5. **Create a function `circle_area(radius)` that returns the area of a circle using `πr²`. Use `pi = 3.14`.**
```python
import math
def circle_area(radius):
    return math.pi*radius*radius;
print(circle_area(1));
```
---

## ⚙️ Level 2 – Intermediate Skills

> Focus: Parameters, return, iteration, conditionals, type annotations

1. **Define a function `sum_even(numbers: list[int]) -> int` that returns the sum of all even numbers in a list.**
```python
def sum_even(numbers: list[int]) -> int:
    return sum(num for num in numbers if num % 2 == 0)
print(sum_even([1,2,3,4]));
```
2. **Write a function `reverse_string(s: str) -> str` to return the reverse of a string.**
```python
def reverse_string(s:str)->str:
    return s[::-1]
print(reverse_string("astha"))
```
3. **Create a function `fibonacci(n: int) -> list[int]` that returns the first `n` Fibonacci numbers.**
```python
def fibonacci(n:int)-> list[int]:
    if(n<=0):
        return [];
    elif(n==1):
        return [0];
    else:
        fib=[0,1]
        for _ in range(2,n):
            fib.append(fib[-1]+fib[-2])
        return fib
print(fibonacci(7))
```
4. **Write a function `count_vowels(sentence: str) -> int` that counts and returns the number of vowels.**
```python
def count_vowels(sentence:str)->int:
    vowels=['a','e','i','o','u']
    count=0;
    for char in sentence:
        if char in vowels:
            count=count+1
    return count;
print(count_vowels("aeiou"));
```

5. **Write a function `average_marks(marks: list[float]) -> float` that returns the average of marks.**
```python
def average_marks(marks:list[float])->float:
    count=0
    for i in marks:
        count+=i
    avg=count/len(marks)
    return avg
print(average_marks([1,2,3]))
```
---

## 🔬 Level 3 – Advanced Practice

> Focus: Function composition, scope, mutation, edge cases, pure vs impure functions

1. **Create a function `analyze_text(text: str)` that returns:**

   - Number of words
   - Number of unique words
   - Frequency of each word
```python
def analyze_text(text: str):
    words = text.split()
    print("Number of words:", len(words))
    print("Number of unique words:", len(set(words)))   
    print("Frequency of each word:")
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    for word, count in freq.items():
        print(f"{word}: {count}")

analyze_text("astha loves coding and astha enjoys learning coding")

```

2. **Write a function `is_palindrome(s: str) -> bool` that checks if the input string is a palindrome. Ignore cases and spaces.**
```python
def is_palindrome(s:str)-> bool:
    strings=s.lower();
    if strings==strings[::-1]:
        return True
    else:
        return False
print(is_palindrome("adaa"))
```

3. **Implement `nested_sum(data: list) -> int` that takes a nested list of integers and returns the sum of all integers.**
   ```python
   nested_sum([[1, 2], [3, [4, 5]], 6])  # Output: 21
   ```
```python
def nested_sum(data: list) -> int:
    total = 0
    for element in data:
        if isinstance(element, list):
            total += nested_sum(element)  
        else:
            total += element 
    return total
print(nested_sum([[1, 2], [3, [4, 5]],7])) 
```

4. **Create a function `safe_divide(x: float, y: float) -> float` that handles divide-by-zero using try-except.**
```python
def safe_divide(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        return 0.0
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: 0.0
```

5. **Simulate a digital clock with a function `time_increment(h: int, m: int) -> tuple[int, int]` that returns the time after 1 minute. Handle boundary cases (e.g., 23:59).**
```python
def time_increment(h: int, m: int) -> tuple[int, int]:
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
    return h, m
print(time_increment(23, 59))  # Output: (0, 0)
print(time_increment(12, 30))  # Output: (12, 31)
print(time_increment(5, 59))   # Output: (6, 0)
```
---

## 💻 Real-world Problem Set: Function Design and Architecture

> Focus: Realistic situations, reusable function design, side effects, mutable arguments

### **Personal Expense Tracker**

1. Create the following functions:

   - `add_expense(expenses: list[float], amount: float) -> None`
   - `total_expense(expenses: list[float]) -> float`
   - `highest_expense(expenses: list[float]) -> float`
   - `average_expense(expenses: list[float]) -> float`
   - `expense_summary(expenses: list[float]) -> dict[str, float]`

2. Use `global` variable to maintain a transaction count across functions.

3. Add a function `print_report()` that **prints** the entire summary — this demonstrates **side effects vs return**.

4. Apply **function composition** to build `generate_report()` that internally calls the above functions.

---

## 🧠 Conceptual Questions (Code + Theory)

1. **What is the difference between returning a value and printing it? Illustrate with two functions.**
2. **Explain with code how passing a mutable object (like a list) affects the original outside the function.**
3. **Write a function where a global variable is modified and explain the risks involved.**
4. **Demonstrate function composition by creating a calculator that computes `sqrt(x² + y²)` using helper functions.**
5. **Create an example where misunderstanding local scope causes a logic bug. Fix it using correct scoping.**

---

## 🌐 Bonus: Mini Challenges

1. **Write a recursive function to compute factorial of a number.**
2. **Create a function that accepts variable number of arguments and returns their sum.**
3. **Build a mock `login()` function that checks a username and password from a predefined list of users.**
4. **Write a function `flatten_list(nested: list) -> list` that flattens a nested list of any depth.**
5. **Use function annotations and docstrings to fully document a `bmi(weight: float, height: float) -> float` calculator.**

---
