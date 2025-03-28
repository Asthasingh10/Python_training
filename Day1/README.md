# Variables, Statements, and Expressions: A Learning Task


## 2.1.1. Learning Goals

### Understand the basics of variables, expressions, and statements in Python.

#### Variable-
A variable is a name that refers to a value stored in memory.In python, you don't need to declare a variable before using it; you just assign a value to it.

 ```python
    x= 10  # x is a variable storing the integer 10
    name = "Astha"#name is a variable storing the string "Astha"
    pi = 3.14  # pi stores a floating-point number
 ```

#### Expression -
An expression is a combination of values, variables, and operators that Python evaluates to produce another value.

```python
a = 5
b = 10
c = a + b  # Expression: a + b evaluates to 15
d = (a * b) / 2  # Expression: (5 * 10) / 2 = 25.0
```


#### Statement -
A statement is a unit of code that performs an action. A statement may or may not produce a value.
```python
x = 100  # Assignment statement
print("Hello, World!")  # Print statement
if x > 50:  # Conditional statement
    print("x is greater than 50")
```

### Differentiate between data types and apply type conversions.
A data type defines the kind of value a variable can hold. Python has several built-in data types:
##### Datatype- 
int,float,char,boolean,string, list, boolean ,set , tuple,custom datatype, Dictionary
##### TypeConversion- 
Type conversion is the process of converting one data type into another.
#### Implicit Type Conversion (Automatic)-
```python
a = 5   # int
b = 2.5 # float
c = a + b  # Python converts 'a' to float, so c becomes 7.5 (float)
print(type(c))  # Output: <class 'float'>
```

#### Explicit Type Conversion (Automatic)-
You can manually convert data types using functions like int(),float(), str(), etc.
```python
x = "100"
y = int(x)  # Convert string to int
z = float(y)  # Convert int to float

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'float'>
```


### Properly name variables following Python conventions-
- Use letters (a-z, A-Z), digits (0-9), and underscores (_) only.

```python
valid_name = "Astha"
age_21 = 21
```
- Must start with a letter or an underscore (_), but not a digit.

```python

_private_variable = "Hidden"
name1 = "John" 
# 1name = "Invalid" ❌ (Starts with a 
### Properly name variables following Python conventions-digit)
```

- Case-sensitive: name, Name, and NAME are different variables.

```python
user = "Alice"
User = "Bob"  # Different from 'user'
```

- Cannot use Python keywords (reserved words).

```python
#  if = 10  ❌ (Invalid, 'if' is a keyword)
```

