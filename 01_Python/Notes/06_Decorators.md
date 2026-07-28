# 06 - Decorators

> **Status:** 🟡 Draft v2.0

# Learning Objectives

After this chapter, you will be able to:

-   Explain what decorators are.
-   Understand why decorators exist.
-   Create your own decorators.
-   Understand how closures power decorators.
-   Apply decorators in real-world Python projects.

------------------------------------------------------------------------

# Prerequisites

-   Variables
-   Memory Model
-   Functions
-   LEGB Rule
-   Closures

------------------------------------------------------------------------

# 1. Why Do Decorators Exist?

Imagine you have 20 functions and you want to:

-   Log every function call
-   Measure execution time
-   Check user permissions
-   Retry failed operations

Copying the same code into every function would be repetitive.

**Decorators solve this by allowing you to add behavior without
modifying the original function.**

------------------------------------------------------------------------

# 2. What is a Decorator?

A decorator is a function that **takes another function as input,
extends its behavior, and returns a new function.**

------------------------------------------------------------------------

# 3. First Example

``` python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()
```

Output:

    Before function
    Hello!
    After function

------------------------------------------------------------------------

# Think First

**Question**

How can `greet()` print extra messages even though its code never
changed?

**Answer**

The original `greet` function is replaced by the function returned from
`decorator()`. The wrapper executes additional code before and after
calling the original function.

------------------------------------------------------------------------

# 4. How Decorators Work Internally

``` python
@decorator
def greet():
    pass
```

is equivalent to:

``` python
def greet():
    pass

greet = decorator(greet)
```

Python rewrites the function definition using the decorator.

------------------------------------------------------------------------

# 5. Closures and Decorators

Decorators work because the inner `wrapper()` function forms a
**closure** around `func`.

    wrapper
       │
       ▼
    func (captured variable)

The wrapper remembers which function it should call.

------------------------------------------------------------------------

# 6. Decorators with Arguments

``` python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

Using `*args` and `**kwargs` allows the decorator to work with almost
any function.

------------------------------------------------------------------------

# 7. Multiple Decorators

``` python
@decorator_one
@decorator_two
def greet():
    pass
```

Execution order:

1.  `decorator_two` is applied.
2.  `decorator_one` wraps the result.

------------------------------------------------------------------------

# Common Mistakes

-   Forgetting to return the wrapper.
-   Forgetting to return the original function's result.
-   Writing wrappers that don't accept `*args` and `**kwargs`.
-   Losing function metadata (use `functools.wraps` in production).

------------------------------------------------------------------------

# Frequently Asked Questions

### Q1. Do decorators modify the original function?

**Answer:** No. They return a new function that wraps the original one.

### Q2. Why are closures required?

**Answer:** The wrapper must remember the original function after the
decorator finishes executing.

### Q3. Why use `*args` and `**kwargs`?

**Answer:** They allow one decorator to support functions with different
parameter lists.

------------------------------------------------------------------------

# Interview Questions

## Beginner

### What is a decorator?

**Answer:** A decorator is a callable that accepts a function, adds
functionality, and returns another function.

------------------------------------------------------------------------

## Intermediate

### Explain what `@decorator` does internally.

**Answer:** Python executes `function = decorator(function)` after
creating the function object.

------------------------------------------------------------------------

## Advanced

### Why is `functools.wraps` recommended?

**Answer:** It preserves metadata such as the original function's name,
docstring, annotations, and module information.

------------------------------------------------------------------------

# Exercises

## Exercise 1 (Basic)

### Problem

Write a decorator that prints `"Starting..."` before calling a function.

### Hint

Create a wrapper inside the decorator.

### Solution

``` python
def start_message(func):
    def wrapper():
        print("Starting...")
        return func()
    return wrapper
```

------------------------------------------------------------------------

## Exercise 2 (Intermediate)

### Problem

Write a decorator that prints the execution time of a function.

### Hint

Use the `time` module.

### Solution

``` python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end-start:.6f} seconds")
        return result
    return wrapper
```

**Time Complexity:** O(1) (decorator overhead)

**Space Complexity:** O(1)

------------------------------------------------------------------------

## Exercise 3 (Interview Challenge)

### Problem

Create a decorator that checks whether a user is logged in before
executing a function.

### One Possible Solution

``` python
def login_required(func):
    logged_in = True

    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Access denied")
            return None
        return func(*args, **kwargs)

    return wrapper
```

### Explanation

The wrapper performs a check before delegating execution to the original
function.

------------------------------------------------------------------------

# Real-world Usage

Decorators are used extensively in:

-   FastAPI (`@app.get`, `@app.post`)
-   Flask routes
-   Unit testing
-   Authentication
-   Logging
-   Performance measurement
-   Retry mechanisms
-   Caching

------------------------------------------------------------------------

# Summary

-   Decorators extend function behavior.
-   They are built using closures.
-   `@decorator` is syntactic sugar.
-   Use `*args` and `**kwargs` for reusable decorators.
-   Decorators are common in modern Python frameworks.

------------------------------------------------------------------------

# Revision Checklist

-   [ ] I can explain decorators.
-   [ ] I know how `@decorator` works internally.
-   [ ] I can write a basic decorator.
-   [ ] I understand why closures are required.
-   [ ] I completed the exercises before reading the solutions.
