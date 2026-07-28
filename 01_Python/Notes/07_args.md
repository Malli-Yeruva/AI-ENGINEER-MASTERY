# 07 - \*args (Variable Positional Arguments)

> **Status:** 🟡 Draft v2.0

# Learning Objectives

By the end of this chapter, you will:

-   Understand why `*args` exists.
-   Differentiate between normal parameters and `*args`.
-   Explain how Python packs positional arguments into a tuple.
-   Use `*args` in real-world code.
-   Answer common interview questions on `*args`.

------------------------------------------------------------------------

# Prerequisites

-   Variables
-   Functions
-   Parameters & Arguments
-   Decorators

------------------------------------------------------------------------

# 1. Why Does `*args` Exist?

Imagine writing separate functions for different numbers of inputs.

``` python
add2(a, b)
add3(a, b, c)
add4(a, b, c, d)
```

This doesn't scale.

`*args` lets a function accept **any number of positional arguments**.

------------------------------------------------------------------------

# 2. Syntax

``` python
def add(*args):
    print(args)

add(10, 20, 30)
```

Output

    (10, 20, 30)

Notice that `args` is a **tuple**.

------------------------------------------------------------------------

# 3. How Python Works Internally

When you call:

``` python
add(1, 2, 3)
```

Python conceptually performs:

    args = (1, 2, 3)

The `*` tells Python to **pack** all remaining positional arguments into
a tuple.

------------------------------------------------------------------------

# Memory Diagram

    Call

    add(10,20,30)

            │
            ▼

    args ─────► (10,20,30)

------------------------------------------------------------------------

# 4. Iterating Over `args`

``` python
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Example:

``` python
print(add(10, 20, 30))
```

Output

    60

------------------------------------------------------------------------

# 5. `*args` with Normal Parameters

``` python
def introduce(name, *skills):
    print(name)
    print(skills)
```

    introduce("Alex", "Python", "SQL", "AWS")

Output

    Alex
    ('Python', 'SQL', 'AWS')

------------------------------------------------------------------------

# 6. Packing vs Unpacking

Packing:

``` python
def demo(*args):
    print(args)
```

Unpacking:

``` python
numbers = (1, 2, 3)
print(*numbers)
```

------------------------------------------------------------------------

# Common Mistakes

-   Thinking `args` is a list (it is a tuple).
-   Forgetting to iterate over `args`.
-   Using `*args` when a fixed number of parameters is sufficient.

------------------------------------------------------------------------

# Frequently Asked Questions

### Q1. Is the name `args` mandatory?

**Answer:** No. Only the `*` has special meaning. These are equivalent:

``` python
def f(*args):
    pass

def f(*numbers):
    pass
```

### Q2. Why is `args` a tuple?

**Answer:** Tuples are immutable and lightweight, making them suitable
for storing an arbitrary number of positional arguments.

### Q3. Can I have normal parameters before `*args`?

**Answer:** Yes.

``` python
def func(a, b, *args):
    pass
```

------------------------------------------------------------------------

# Interview Questions

## Beginner

### 1. What is `*args`?

**Answer:** `*args` allows a function to accept any number of positional
arguments. Python packs them into a tuple.

------------------------------------------------------------------------

## Intermediate

### 2. Explain packing in Python.

**Answer:** Packing collects multiple positional arguments into a single
tuple parameter using `*`.

------------------------------------------------------------------------

## Advanced

### 3. When would you use `*args` in production code?

**Answer:** It is useful when building decorators, logging utilities,
wrappers, plugin systems, or APIs where the number of positional
arguments is unknown in advance.

------------------------------------------------------------------------

# Exercises

## Exercise 1 (Basic)

### Problem

Write a function that returns the sum of all numbers passed to it.

### Hint

Loop through `args`.

### Solution

``` python
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total
```

Time Complexity: **O(n)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

## Exercise 2 (Intermediate)

### Problem

Write a function that returns the largest number from `*args`.

### Solution

``` python
def find_max(*args):
    largest = args[0]
    for num in args:
        if num > largest:
            largest = num
    return largest
```

Time Complexity: **O(n)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

## Exercise 3 (Advanced)

### Problem

Write a function to find the second largest number.

### Solution

``` python
def second_largest(*args):
    if len(args) < 2:
        return None

    largest = float("-inf")
    second = float("-inf")

    for num in args:
        if num > largest:
            second = largest
            largest = num
        elif second < num < largest:
            second = num

    return None if second == float("-inf") else second
```

### Explanation

-   Track the largest and second-largest values.
-   Update both carefully when a new maximum is found.
-   The `elif second < num < largest` condition prevents duplicates from
    replacing the second-largest value.

Time Complexity: **O(n)**

Space Complexity: **O(1)**

------------------------------------------------------------------------

# Real-world Usage

`*args` is commonly used in:

-   Decorators
-   Logging frameworks
-   FastAPI middleware
-   Wrapper functions
-   Utility libraries
-   Machine Learning helper functions

------------------------------------------------------------------------

# Summary

-   `*args` accepts any number of positional arguments.
-   Python packs them into a tuple.
-   The name `args` is a convention, not a keyword.
-   `*args` is widely used with decorators and reusable APIs.

------------------------------------------------------------------------

# Revision Checklist

-   [ ] I know why `*args` exists.
-   [ ] I understand packing.
-   [ ] I know `args` is a tuple.
-   [ ] I can solve the exercises without looking at the solutions.
-   [ ] I can explain real-world uses of `*args`.
