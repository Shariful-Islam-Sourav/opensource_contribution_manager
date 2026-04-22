# 📘 Project Documentation

## Open Source Project Manager CLI

---

## 1. 📌 Overview

This project is a **Command-Line Interface (CLI) application** built in Python that simulates the management of an open-source project. It allows users to:

* Store project details
* Manage contributors
* Track and analyze issues
* Perform data operations using Python structures
* Generate reports and CSV files

---

## 2. 🎯 Objectives

The main goals of this project are:

* Demonstrate Python core concepts:

  * Tuples
  * Lists
  * Dictionaries
  * Sets
* Implement file handling operations
* Practice structured data manipulation
* Simulate real-world project workflows

---

## 3. 🧱 System Architecture

The application is divided into **four main sections**:

### 🔹 Section 1: Project & Contributor Management

* Collects project information
* Stores data in a tuple (immutable)
* Registers contributors using dictionaries inside a list
* Performs:

  * Sorting
  * Slicing
  * Dictionary updates

---

### 🔹 Section 2: Issue Tracking System

* Stores issues as dictionaries in a list
* Tracks:

  * ID, Title, Type, Priority, Reporter, Status
* Performs:

  * Counting open issues
  * Updating priorities
  * Grouping by status
  * Finding top reporter

---

### 🔹 Section 3: File Handling

* Creates project directory
* Generates:

  * `project_report.txt`
  * `issues.csv`
* Supports:

  * Writing files
  * Reading using:

    * `read()`
    * `readline()`
    * `readlines()`

---

### 🔹 Section 4: Bonus Features

* Extracts urgent issues (Critical/High)
* Appends urgent issues to report file
* Displays last lines of report

---

## 4. 📊 Data Structures Used

### 🟢 Tuple

* Stores project information
* Immutable (ensures data integrity)

### 🔵 List

* Stores:

  * Contributors
  * Issues
* Supports indexing, slicing, iteration

### 🟡 Dictionary

* Represents:

  * Contributor data
  * Issue data
* Key operations:

  * `get()`
  * `update()`
  * `copy()`
  * `pop()`

### 🔴 Set

* Used for:

  * Unique reporters
  * Tech stack
* Operations:

  * Union
  * Intersection
  * Difference

---

## 5. ⚙️ Functional Workflow

### Step 1: Project Initialization

* User inputs project details
* Data stored in tuple

---

### Step 2: Contributor Registration

* User enters 4 contributors
* Data stored in list of dictionaries
* Names extracted and sorted

---

### Step 3: Issue Registration

* User enters 5 issues
* Data stored in list of dictionaries

---

### Step 4: Data Processing

* Count open issues
* Identify top reporter
* Group issues by status
* Count priorities

---

### Step 5: File Generation

* Create folder using project name
* Save:

  * Summary report (TXT)
  * Issues data (CSV)

---

### Step 6: File Reading

* Display contents using different read methods
* Filter high/critical issues

---

## 6. 📁 File Structure

```
project_name/
│── task_5.py
│── project_report.txt
│── issues.csv
```

---

## 7. 🧪 Error Handling

The project uses basic exception handling:

* `IOError` → File writing issues
* `FileNotFoundError` → File reading issues

---

## 8. 📈 Output Details

### 📄 project_report.txt

Contains:

* Project info
* Contributor count
* Issue count
* Top reporter
* Urgent issues

---

### 📊 issues.csv

Contains:

* id
* title
* priority
* reporter
* status

---

## 9. ⚠️ Limitations

* No persistent storage (data resets after run)
* No input validation
* Fixed number of contributors/issues
* CLI-only interface
* No database integration

---

## 10. 🚀 Future Improvements

* Add database (SQLite / MongoDB)
* Convert to web app (Flask / Django / MERN)
* Add input validation
* Dynamic number of contributors/issues
* Add search and filtering
* Build GUI version

---

## 11. 🧠 Learning Outcomes

After completing this project, a developer understands:

* Data structure usage in real scenarios
* File handling in Python
* CLI application design
* Basic data analysis logic
* Structured programming practices

---

## 12. 👨‍💻 Author

Project Lead: Shariful Islam Sourav

---

## 13. 📜 Conclusion

This project serves as a **foundational mini-system** that mimics real-world project management workflows while reinforcing Python fundamentals. It is ideal for beginners transitioning into intermediate-level programming.
