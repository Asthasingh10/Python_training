## 📘 Chapter 10: Dictionaries

### 10.1. Introduction: Dictionaries

#### 10.1.1. Learning Goals

- Understand what dictionaries are and how they differ from other data structures.
```
A dictionary is a collection of key-value pairs. Each key is unique, and it maps to a value. Example:
student = {
    "name": "Astha",
    "age": 21,
    "course": "B.Tech CSE"
}
```
| Feature             | Dictionary                         | List/Array                     | Set                             | Tuple                          |
|---------------------|-------------------------------------|--------------------------------|----------------------------------|--------------------------------|
| **Structure**        | Key-value pairs                     | Ordered collection of items    | Unordered unique items           | Ordered, immutable items       |
| **Access by**        | Key                                | Index                          | Can't access by index            | Index                          |
| **Order** (Python 3.7+)| Maintains insertion order         | Maintains order                | Does **not** maintain order      | Maintains order                |
| **Mutability**       | Mutable                            | Mutable                        | Mutable                          | **Immutable**                  |
| **Duplicates**       | Keys must be unique                | Allows duplicates              | Does **not** allow duplicates    | Allows duplicates              |


- Learn how to create, modify, and access data in dictionaries.
```
Create: my_dict = {"brand": "Ford", "model": "Mustang"}
Modify: my_dict["model"] = "Figo"
Access: print(my_dict["brand"])  # Ford
You can also use .get() to avoid errors if the key doesn’t exist: 
>> print(my_dict.get("year", "Not Available"))  # Not Available
``` 
- Master dictionary operations and advanced patterns such as accumulation.
```
Common operations:
dict.keys(), dict.values(), dict.items()

Adding or removing keys using del, .pop(), .update()

Looping through dictionaries:
for key, value in my_dict.items():
    print(key, value)

Accumulation pattern:
Used for tasks like counting occurrences. Example: Count how many times each word appears:

text = "apple banana apple orange"
counter = {}
for word in text.split():
    counter[word] = counter.get(word, 0) + 1
print(counter)  # {'apple': 2, 'banana': 1, 'orange': 1}

```
- Learn when and why dictionaries should be used in real-world scenarios.
```
Dictionaries are ideal when:
- You need fast lookups (like a contact book).
- Data is labeled (like JSON or API responses).
- You want to build mappings or counters.

Real-world examples:
- Storing user profiles (user["email"])
- Counting votes or word frequency
- Representing JSON-like data (APIs, configs) 
```

#### 10.1.2. Objectives

- Define dictionaries and identify key-value pairs.
```
- A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
- Think of it like a real-life dictionary: the word (key) maps to its meaning (value).
 Example:
person = {"name": "Astha", "age": 21, "city": "Mathura"}
```
- Perform insertions, deletions, updates, and lookups.
```
Insert: person["email"] = "astha@example.com"
Update: person["age"] = 22
Delete: del person["city"]
LookUp: print(person["name"])  # Output: Astha
Safe Lookup: print(person.get("city", "Not found"))  # Avoids error if key is missing
```
- Use dictionary methods to manipulate and traverse data.
```
Common methods:

dict.keys() – returns all keys

dict.values() – returns all values

dict.items() – returns key-value pairs

dict.update() – updates with another dictionary or key-value pairs

dict.pop(key) – removes and returns the value for a key
```
- Implement accumulation and aggregation tasks using dictionaries.
```
Used to count or group data dynamically.

words = ["apple", "banana", "apple", "orange"]
counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

print(counter)  # {'apple': 2, 'banana': 1, 'orange': 1}

```
- Understand dictionary copying and aliasing behavior.
```
- Aliasing (shared reference):
a = {"x": 1}
b = a
b["x"] = 99
print(a)  # {'x': 99} – a is also changed!

- Proper copy (shallow):
c = a.copy()
c["x"] = 50
print(a)  # Original remains unchanged

```
---

### 10.2. Getting Started with Dictionaries

Dictionaries in Python are **unordered collections** of data values used to store data in **key:value** pairs.

```python
# Basic dictionary
student = {"name": "Aman", "age": 22, "courses": ["Math", "CompSci"]}
```

- Keys are **unique** and must be **immutable** (str, int, tuple).
- Values can be any type.

Accessing elements:

```python
print(student["name"])         # Aman
print(student.get("age"))      # 22
print(student.get("grade", "N/A"))  # N/A (default)
```

---

### 10.3. Dictionary Operations

