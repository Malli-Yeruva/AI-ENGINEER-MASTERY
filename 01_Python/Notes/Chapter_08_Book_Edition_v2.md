# Chapter 8 – **kwargs, Packing & Unpacking (Book Edition)

> **Note:** This is the blueprint and first complete edition of the chapter. Every interview question includes an answer, every exercise includes a solution, and the mini-project is fully solved.

# 1. Why `**kwargs` Exists
Python functions often need to accept optional configuration without changing their signature every time a new option is added.

```python
def connect(**kwargs):
    print(kwargs)
```

Calling:

```python
connect(host="localhost", port=5432, ssl=True)
```

Internally becomes:

```python
{
    "host":"localhost",
    "port":5432,
    "ssl":True
}
```

---
# 2. Mental Model

Variables hold **references**, not objects.

```
kwargs
  |
  v
+--------------------------+
| Dictionary Object        |
| host -> localhost        |
| port -> 5432             |
| ssl  -> True             |
+--------------------------+
```

---
# 3. Packing vs Unpacking

Definition:

```python
def f(*args, **kwargs):
    ...
```

Call:

```python
nums=(1,2)
cfg={"x":10}

f(*nums, **cfg)
```

Equivalent to:

```python
f(1,2,x=10)
```

---
# 4. Argument Binding Algorithm

1. Required positional parameters.
2. Remaining positional → `*args`
3. Keyword-only parameters.
4. Remaining keywords → `**kwargs`

---
# 5. Comparison Table

| Feature | *args | **kwargs |
|---|---|---|
| Stores | Tuple | Dictionary |
| Receives | Positional | Keyword |
| Mutable | No | Yes |
| Used in definition | Pack | Pack |
| Used in call | Unpack | Unpack |

---
# 6. Real-world Usage

- Flask decorators forward request data.
- FastAPI dependency injection forwards keyword arguments.
- PyTorch `forward(*args, **kwargs)` enables flexible models.
- TensorFlow layers accept `**kwargs` for future compatibility.

---
# 7. Interview Questions (with Answers)

### Q1. What is **kwargs?
**Answer:** A parameter that collects extra keyword arguments into a dictionary.

### Q2. Difference between *args and **kwargs?
**Answer:** `*args` stores positional arguments in a tuple. `**kwargs` stores keyword arguments in a dictionary.

### Q3. Why dictionary?
**Answer:** Keyword arguments are name-value pairs. Dictionaries naturally represent key-value mappings.

### Q4. Why must **kwargs be last?
**Answer:** Python first binds declared parameters. Whatever keyword arguments remain are collected by `**kwargs`.

### Q5. Mutation vs rebinding?
**Answer:** Mutation changes the existing dictionary. Rebinding makes the variable reference a new dictionary.

### Q6. What does `**person` do?
**Answer:** Converts dictionary keys into parameter names and values into argument values.

### Q7. Can `**` unpack a list?
**Answer:** No. `**` requires a mapping (dictionary-like object).

### Q8. Why do decorators use `*args, **kwargs`?
**Answer:** To accept and forward any function signature without knowing it beforehand.

### Q9. Packing vs unpacking?
**Answer:** Packing happens in the function definition. Unpacking happens in the function call.

### Q10. What happens if a required parameter is missing?
**Answer:** Python raises `TypeError`.

---
# 8. Exercises (with Solutions)

### Exercise 1
Write a function accepting any keyword arguments.

Solution:

```python
def show(**kwargs):
    print(kwargs)
```

### Exercise 2
Print only the keys.

Solution:

```python
def show(**kwargs):
    for k in kwargs:
        print(k)
```

### Exercise 3
Count keyword arguments.

Solution:

```python
def show(**kwargs):
    return len(kwargs)
```

### Exercise 4
Add `"country":"India"`.

Solution:

```python
kwargs["country"]="India"
```

### Exercise 5
Forward keyword arguments.

Solution:

```python
def inner(**kwargs):
    print(kwargs)

def outer(**kwargs):
    inner(**kwargs)
```

### Exercise 6
Combine positional and keyword arguments.

Solution:

```python
def demo(a,*args,**kwargs):
    print(a,args,kwargs)
```

### Exercise 7
Unpack tuple and dictionary.

Solution:

```python
nums=(1,2)
cfg={"x":10}
demo(*nums,**cfg)
```

### Exercise 8
Explain why this fails.

```python
demo(**[1,2])
```

Solution:
`**` only works with mappings (dictionary-like objects).

---
# 9. Mini Project (Complete Solution)

## Problem

Create a decorator that logs every function call.

## Solution

```python
def log_calls(func):

    def wrapper(*args, **kwargs):

        print("="*30)
        print("Function:", func.__name__)
        print("Positional:", args)
        print("Keyword:", kwargs)

        result = func(*args, **kwargs)

        print("Returned:", result)
        print("="*30)

        return result

    return wrapper


@log_calls
def multiply(a, b, scale=1):
    return a * b * scale


multiply(3, 4, scale=2)
```

Output

```
==============================
Function: multiply
Positional: (3, 4)
Keyword: {'scale': 2}
Returned: 24
==============================
```

Why it works:
- `wrapper(*args, **kwargs)` accepts any function signature.
- `func(*args, **kwargs)` forwards arguments unchanged.
- The decorator is reusable for almost every function.

---
# 10. Cheat Sheet

```
Definition
----------
*args  -> tuple
**kwargs -> dictionary

Definition
----------
def f(*args, **kwargs)

Call
----
f(*tuple_obj, **dict_obj)

Mutation
--------
kwargs["x"]=1

Rebinding
---------
kwargs={"x":1}

Binding Order
-------------
1. Positional
2. *args
3. Keyword-only
4. **kwargs
```

# Summary

You should now be able to explain not only what `**kwargs` does, but why Python designed it this way and how it enables decorators and modern frameworks.
