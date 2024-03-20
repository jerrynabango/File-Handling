**File Handling in Python**

File handling in Python allows you to work with files, such as reading from and writing to them. Python provides built-in functions and methods for performing various file operations, making it easy to manipulate files and process their contents.

**Opening a File**

You can open a file using the `open()` function, which takes two parameters: the file path and the mode in which you want to open the file. The mode can be "r" for reading, "w" for writing, "a" for appending, "r+" for reading and writing, and more.

```python
file = open("filename.txt", "r")
```

**Reading from a File**

You can read the contents of a file using various methods such as `read()`, `readline()`, or `readlines()`.

```python
content = file.read()  # Reads the entire file
line = file.readline()  # Reads one line at a time
lines = file.readlines()  # Reads all lines and returns a list
```

**Writing to a File**

To write to a file, open it in write mode ("w") or append mode ("a") and use the `write()` method.

```python
file = open("filename.txt", "w")
file.write("This is a line.\n")
```

**Closing a File**

After performing file operations, it's important to close the file using the `close()` method to release system resources.

```python
file.close()
```

**Using `with` Statement**

Python's `with` statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.

```python
with open("filename.txt", "r") as file:
    content = file.read()
    print(content)
```

**Error Handling**

When working with files, it's essential to handle exceptions that may occur, such as `FileNotFoundError` or `PermissionError`.

```python
try:
    file = open("filename.txt", "r")
    # File operations
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    file.close()
```
