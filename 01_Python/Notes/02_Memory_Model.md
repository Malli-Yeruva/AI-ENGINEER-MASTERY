# 02 - Python Memory Model

> **Status:** 🟡 Draft v1.0

## Learning Objectives

After this chapter you should understand:

-   How Python stores objects
-   What references are
-   The difference between identity and equality
-   Mutable vs immutable objects
-   Why understanding memory prevents bugs

------------------------------------------------------------------------

# 1. Why Learn the Memory Model?

Many Python bugs come from not understanding references.

Example:

``` python
a = [1, 2]
b = a
b.append(3)

print(a)
```

Why did `a` change?

The answer is the memory model.

------------------------------------------------------------------------

# 2. Core Idea

Everything in Python is an object.

Variables do **not** contain data.

Variables point to objects.

    a --------> [1,2]

------------------------------------------------------------------------

# 3. References

``` python
x = 10
y = x
```

Memory:

    x --\
         ---> 10
    y --/

Both names reference the same object.

------------------------------------------------------------------------

# 4. Identity vs Equality

``` python
a = [1,2]
b = a
c = [1,2]
```

-   `a == c` → True (same value)
-   `a is c` → False (different objects)
-   `a is b` → True (same object)

------------------------------------------------------------------------

# 5. Mutable vs Immutable

## Immutable

-   int
-   float
-   bool
-   str
-   tuple

Changing an immutable value creates a new object.

``` python
x = 10
x = 20
```

------------------------------------------------------------------------

## Mutable

-   list
-   dict
-   set

The same object can be modified.

``` python
nums = [1,2]
nums.append(3)
```

------------------------------------------------------------------------

# 6. id()

``` python
x = 10
print(id(x))
```

`id()` returns the identity of an object.

Useful for understanding references during debugging.

------------------------------------------------------------------------

# 7. Common Mistakes

-   Using `is` instead of `==`
-   Assuming assignment copies objects
-   Forgetting lists are mutable

------------------------------------------------------------------------

# 8. Interview Questions

1.  What is a reference?
2.  Difference between `==` and `is`?
3.  What is object identity?
4.  Mutable vs immutable?
5.  Why do lists behave differently from integers?

------------------------------------------------------------------------

# 9. Exercises

### Exercise 1

Predict:

``` python
a = [1,2]
b = a
b.append(3)

print(a)
print(b)
```

### Exercise 2

Predict:

``` python
x = 10
y = x
x = 20

print(x)
print(y)
```

Explain why.

------------------------------------------------------------------------

# 10. Summary

-   Everything is an object.
-   Variables reference objects.
-   `==` compares values.
-   `is` compares identity.
-   Mutable objects change in place.
-   Immutable objects create new objects.

------------------------------------------------------------------------

# Revision Checklist

-   [ ] I know the difference between `==` and `is`.
-   [ ] I understand references.
-   [ ] I know mutable vs immutable.
-   [ ] I can explain why list assignment shares the same object.
