# 04 - Scope (LEGB Rule)

> **Status:** 🟡 Draft v2.0

# Learning Objectives

By the end of this chapter, you will be able to:

-   Explain what scope is.
-   Understand the LEGB rule.
-   Differentiate between local, enclosing, global, and built-in scopes.
-   Use `global` and `nonlocal` correctly.
-   Predict variable lookup in nested functions.

------------------------------------------------------------------------

# Prerequisites

-   Variables
-   Memory Model
-   Functions

------------------------------------------------------------------------

# 1. Why Does Scope Exist?

Imagine every variable in your program were visible everywhere. Two
functions could accidentally modify the same variable, causing difficult
bugs.

Scope limits where a variable is visible, making programs safer and
easier to understand.

------------------------------------------------------------------------

# 2. What is Scope?

A **scope** is the region of a program where a variable can be accessed.

``` python
def greet():
    message = "Hello"
    print(message)
```

`message` exists only inside `greet()`.

------------------------------------------------------------------------

# 3. The LEGB Rule

Python searches for variables in this order:

1.  **L -- Local**
2.  **E -- Enclosing**
3.  **G -- Global**
4.  **B -- Built-in**

Memory Trick:

> **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

------------------------------------------------------------------------

# 4. Local Scope

``` python
x = 100

def demo():
    x = 10
    print(x)

demo()
print(x)
```

Output

    10
    100

The local variable hides the global variable inside the function.

------------------------------------------------------------------------

# 5. Enclosing Scope

``` python
def outer():
    message = "Python"

    def inner():
        print(message)

    inner()

outer()
```

`inner()` finds `message` in the enclosing function.

------------------------------------------------------------------------

# 6. Global Scope

``` python
count = 0

def show():
    print(count)
```

Global variables can be read inside functions.

To modify them:

``` python
count = 0

def increment():
    global count
    count += 1
```

Use `global` sparingly because it makes code harder to maintain.

------------------------------------------------------------------------

# 7. Built-in Scope

Python automatically provides built-in functions.

``` python
print(len([1,2,3]))
```

`print()` and `len()` come from the built-in scope.

------------------------------------------------------------------------

# 8. The `nonlocal` Keyword

``` python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print(count)

outer()
```

`nonlocal` modifies a variable in the enclosing scope.

------------------------------------------------------------------------

# Common Mistakes

-   Thinking local variables exist after a function ends.
-   Using `global` when it is unnecessary.
-   Confusing `global` and `nonlocal`.
-   Shadowing built-in names like `list`, `str`, or `sum`.

------------------------------------------------------------------------

# Frequently Asked Questions

### Q1. What happens if Python cannot find a variable?

**Answer:** Python searches Local → Enclosing → Global → Built-in. If it
is not found anywhere, a `NameError` is raised.

### Q2. When should I use `global`?

**Answer:** Rarely. Prefer passing values as parameters and returning
results. Use `global` only when shared application state is truly
required.

### Q3. What is the difference between `global` and `nonlocal`?

**Answer:** `global` modifies a module-level variable, while `nonlocal`
modifies a variable in the nearest enclosing function.

------------------------------------------------------------------------

# Interview Questions

## Beginner

### 1. What is scope?

**Answer:** Scope defines where a variable is accessible in a program.

### 2. What does LEGB stand for?

**Answer:** Local, Enclosing, Global, Built-in.

------------------------------------------------------------------------

## Intermediate

### 3. Explain how Python resolves variable names.

**Answer:** Python searches scopes in LEGB order until it finds the
first matching name.

------------------------------------------------------------------------

## Advanced

### 4. Why is excessive use of `global` considered bad practice?

**Answer:** It increases coupling, makes debugging harder, and creates
hidden dependencies between different parts of the program.

------------------------------------------------------------------------

# Exercises

## Exercise 1 (Basic)

### Problem

Predict the output.

``` python
x = 5

def show():
    x = 10
    print(x)

show()
print(x)
```

### Hint

There are two different scopes.

### Solution

Output:

    10
    5

### Explanation

The local `x` exists only inside `show()`.

------------------------------------------------------------------------

## Exercise 2 (Intermediate)

### Problem

Predict the output.

``` python
x = 10

def change():
    global x
    x = 20

change()
print(x)
```

### Solution

Output:

    20

### Explanation

`global` tells Python to modify the module-level variable.

Time Complexity: **O(1)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

## Exercise 3 (Interview Challenge)

### Problem

Predict the output.

``` python
def outer():
    value = 100

    def inner():
        nonlocal value
        value += 50

    inner()
    return value

print(outer())
```

### Solution

Output:

    150

### Explanation

`nonlocal` updates the variable in the enclosing scope rather than
creating a new local variable.

Time Complexity: **O(1)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

# Real-world Usage

Scope is used everywhere:

-   FastAPI request handlers
-   TensorFlow callbacks
-   PyTorch training loops
-   Decorators
-   Closures
-   Configuration management

------------------------------------------------------------------------

# Summary

-   Scope controls variable visibility.
-   Python follows the LEGB rule.
-   Use `global` carefully.
-   Use `nonlocal` for enclosing scopes.
-   Understanding scope prevents subtle bugs.

------------------------------------------------------------------------

# Revision Checklist

-   [ ] I can explain LEGB.
-   [ ] I know when to use `global`.
-   [ ] I know when to use `nonlocal`.
-   [ ] I can predict variable lookup.
-   [ ] I solved the exercises without looking at the answers.
