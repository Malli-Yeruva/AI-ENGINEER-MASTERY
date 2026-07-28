# 05 - Closures

> **Status:** 🟡 Draft v2.0

# Learning Objectives

By the end of this chapter, you will:

-   Understand what a closure is.
-   Explain why closures exist.
-   Understand enclosing scope.
-   Predict how closures preserve state.
-   Compare closures with classes.
-   Use closures in real-world applications.

------------------------------------------------------------------------

# Prerequisites

-   Variables
-   Memory Model
-   Functions
-   LEGB Rule

------------------------------------------------------------------------

# Why Do Closures Exist?

Sometimes a function needs to **remember information** even after the
outer function has finished executing.

Closures solve this problem by allowing an inner function to remember
variables from its enclosing scope.

------------------------------------------------------------------------

# What is a Closure?

A closure is a function that:

1.  Is defined inside another function.
2.  Captures variables from the enclosing scope.
3.  Continues to access those variables even after the outer function
    has returned.

------------------------------------------------------------------------

# Example

``` python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()

print(c())   # 1
print(c())   # 2
print(c())   # 3
```

------------------------------------------------------------------------

# Think First

**Question**

Why does `count` continue increasing even though `counter()` has already
finished?

Pause and think before reading the answer.

------------------------------------------------------------------------

# Answer

The returned function `increment` keeps a reference to the variable
`count`.

Since the closure still references `count`, Python keeps that variable
alive.

------------------------------------------------------------------------

# Memory Diagram

    counter()

    count = 0
       ▲
       │
    increment()
       │
       ▼

    Closure remembers count

------------------------------------------------------------------------

# Behind the Scenes

Python stores references to captured variables inside the function
object's closure.

These captured variables are called **free variables**.

They remain alive until the closure itself is destroyed.

------------------------------------------------------------------------

# Closures vs Normal Functions

  Normal Function         Closure
  ----------------------- ------------------------------
  No persistent state     Remembers state
  Independent execution   Captures enclosing variables
  No stored context       Stores context

------------------------------------------------------------------------

# Closures vs Classes

  Closure                Class
  ---------------------- ------------------------------
  Lightweight            Better for complex state
  Small private state    Large structured state
  Great for decorators   Great for large applications

------------------------------------------------------------------------

# Common Mistakes

-   Forgetting `nonlocal` when modifying captured variables.
-   Assuming the outer variable disappears immediately.
-   Confusing closures with recursion.

------------------------------------------------------------------------

# Frequently Asked Questions

### Q1. Does the outer function continue running?

**Answer:** No. The outer function finishes, but captured variables
remain alive because the closure references them.

### Q2. What are free variables?

**Answer:** Variables used by the inner function that come from the
enclosing scope.

### Q3. Can two closures have different states?

**Answer:** Yes.

``` python
c1 = counter()
c2 = counter()
```

Each closure maintains its own independent `count`.

------------------------------------------------------------------------

# Interview Questions

## Beginner

### What is a closure?

**Answer:** A closure is an inner function that remembers variables from
its enclosing scope even after the outer function has returned.

------------------------------------------------------------------------

## Intermediate

### Why are closures useful?

**Answer:** They preserve state without using global variables or
classes, making code cleaner and more modular.

------------------------------------------------------------------------

## Advanced

### How does Python keep closure variables alive?

**Answer:** Python stores references to captured variables in the
function object's closure, preventing them from being garbage-collected
while the closure exists.

------------------------------------------------------------------------

# Exercises

## Exercise 1 (Basic)

### Problem

Create a closure that always greets the same person.

### Hint

Pass the person's name to the outer function.

### Solution

``` python
def greeter(name):
    def greet():
        return f"Hello {name}"
    return greet
```

------------------------------------------------------------------------

## Exercise 2 (Intermediate)

### Problem

Create a multiplier closure.

``` python
double = multiplier(2)
print(double(10))
```

Output:

    20

### Solution

``` python
def multiplier(factor):
    def multiply(number):
        return factor * number
    return multiply
```

**Time Complexity:** O(1)

**Space Complexity:** O(1)

------------------------------------------------------------------------

## Exercise 3 (Interview Challenge)

### Problem

Implement a counter closure that increments every time it is called.

### Solution

``` python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

### Dry Run

    counter()

    count = 0

    Call 1 -> 1
    Call 2 -> 2
    Call 3 -> 3

**Time Complexity:** O(1)

**Space Complexity:** O(1)

------------------------------------------------------------------------

# Real-world Usage

Closures are widely used in:

-   Decorators
-   Callback functions
-   Event handlers
-   Function factories
-   Machine Learning preprocessing pipelines
-   Configuration wrappers

------------------------------------------------------------------------

# Summary

-   Closures remember variables from their enclosing scope.
-   They preserve state across function calls.
-   `nonlocal` modifies captured variables.
-   Decorators are built using closures.

------------------------------------------------------------------------

# Revision Checklist

-   [ ] I can explain what a closure is.
-   [ ] I understand why closures exist.
-   [ ] I know what free variables are.
-   [ ] I know when to use `nonlocal`.
-   [ ] I solved all exercises before reading the solutions.
