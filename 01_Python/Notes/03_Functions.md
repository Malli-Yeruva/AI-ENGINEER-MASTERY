# 03 - Functions

> **Status:** 🟡 Draft v2.0

# Learning Objectives

After this chapter you will be able to:

-   Explain why functions exist.
-   Write and call functions.
-   Understand parameters, arguments, and return values.
-   Recognize local scope.
-   Design reusable, readable code.

------------------------------------------------------------------------

# Prerequisites

-   Variables
-   Python Memory Model

------------------------------------------------------------------------

# 1. Why Do Functions Exist?

Imagine writing the same 20 lines of code ten times. It becomes
difficult to maintain and easy to introduce bugs.

Functions solve this by allowing us to **write code once and reuse it
many times**.

Benefits: - Reusability - Readability - Easier debugging - Better
organization - Modularity

------------------------------------------------------------------------

# 2. Syntax

``` python
def greet(name):
    return f"Hello, {name}"
```

Calling a function:

``` python
message = greet("Mallikarjuna")
print(message)
```

------------------------------------------------------------------------

# 3. Parameters vs Arguments

``` python
def add(a, b):
    return a + b
```

-   `a` and `b` are **parameters**.
-   `10` and `20` below are **arguments**.

``` python
result = add(10, 20)
```

------------------------------------------------------------------------

# 4. Return Values

``` python
def square(x):
    return x * x
```

`return` sends a value back to the caller.

Without a return statement:

``` python
def demo():
    print("Hello")
```

Python returns `None`.

------------------------------------------------------------------------

# 5. Local Variables

``` python
def greet():
    message = "Hello"
    print(message)
```

`message` exists only while the function executes.

------------------------------------------------------------------------

# 6. Best Practices

-   Use meaningful function names.
-   Keep functions focused on one task.
-   Prefer returning values over printing.
-   Avoid long functions.

------------------------------------------------------------------------

# Frequently Asked Questions

### Q1. Why use functions instead of writing code repeatedly?

**Answer:** Functions eliminate duplication, improve readability, and
make maintenance easier.

### Q2. Why does a function return `None`?

**Answer:** Every Python function returns a value. If no `return`
statement is written, Python automatically returns `None`.

### Q3. What is the difference between `print()` and `return`?

**Answer:** `print()` displays output on the screen, while `return`
sends a value back to the caller so it can be reused.

------------------------------------------------------------------------

# Interview Questions

## Beginner

### 1. What is a function?

**Answer:** A function is a reusable block of code designed to perform a
specific task. It improves modularity and reduces code duplication.

------------------------------------------------------------------------

### 2. What is the difference between parameters and arguments?

**Answer:** Parameters are variables defined in a function definition.
Arguments are actual values passed during the function call.

------------------------------------------------------------------------

## Intermediate

### 3. What happens internally when a function is called?

**Answer:** Python creates a new stack frame, assigns arguments to
parameters, executes the function body, returns the result, and removes
the stack frame.

------------------------------------------------------------------------

## Advanced

### 4. Why are small functions preferred?

**Answer:** Small functions are easier to test, debug, reuse, and
maintain. They also follow the Single Responsibility Principle.

------------------------------------------------------------------------

# Exercises

## Exercise 1 (Basic)

### Problem

Write a function that returns the cube of a number.

### Solution

``` python
def cube(x):
    return x ** 3
```

### Explanation

The exponent operator `**` raises the value to the third power.

------------------------------------------------------------------------

## Exercise 2 (Intermediate)

### Problem

Write a function that returns the larger of two numbers.

### Solution

``` python
def maximum(a, b):
    if a > b:
        return a
    return b
```

### Time Complexity

O(1)

### Space Complexity

O(1)

------------------------------------------------------------------------

## Exercise 3 (Advanced)

### Problem

Write a function that returns the factorial of a positive integer
without using recursion.

### Solution

``` python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Dry Run

Input: 5

result = 1

2 → 2

3 → 6

4 → 24

5 → 120

Output: 120

### Time Complexity

O(n)

### Space Complexity

O(1)

------------------------------------------------------------------------

# Real-world Usage

Functions are heavily used in:

-   Machine Learning pipelines
-   Data preprocessing
-   FastAPI route handlers
-   TensorFlow models
-   OpenCV image processing
-   Utility libraries

------------------------------------------------------------------------

# Summary

-   Functions promote reuse.
-   Parameters receive data.
-   Arguments provide data.
-   `return` gives data back.
-   Functions improve software quality.

------------------------------------------------------------------------

# Revision Checklist

-   [ ] I can write a function.
-   [ ] I know parameters vs arguments.
-   [ ] I understand return values.
-   [ ] I can answer the interview questions.
-   [ ] I solved all exercises without looking at the answers.
