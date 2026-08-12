# Python Notes

This file is the initial Python notes document for the repository. Keep adding topic notes here, or move them into `01_Python/Notes/` as the repo grows.

---

Variables never contain values or store values 
variables references to objects
everythin in python is an object
everything has identity , type ,value
IMMUTABLE - CAN'T CHANGE AFTER CREATION  EX:INT,FLOAT,STRING,BOOL,TUPLE,FROZEN SET. HERE NEW STRING WILL BE CREATED FOR NEW CHANGES 
MUTABLE - CAN CHANGE ONCE CREATION.   , LIST ,DICT,SET. HERE NO NEW LIST IS CREATED
lIST- ORDERED ,Mutable ,duplicates allowed
tuple- immutable list -faster ,hashable,safe
dict - key value pairs
set - stores unique values  ,perfect for duplicates,fast lookup 
== checks whether two objects have the same value
is checks whethere two variables refer to the exact same object in mmemory

why dictonaries are fast because it is implemented using hash table . When a key is inserted:
Python computes the key's hash.
The hash determines where to store the value.
When searching, Python computes the same hash and jumps directly to the location.

Hashing is a technique used in data structures that efficiently stores and retrieves data in a way that allows for quick access.

Hashing

A technique that converts data into a fixed-size integer (hash value) so it can be stored and retrieved efficiently.

Hash Function

A function that takes an object and returns its hash value.

hash()

Python's built-in function that returns the hash of a hashable object.

Notice the difference:

Hash Value → Integer returned by hash()
Bucket → Memory location in the hash table

An object is hashable if:

It has a hash value.
That hash value never changes during its lifetime.
It supports equality comparison (==).

Why are dictionaries fast?

Because they use a hash table, which computes the hash of a key and uses it to quickly locate the associated value, giving average-case O(1) lookup, insertion, and deletion

Multiple keys can map to the same bucket, and the hash table has a collision-resolution strategy.

Why are tuples immutable?  - Tuples are immutable because once created, their contents cannot change.

Concept   	Meaning
Variable	Reference to an object
Object	    Lives in memory
==	        Compare values
is	        Compare object identity
Integer     Caching	Python reuses small integer  objects (typically -5 to 256)
String Interning	Python may reuse immutable string objects
Best Practice	Use == for values, is for identity (primarily None)



Python stores the default parameter once, when the function is defined, not every time it's called.

Why do we use None instead of [] as a default parameter?

A strong answer is:

"Default parameter values are evaluated only once when the function is defined. If the default value is a mutable object like a list or dictionary, that same object is shared across function calls. Using None and creating a new list inside the function ensures each call gets its own fresh list."


def add_item(item, my_list=[]):

Answer:

Because

✅ Lists are mutable.

↓

Python stores the default list once.

↓

Every call references the same list.

↓

The list gets modified.

↓

Next call sees the modified list.

Notice?

This is not a "functions" topic.

It's actually

Functions
Memory
References
Mutability

working together.


Code Pattern	Complexity
a[5]	O(1)
Dictionary lookup	O(1)
Single loop	O(n)
List search	O(n)
Two separate loops	O(n)
Nested loops	O(n²)
n + n²	O(n²)
2n	O(n)
100n	O(n)


| Operation                   | Time Complexity | Why                                      |
| --------------------------- | --------------- | ---------------------------------------- |
| `arr[i]`                    | O(1)            | Direct index access                      |
| `len(arr)`                  | O(1)            | Stored length                            |
| Dictionary lookup           | O(1) (average)  | Hash table                               |
| `append()`                  | Amortized O(1)  | Usually direct insert, occasional resize |
| Search in list (`x in arr`) | O(n)            | Linear scan                              |
| Single loop                 | O(n)            | Visit each element once                  |
| Nested loops                | O(n²)           | `n × n` operations                       |


"Searching in a list is O(n) because Python may need to examine each element until it finds the target. Searching in a set is O(1) on average because Python computes the hash of the value, uses it to locate the appropriate bucket in the hash table, and checks only that bucket instead of scanning the entire collection."


If a variable is assigned anywhere inside a function, Python treats it as a local variable in that function (unless you explicitly declare it global or nonlocal).

Why doesn't Python check the enclosing scope here?

def outer():
    x = 10

    def inner():
        print(x)
        x = 50

    inner()

outer()

The answer is:

"Because the assignment x = 50 makes x a local variable for the entire inner() function. When print(x) executes, Python looks only at the local x, which hasn't been assigned yet, so it raises UnboundLocalError."

Step 1: Python reads inner()

Before executing the function, Python sees:

x = 50

So it decides:

"x is a local variable in inner()."

This decision is made before the function starts running.

Step 2: Execute inner()

Memory looks like this:

Outer Frame

x = 10

      │
      ▼

Inner Frame

x = ?   (local variable, but not assigned yet)

Now Python executes:

print(x)

Does it look in the enclosing scope?

❌ No.

Why?

Because it has already decided that x is local to inner().

So it tries to print the local x.

But the local x hasn't been assigned a value yet.

Result:

UnboundLocalError:
cannot access local variable 'x'
where it is not associated with a value
Your Answer

You said:

after print it throws unbound error

✅ Exactly right.

Then you said:

for outer it gives updated value 50

❌ This part doesn't happen.

Why?

Because once Python raises an exception, execution stops immediately.

The line:

x = 50

is never executed.

So the outer x is never changed.

In fact, outer() doesn't finish normally.

Memory at the Moment of Error
Outer Frame

x = 10

      │
      ▼

Inner Frame

local x = uninitialized

↓

print(x)

↓


| Keyword      | Uses which variable?                           |
| ------------ | ---------------------------------------------- |
| `x = 10`     | Creates a local variable                       |
| `global x`   | Uses the global variable                       |
| `nonlocal x` | Uses the nearest enclosing function's variable |


A decorator is simply:

A function that takes another function, wraps it inside a new function, and returns the new function.

✅ Functions are objects.
✅ Functions can be passed as arguments.
✅ Functions can be returned.
✅ Closures capture variables.
✅ Every call creates a new closure.

hello refers to a single wrapper closure. That closure captures the variable count. Every time hello() is called, Python executes the same wrapper closure, so the captured count retains its updated value between calls.


Mutation changes the object. Rebinding changes what the variable refers to.

def func(
    positional_parameters,
    *args,
    keyword_only_parameters,
    **kwargs
):

def train_model(
    model_name,
    epochs,
    *metrics,
    learning_rate=0.001,
    optimizer="Adam",
    **extra_options
):
    pass

Here:

model_name → required positional parameter
epochs → required positional parameter
*metrics → extra positional arguments
learning_rate and optimizer → keyword-only parameters (because they come after *args)
**extra_options → any remaining keyword arguments



Decorators solve the problem of adding common behavior to multiple functions without modifying each function individually.


Parameterized decorators have three nested functions because the required information becomes available at three different times.