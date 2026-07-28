
# Chapter 8 — `**kwargs`, Packing & Unpacking (Professional Edition)

> **Prerequisites:** Variables & Memory Model, Functions, `*args`

---

# 1. Why does `**kwargs` exist?

Imagine Python only supported this:

```python
def greet(name, age):
    ...
```

Every time you wanted to add a new optional argument, you would have to modify the function.

`**kwargs` solves this by allowing a function to accept **any number of keyword arguments**.

Example:

```python
def greet(**kwargs):
    print(kwargs)

greet(name="Alex", age=25, city="Hyderabad")
```

Python automatically creates:

```python
{
    "name": "Alex",
    "age": 25,
    "city": "Hyderabad"
}
```

---

# 2. Mental Model

Variables do **not** store objects.

```
kwargs
   │
   ▼
+------------------------------+
| Dictionary Object            |
|------------------------------|
| name  -> Alex                |
| age   -> 25                  |
| city  -> Hyderabad           |
+------------------------------+
```

`kwargs` is only a **reference**.

---

# 3. Behind the Scenes (Execution Trace)

Function call:

```python
demo(name="Alex", age=25)
```

Python performs:

```
Caller
  │
  ▼
Parse keyword arguments
  │
  ▼
Create dictionary
  │
  ▼
Bind local variable kwargs
  │
  ▼
Execute function body
```

---

# 4. CPython Intuition

Conceptually, CPython:

1. Creates a new stack frame.
2. Allocates local variables.
3. Matches named parameters.
4. Places unmatched keyword arguments into a new dictionary.
5. Binds that dictionary to `kwargs`.
6. Executes the function.

You don't need to memorize CPython internals, but this model explains Python's behavior.

---

# 5. `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Accepts | Positional | Keyword |
| Stored as | Tuple | Dictionary |
| Order | By position | By key |
| Mutable | Tuple (immutable) | Dict (mutable) |
| Definition | `*args` | `**kwargs` |
| Call | `*tuple` | `**dict` |

---

# 6. Mutation vs Rebinding

Mutation:

```python
kwargs["country"] = "India"
```

```
kwargs
   │
   ▼
Dictionary
   │
(add key)
```

Rebinding:

```python
kwargs = {"country": "India"}
```

```
kwargs
   │
   ▼
New Dictionary
```

Mutation changes the object.

Rebinding changes the reference.

---

# 7. Packing vs Unpacking

## Packing

```python
def demo(*args, **kwargs):
    ...
```

```
10 20 30
   │
   ▼
args = (10,20,30)

name="Alex"
age=25
   │
   ▼
kwargs={"name":"Alex","age":25}
```

## Unpacking

```python
numbers=(10,20,30)
person={"name":"Alex","age":25}

demo(*numbers, **person)
```

Equivalent to:

```python
demo(10,20,30,name="Alex",age=25)
```

---

# 8. Python Argument Binding Algorithm

Python binds arguments in this order:

1. Positional parameters
2. Remaining positional → `*args`
3. Keyword-only parameters
4. Remaining keyword → `**kwargs`

Remember this order—it explains most function-call behavior.

---

# 9. Keyword-only Parameters

```python
def demo(a, *args, b=100):
    print(b)
```

Valid:

```python
demo(10,20,b=999)
```

Invalid:

```python
demo(10,20,999)
```

---

# 10. Real-world Examples

## Flask

```python
@app.route("/")
def home():
    ...
```

Frameworks internally forward unknown arguments using `*args` and `**kwargs`.

## FastAPI

Dependency injection frequently forwards keyword arguments into your endpoint.

## PyTorch

```python
class MyModel(nn.Module):
    def forward(self, *args, **kwargs):
        ...
```

Allows flexible model APIs.

## TensorFlow / Keras

Many layers accept `**kwargs` so new options can be added without breaking old code.

## Pandas

Functions often accept `**kwargs` to forward configuration to lower-level APIs.

---

# 11. Common Mistakes

1. Thinking `kwargs` is the dictionary itself.
2. Forgetting `**kwargs` must come last.
3. Confusing mutation with rebinding.
4. Assuming tuples unpack automatically.
5. Passing a list with `**`.

---

# 12. Interview Questions

1. Difference between `*args` and `**kwargs`?
2. Why is `kwargs` a dictionary?
3. Why must `**kwargs` appear last?
4. Packing vs unpacking?
5. Mutation vs rebinding?
6. Why do decorators use `*args, **kwargs`?
7. What is a keyword-only parameter?
8. Can `**` unpack a list? Why not?
9. What happens if dictionary keys don't match parameter names?
10. What error occurs if required parameters are missing?

---

# 13. Exercises

## Basic

1. Write a function that prints all keyword arguments.
2. Count the number of keys in `kwargs`.
3. Add a new key to `kwargs`.

## Intermediate

4. Combine positional parameters, `*args`, and `**kwargs`.
5. Forward `**kwargs` to another function.

## Advanced

6. Build a decorator using `*args` and `**kwargs`.
7. Merge two dictionaries using `**`.

---

# 14. Mini Project

Build a logging decorator:

```python
@log_calls
def predict(image, threshold=0.5):
    ...
```

Requirements:

- Print function name.
- Print positional arguments.
- Print keyword arguments.
- Print return value.

Use `*args` and `**kwargs` internally.

---

# 15. One-page Cheat Sheet

```
Definition
----------
*args     -> tuple
**kwargs  -> dictionary

Packing
-------
def f(*args, **kwargs)

Unpacking
---------
f(*tuple_obj, **dict_obj)

Argument Binding
----------------
1. Positional
2. *args
3. Keyword-only
4. **kwargs

Mutation
--------
kwargs["x"]=1

Rebinding
---------
kwargs={"x":1}
```

---

# Chapter Summary

- `**kwargs` collects extra keyword arguments into a dictionary.
- `*args` and `**kwargs` are symmetric: they **pack** in function definitions and **unpack** in function calls.
- Dictionaries are mutable; variables are references.
- Python follows a fixed argument binding algorithm.
- These concepts are the foundation for decorators, FastAPI, Flask, TensorFlow, PyTorch, and many production APIs.