- Avoid using -  special characters (!@#$%^&*), starting with a number, using reserved word


###  Grasp the flow of execution through function calls and expressions-
The flow of execution determines the order in which statements and function calls are executed in a Python program.

1. Flow of Execution in Function Calls
How Function Calls Work
- The main script starts executing from the first line.
- When a function is called, execution jumps to the function definition.
- The function executes its statements.
- Once the function completes, execution returns to the point where it was called.

```python
def greet(name):  # Function definition
    print("Hello,", name)  # Executes when function is called

print("Start of program")  # Step 1
greet("Astha")  # Step 2: Function call (execution jumps to function)
print("End of program")  # Step 3: Execution resumes here after function call
```

2. Flow of Execution in Expressions-

Expressions are evaluated before being used in statements.

Example: 
```python
a = 5
b = 10
c = a + b * 2  # Multiplication (*) happens first, then addition (+)
print(c)  # Output: 25
```
3. Function Call Stack (Nested Calls)

When multiple functions call each other, execution follows a stack (Last-In-First-Out).
```python
def multiply(x, y):
    return x * y  # Step 3

def calculate():
    result = multiply(3, 4)  # Step 2: Calls multiply()
    print(result)  # Step 4

calculate()  # Step 1: Calls calculate()
```
4. Flow Control with Conditional and Loop Statements

Functions and expressions execute sequentially unless modified by conditionals (if-else) or loops (for, while).
```python
def countdown(n):
    while n > 0:  # Step 2: Loop executes until n = 0
        print(n)  
        n -= 1  # Step 3: Decreases n

    print("Blast off!")  # Step 4: Executes after loop ends

countdown(3)  # Step 1: Calls countdown()
```

### Update and reassign variables effectively.
Variables in Python can be updated and reassigned dynamically, allowing for flexible and efficient code.

1. Reassigning Variables:

A variable can be assigned a new value at any point in the program.
```python
x = 10  # Initial assignment
print(x)  # Output: 10

x = 20  # Reassignment
print(x)  # Output: 20
```
2. Updating Variables (Using Current Value):

You can update a variable using its existing value.
```python
count = 5
count = count + 1  # Updates count by adding 1
print(count)  # Output: 6
```
3. Swapping Values Without a Temporary Variable:
Python allows swapping values in a single step.
```python
a = 5
b = 10
a, b = b, a  # Swap values
print(a, b)  # Output: 10 5
```
4. Reassigning with Different Data Types:

Python variables are dynamically typed, meaning they can hold values of different types at different times.
```python
x = 10  # Integer
x = "Hello"  # String
x = [1, 2, 3]  # List
print(x)  # Output: [1, 2, 3]
```
✔ Python allows changing types without restrictions.


## 2.2. Values and Data Types

1. *Research:*
 
 -   What is a value in Python?

A value in Python is a piece of data stored in memory that can be assigned to a variable or used directly in expressions. Values represent data that Python programs manipulate.
Each value in Python has an associated data type, which determines how Python stores and manipulates the value.

2. *Identify different data types in Python (e.g., integers, floats, strings, booleans).:*
    1. Numeric -int,float,
    2. Sequence- string,list,tuple,range
    3. Dictionary- key and value pairs
    4. Boolean- bool
    5. None- when value is not assigned
    6. Set- set,frozenset
    7. Custom Datatype
    8. Binary - bytes, bytearray

 3. *Exercise:*
 ```python
 # Assigning values to variables
num = 42               # Integer
pi = 3.14             # Float
name = "Astha"        # String
is_python_fun = True  # Boolean
fruits = ["apple", "banana", "cherry"]  # List
coordinates = (10, 20)  # Tuple
unique_nums = {1, 2, 3}  # Set
student = {"name": "Astha", "age": 22}  # Dictionary
binary_data = bytes([65, 66, 67])  # Bytes

# Printing the type of each variable
print("Type of num:", type(num))
print("Type of pi:", type(pi))
print("Type of name:", type(name))
print("Type of is_python_fun:", type(is_python_fun))
print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of unique_nums:", type(unique_nums))
print("Type of student:", type(student))
print("Type of binary_data:", type(binary_data))
```


## 2.3. Operators and Operands

 *Research:*
   - Learn about arithmetic, comparison, and logical operators

        In Python, operators are special symbols that perform operations on values (operands). They can be classified into different categories:

1. Arithmetic Operators- +, - , * , / , // , %, **
2. Relational Operators- ==	Equal to,!=	Not equal to,>	Greater than, <	Less than, >=	Greater than or equal to,<=Less than equal to
3. Logical Operators- and, or ,not
4. Bitwise Operators- &(and),`(or),^(xor),~(bitwise not),<<(Left shift),>>(Right shift)
5.  Assignment Operators- ==,+=,*=,-= and many more.
6. Identity Operators- is ,is not
7. Membership Operator- in, not in

 *Exercise :*
  Create a Python script that demonstrates:
     - Addition, subtraction, multiplication, and division.
     - Comparisons between numbers.
     - Logical operations like and, or, not.
```python
# Arithmetic Operations
a = 10
b = 5

print("Addition:", a + b)        # 10 + 5 = 15
print("Subtraction:", a - b)     # 10 - 5 = 5
print("Multiplication:", a * b)  # 10 * 5 = 50
print("Division:", a / b)        # 10 / 5 = 2.0

# Comparison Operations
x = 15
y = 20

print("\nIs x equal to y?", x == y)   # False
print("Is x not equal to y?", x != y) # True
print("Is x greater than y?", x > y)  # False
print("Is x less than or equal to y?", x <= y)  # True

# Logical Operations
p = True
q = False

print("\nLogical AND (p and q):", p and q)  # False
print("Logical OR (p or q):", p or q)       # True
print("Logical NOT (not p):", not p)        # False
```

## 2.4. Function Calls

### 2.4.1. Function Calls as Part of Complex Expressions

1. *Fun Fact:*
   - In Python, functions are first-class objects, meaning they can be assigned to variables and passed as arguments.
2. *Exercise:*
   - Write a program that uses built-in functions inside expressions:
     python
     numbers = [5, 3, 8, 1]
     print(max(numbers) - min(numbers))
     


### 2.4.2. Functions are Objects; Parentheses Invoke Functions

1. *Exercise:*
   - Assign a function to a variable, then call the function using the new variable:
   ```python
     greet = print
     greet('Hello, World!')
    ```     

In Python, functions are first-class objects, meaning they can be assigned to variables, passed as arguments, and returned from other functions.
##### Explanation:
The print function is assigned to greet.
When calling greet('Hello, World!'), it behaves exactly like print('Hello, World!').

## 2.5. Data Types

1. **Research:**
   - Investigate Python’s dynamic typing.

Python is a dynamically typed language, which means:
You don’t need to declare the type of a variable before assigning a value.
A variable’s type can change at runtime based on the assigned value.

```python
x = 10        # x is an integer
print(type(x))  # Output: <class 'int'>

x = "Hello"   # Now x is a string
print(type(x))  # Output: <class 'str'>

x = 3.14      # Now x is a float
print(type(x))  # Output: <class 'float'>
```
2. **Exercise:**
 - Convert variables between types and observe the results:
     ```python
     num = '123'
     converted_num = int(num)
     print(converted_num, type(converted_num))
     ```

## 2.7. Variables

1. **Research:**
   - Understand how Python stores variables in memory.

In Python, variables are stored in memory using a concept called "references" rather than directly storing values. When you assign a value to a variable, Python:

  - Python uses reference counting to manage memory.
  - When a variable is assigned a value, Python creates an object and stores it in memory.
  - The variable name is just a reference (pointer) to that object.
  -  When an object is no longer referenced, Python’s garbage collector deletes it.

2. **Exercise:**
   - Assign values to variables, print them, and observe changes upon reassignment.

   Let's explore how Python stores variables in memory by assigning values, printing their memory addresses (id()), and observing changes when reassigned.

Step 1: Assigning Initial Values
```python
a = 10
b = "Hello"
c = [1, 2, 3]

print(f"a: {a}, Memory Address: {id(a)}")
print(f"b: {b}, Memory Address: {id(b)}")
print(f"c: {c}, Memory Address: {id(c)}")
```
Step 2: Reassigning Variables
```python
a = 20  # Integer reassignment
b = "World"  # String reassignment
c.append(4)  # Modifying the list (mutable object)

print("\nAfter Reassignment:")
print(f"a: {a}, Memory Address: {id(a)}")  # Different address
print(f"b: {b}, Memory Address: {id(b)}")  # Different address
print(f"c: {c}, Memory Address: {id(c)}")  # Same address (modified in place)
```
Observations:

Immutable Objects (Integers, Strings):

When reassigned (a = 20, b = "World"), Python creates a new object in memory.
The old object may be garbage collected if no other variable references it.
Mutable Objects (Lists, Dictionaries):

When modified (c.append(4)), the same memory address remains.
This means the list is updated in place.


## 2.8. Variable Names and Keywords

1. **Exercise:**
   - Try using reserved keywords as variable names and observe the errors.

Python will throw a SyntaxError, indicating that these words cannot be used as variable names.

2. **Fun Fact:**
   - Use `import keyword; print(keyword.kwlist)` to list all reserved keywords in Python.


## 2.9. Choosing the Right Variable Name

1. **Exercise:**
   - Rewrite a piece of code with meaningful variable names.

def multiply_numbers(first_number, second_number):
    product = first_number * second_number
    return product

num1 = 5
num2 = 10
result = multiply_numbers(num1, num2)
print(result)

2. **Challenge:**
   - Why is `total_price` a better name than `tp`?
   1. Readability
   2. Maintainability
   3. Avoiding Errors


## 2.10. Statements and Expressions

1. **Research:**
   - Differentiate between statements and expressions.
   Expression: -  A piece of code that evaluates to a value.
   	         - Expressions can be part of statements, but statements cannot be part of expressions.
               - Examples of expressions:
                 5 + 3 (evaluates to 8)
                 "Hello".upper() (evaluates to "HELLO")

      -Statement: A complete instruction that performs an action but does not return a value.
         Statement do not return any value.
         Examples of statements:
               x = 5 (assignment statement)
               print("Hello") (print statement)

2. **Exercise:**
   - Identify statements and expressions in this code:
     ```python
     x = 5 + 3
     print(x)
     ```
Expression:

5 + 3 → This is an expression because it evaluates to 8.

Statements:

x = 5 + 3 → This is an assignment statement (it assigns the result of the expression 5 + 3 to x).

print(x) → This is a function call statement (it performs an action by printing the value of x).


## 2.11. Order of Operations

1. **Fun Fact:**
   - Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction) rules.
2. **Exercise:**
   - Write expressions using multiple operators to explore Python’s order of operations.
     ```python
     result = 2 + 3 * 4 ** 2 / 8
     print(result)
     ```

## 2.12. Reassignment

### 2.12.1. Developing Your Mental Model of How Python Evaluates

1. **Exercise:**
   - Assign a value to a variable, reassign it, and observe the changes:
     ```python
     count = 10
     print(count)
     count = 20
     print(count)
     ```

## 2.13. Updating Variables

1. **Exercise:**
   - Increment and decrement variables using `+=` and `-=`.
     ```python
     score = 100
     score += 10
     print(score)
     score -= 5
     print(score)
     ```
# *Finished*