- **Accessing**: `dict[key]` or `dict.get(key)`
- **Adding/Updating**: `dict[key] = value`
- **Deleting**: `del dict[key]` or `dict.pop(key)`
- **Membership Test**: `'key' in dict`
- **Length**: `len(dict)`

```python
student["grade"] = "A"      # Add new key
del student["courses"]      # Delete key
```

---

### 10.4. Dictionary Methods

- `dict.keys()`
- `dict.values()`
- `dict.items()`
- `dict.pop(key)`
- `dict.popitem()`
- `dict.update(other_dict)`
- `dict.clear()`

#### 10.4.1. Iterating over Dictionaries

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

#### 10.4.2. Safely Retrieving Values

Use `get()` to avoid `KeyError`.

```python
email = student.get("email", "Not Found")
```

---

### 10.5. Aliasing and Copying

```python
a = {"x": 1, "y": 2}
b = a             
c = a.copy() 
a["x"] = 99
print(b["x"])   
print(c["x"])   
```

Deep copies for nested structures:

```python
import copy
deep_copy = copy.deepcopy(nested_dict)
```

---

### 10.6. Accumulating Multiple Results in a Dictionary

Use `dict.setdefault()` or `collections.defaultdict()`.

```python
from collections import defaultdict

scores = defaultdict(list)
scores["Math"].append(90)
scores["Math"].append(85)
print(scores)  # {'Math': [90, 85]}
```

---

### 10.7. Accumulating Results from a Dictionary

Example: Counting word occurrences.

```python
text = "to be or not to be"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)  # {'to': 2, 'be': 2, 'or': 1, 'not': 1}
```

---

### 10.8. Accumulating the Best Key

Find the key with the maximum value.

```python
grades = {'Alice': 91, 'Bob': 85, 'Charlie': 99}
top_student = max(grades, key=grades.get)
print(top_student)  # Charlie
```

---

### 10.9. 👩💻 When to Use a Dictionary

Use dictionaries when:

- Fast lookups and updates are needed.
- Data is best represented as key-value pairs.
- Frequency counting or grouping is required.
- Order of insertion matters (Python 3.7+ maintains order).

---

## 💡 Advanced Assignment: Mastering Dictionaries

### 🧠 **Level: Hard**

#### **Q1. Nested Aggregation**

Write a function that takes a list of tuples, each containing (department, employee, salary), and returns a dictionary with departments as keys and a list of (employee, salary) sorted by salary descending.

```python
data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]
```
Answer:
```python
def group_and_sort_employees(data):
    result = {}

    for dept, emp, sal in data:
        if dept not in result:
            result[dept] = []
        result[dept].append((emp, sal))
    for dept in result:
        result[dept].sort(key=lambda x: x[1], reverse=True)
    return result
```

Expected output:

```python
{
    'HR': [('Bob', 60000), ('Alice', 50000)],
    'Tech': [('Charlie', 120000), ('Eve', 115000), ('Dave', 110000)]
}
```

---

#### **Q2. Inverted Index**

Create a dictionary from a list of sentences that maps each word to the indices of the sentences it appears in.

```python
sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
```

Expected output:

```python
{
    'the': [0, 1, 2],
    'quick': [0],
    'dog': [1, 2],
    ...
}
```
```python
def word_to_sentence_indices(sentences):
    word_map = {}

    for idx, sentence in enumerate(sentences):
        words = set(sentence.split()) 
        for word in words:
            if word not in word_map:
                word_map[word] = []
            word_map[word].append(idx)

    return word_map

```
---

#### **Q3. Deep Copy Trap**

Demonstrate a scenario where using `dict.copy()` fails due to nested structures. Show how `deepcopy` fixes it.

```python
original = {
    "employee": {
        "name": "Astha",
        "skills": ["Python", "SQL"]
    }
}
copied = original.copy()
copied["employee"]["skills"].append("Power BI")

print("Original:", original)
print("Copied:", copied)

```
---

#### **Q4. Accumulate Word Lengths**

Write a program that takes a list of words and creates a dictionary where the key is the length of the word, and the value is a list of words of that length.

```python
words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
```

Expected output:

```python
{2: ['hi', 'ok'], 5: ['hello', 'thanks'], 3: ['hey', 'bye']}
```
```python
def group_words_by_length(words):
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)

    return length_dict

```
---

#### **Q5. Dictionary Merge with Conflict Resolution**

Given two dictionaries, merge them such that:

- If keys are unique, include both.
- If keys conflict, take the larger value.

```python
d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}

# Output: {'a': 5, 'b': 10, 'c': 3}
```

```python
def merge_dicts_with_conflict(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] = max(merged[key], value)
        else:
            merged[key] = value
    return merged

```
---
