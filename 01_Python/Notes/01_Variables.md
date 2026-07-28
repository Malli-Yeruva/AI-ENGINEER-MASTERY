# 01 - Variables

> **Status:** 🟡 Draft v1.0

## Learning Objectives

-   Explain what a variable is.
-   Understand variables vs objects.
-   Predict assignment behavior.
-   Avoid common mistakes.

## Why Do Variables Exist?

Variables give meaningful names to objects in memory.

A variable is **not a box**.

A variable is a **reference (name)** to an object.

## Mental Model

    price ---------> 100

The name points to the object.

## Assignment

``` python
x = 10
```

Conceptually:

1.  Create/reuse object `10`
2.  Bind `x` to it

## Variables vs Objects

``` python
x = 10
y = x
```

    x --\
          ---> 10
    y --/

## Reassignment

``` python
x = 10
y = x
x = 20
```

    x ---> 20
    y ---> 10

## Dynamic Typing

``` python
x = 10
x = "hello"
x = [1,2,3]
```

The variable name stays; the referenced object changes.

## Common Mistakes

-   Thinking variables store values.
-   Confusing assignment with copying.
-   Poor naming.

## Interview Questions

1.  What is a variable?
2.  What happens during assignment?
3.  What is dynamic typing?
4.  Variables vs objects?

## Exercises

Predict:

``` python
x = 10
y = x
x = 20

print(x)
print(y)
```

## Summary

-   Variables are names.
-   Objects hold data.
-   Assignment binds a name to an object.
-   Python is dynamically typed.

## Revision Checklist

-   [ ] I understand references.
-   [ ] I can explain assignment.
-   [ ] I can predict reassignment.
