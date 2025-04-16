## 🔰 **Beginner-Level Questions (Concept + Code)**

1. **Open and Read File**

   - Write a Python program to read a file `notes.txt` and print its contents line-by-line.
   - 📌 _Concept tested_: File opening, reading, and loop.

```python
with open('notes.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

2. **Count Lines in a File**

   - Count how many lines exist in a file `poem.txt`.
```python
with open('poem.txt', 'r') as file:
    lines = file.readlines()
    print(f'Number of lines: {len(lines)}')

```

3. **Write to a File**

   - Create a new file `reminder.txt` and write 5 tasks to it, one per line.
```python
tasks = [
    "Buy groceries\n",
    "Complete homework\n",
    "Attend meeting\n",
    "Call friend\n",
    "Go for a walk\n"
]
with open('reminder.txt', 'w') as file:
    file.writelines(tasks)
```

4. **Append to a File**

   - Add a new task to `reminder.txt` without deleting existing ones.

```python
with open('reminder.txt', 'a') as file:
    file.write("Read a book\n")
```

5. **Check File Exists**
   - Use `os.path.exists()` to check if `data.txt` exists before opening.
```python
import os
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as file:
        print(file.read())
else:
    print("File not found!")

```
---

## 🧪 **Intermediate-Level Questions**

6. **Remove Blank Lines**

   - Write a program that reads `input.txt` and creates `cleaned.txt` with no empty lines.

```python
with open('input.txt', 'r') as infile, open('cleaned.txt', 'w') as outfile:
    for line in infile:
        if line.strip():
            outfile.write(line)
```

7. **Find and Replace**

   - Search and replace the word “Python” with “PYTHON” in `article.txt`.

```python
with open('article.txt', 'r') as file:
    content = file.read().replace('Python', 'PYTHON')

with open('article.txt', 'w') as file:
    file.write(content)

```
8. **Uppercase Writer**

   - Read a file and write its contents in all **uppercase** to `output.txt`.

```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read().upper())

```

9. **Student Report Generator**

   - Read `students.txt` containing `Name,Marks`, calculate and save the pass/fail status in `report.txt` (`Pass` if Marks ≥ 50).
```python
with open('students.txt', 'r') as infile, open('report.txt', 'w') as outfile:
    for line in infile:
        name, marks = line.strip().split(',')
        marks = int(marks)
        status = "Pass" if marks >= 50 else "Fail"
        outfile.write(f'{name},{marks},{status}\n')

```

10. **Reverse File Lines**
    - Reverse the order of lines in `quotes.txt` and write to `reversed_quotes.txt`.
```python
with open('quotes.txt', 'r') as infile:
    lines = infile.readlines()
with open('reversed_quotes.txt', 'w') as outfile:
    for line in reversed(lines):
        outfile.write(line)
```

---

## 💡 **Advanced-Level Questions / Mini Projects**

11. **Log File Analyzer**

    - Read a `server.log` file, count how many times the word `"ERROR"` appears, and write all lines with errors to `errors_only.log`.

12. **Word Frequency Counter**

    - Read `story.txt` and create a dictionary of word frequency (how many times each word appears), and write it to `frequency.txt`.

13. **CSV Reader + Filter**

    - Read `sales.csv`, display all sales above ₹10,000 and write those entries to `high_sales.csv`.

14. **Merge Multiple Files**

    - Combine the contents of `chapter1.txt`, `chapter2.txt`, and `chapter3.txt` into `full_book.txt`.

15. **Directory File Scanner**
    - List all `.txt` or `.csv` files in a given folder using `os.listdir()` and `os.path`.

---

## 🚀 **Bonus Challenges**

16. **Auto Backup System**

    - Copy the contents of `data.csv` into `backup/data_backup.csv` with the current date in the filename.

17. **Text Formatter**

    - Remove leading/trailing spaces and convert tabs to spaces in `raw_text.txt`.

18. **Chat History Logger**

    - Build a basic chat logger: take user input until “exit” and save all messages with timestamps to `chat_log.txt`.

19. **Custom CSV Sorter**

    - Read `products.csv` and sort by price (ascending). Write the sorted records to `products_sorted.csv`.

20. **JSON Converter**
    - Read `students.txt` with comma-separated values, convert it to a list of dictionaries, and write to `students.json`.

---
