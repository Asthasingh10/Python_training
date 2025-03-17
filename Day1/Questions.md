# Variables, Statements, and Expressions: A Learning Task

## 2.1. Introduction

### 2.1.1. Learning Goals

By the end of this task, students should be able to:

- Understand the basics of variables, expressions, and statements in Python.
- Differentiate between data types and apply type conversions.
- Properly name variables following Python conventions.
- Grasp the flow of execution through function calls and expressions.
- Update and reassign variables effectively.

### 2.1.2. Objectives

- Identify values and their data types.
- Perform operations using different operators.
- Understand function calls and their role in expressions.
- Explore Python's order of operations.
- Practice variable reassignment and updating.

---

## 2.2. Values and Data Types

1. **Research:**
   - What is a value in Python?
   - Identify different data types in Python (e.g., integers, floats, strings, booleans).
2. **Fun Fact:**
   - Python is dynamically typed — you don’t need to declare the type of a variable when you create one.
3. **Exercise:**
   - Write a program that:
     - Assigns different values to variables.
     - Prints the type of each variable.
   - Example:
     ```python
     x = 42
     y = 3.14
     z = 'Hello'
     print(type(x), type(y), type(z))
     ```

## 2.3. Operators and Operands

1. **Research:**
   - Learn about arithmetic, comparison, and logical operators.
2. **Fun Fact:**
   - Python uses `//` for floor division, ensuring the result is always an integer.
3. **Exercise:**
   - Create a Python script that demonstrates:
     - Addition, subtraction, multiplication, and division.
     - Comparisons between numbers.
     - Logical operations like `and`, `or`, `not`.

## 2.4. Function Calls

### 2.4.1. Function Calls as Part of Complex Expressions

1. **Fun Fact:**
   - In Python, functions are first-class objects, meaning they can be assigned to variables and passed as arguments.
2. **Exercise:**
   - Write a program that uses built-in functions inside expressions:
     ```python
     numbers = [5, 3, 8, 1]
     print(max(numbers) - min(numbers))
     ```

### 2.4.2. Functions are Objects; Parentheses Invoke Functions

1. **Exercise:**
   - Assign a function to a variable, then call the function using the new variable:
     ```python
     greet = print
     greet('Hello, World!')
     ```

## 2.5. Data Types

1. **Research:**
   - Investigate Python’s dynamic typing.
2. **Exercise:**
   - Create variables of different types and print their types:
     ```python
     a = 10
     b = 'Python'
     c = 3.14
     print(type(a), type(b), type(c))
     ```

## 2.6. Type Conversion Functions

1. **Fun Fact:**
   - Python provides built-in functions like `int()`, `float()`, and `str()` to handle type conversions.
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
2. **Exercise:**
   - Assign values to variables, print them, and observe changes upon reassignment.

## 2.8. Variable Names and Keywords

1. **Exercise:**
   - Try using reserved keywords as variable names and observe the errors.
2. **Fun Fact:**
   - Use `import keyword; print(keyword.kwlist)` to list all reserved keywords in Python.

## 2.9. Choosing the Right Variable Name

1. **Exercise:**
   - Rewrite a piece of code with meaningful variable names.
2. **Challenge:**
   - Why is `total_price` a better name than `tp`?

## 2.10. Statements and Expressions

1. **Research:**
   - Differentiate between statements and expressions.
2. **Exercise:**
   - Identify statements and expressions in this code:
     ```python
     x = 5 + 3
     print(x)
     ```

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

## Submission Guidelines:

- Upload all Python files in a zip folder.
- Ensure your code is well-commented.
- Include a README file explaining your submission.

Happy coding! 🚀
