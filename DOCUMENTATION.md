# Documentation

## Open Source Project Manager CLI

---

## 1. 🧠 Program Overview (Execution Model)

The script follows a **top-to-bottom procedural execution**:

```text
Input → Store → Process → Analyze → Save → Read → Output
```

There are **no functions or classes**, so all logic executes sequentially in the global scope.

---

## 2. 🔹 Section 1: Project Initialization

### Code

```python
p_name = input("Enter project name: ")
p_version = input("Enter project version: ")
p_year = int(input("Enter year started: "))
p_lang = input("Enter main programming language: ")
p_lead = input("Enter your name (Project Lead): ")

project = (p_name, p_version, p_year, p_lang, p_lead)
```

### Explanation

* User input is collected using `input()`
* `p_year` is explicitly cast to `int` → ensures numeric data type
* All values are grouped into a **tuple**

### Why Tuple?

```python
project = (name, version, year, language, lead)
```

* Immutable → cannot be changed later
* Suitable for **fixed project metadata**

---

### Tuple Operations

```python
project[:3]
project.count(p_lang)
project.index(p_lang)
```

* `[:3]` → slicing (first 3 elements)
* `count()` → counts occurrences
* `index()` → returns position

---

## 3. Section 1: Contributor Management

### Data Structure

```python
contributors = []
```

Each contributor is stored as:

```python
contrib_dict = {
    'name': c_name,
    'role': c_role,
    'language': c_lang,
    'commits': c_commits,
    'country': c_country
}
```

---

### Key Logic

#### 1. Adding Contributors

```python
for i in range(4):
    contributors.append(contrib_dict)
```

* Fixed loop → exactly 4 contributors
* Each iteration creates a new dictionary

---

#### 2. Extracting & Sorting Names

```python
names = []
for c in contributors:
    extracted_name = c['name']
    names.append(extracted_name)
    names.sort()
```

⚠️ Important detail:

* `names.sort()` is inside loop → sorting happens **every iteration**
* Inefficient but works

Better version:

```python
names = [c['name'] for c in contributors]
names.sort()
```

---

#### 3. List Slicing

```python
first_two = names[:-2]
```

* If 4 elements:

  * `[:-2]` → first 2 elements
* Uses **negative indexing**

---

#### 4. Dictionary Update

```python
c.update({'status': 'Active'})
```

* Adds new key-value pair dynamically

---

#### 5. Safe Access & Copy

```python
contributors[0].get('status')
backup_contributor = contributors[0].copy()
```

* `get()` → avoids KeyError
* `copy()` → shallow copy (important for backup)

---

## 4. 🔹 Section 2: Issue Tracking

### Data Structure

```python
issues = []
```

Each issue:

```python
issue_dict = {
    'id': i_id,
    'title': i_title,
    'type': i_type,
    'priority': i_priority,
    'reporter': i_reporter,
    'status': i_status
}
```

---

### Key Operations

#### 1. Counting Open Issues

```python
open_count = 0
for issue in issues:
    if issue['status'] == 'Open':
        open_count += 1
```

* Simple counter pattern
* Time complexity: **O(n)**

---

#### 2. Updating First Issue

```python
issues[0]['priority'] = 'Critical'
```

* Direct dictionary mutation

---

#### 3. List Slicing

```python
issues[-2:]
```

* Gets last 2 elements

---

## 5. 🔹 Section 2: Set Operations

### Creation

```python
reporters = {issue['reporter'] for issue in issues}
tech_stack = {c['language'] for c in contributors}
```

* Uses **set comprehension**
* Automatically removes duplicates

---

### Operations

```python
tech_stack.add('Docker')
combined_set = tech_stack.union(reporters)
tech_stack.discard('Java')
common_items = tech_stack.intersection(reporters)
diff_reporters = reporters.difference(tech_stack)
```

| Operation        | Meaning        |
| ---------------- | -------------- |
| `add()`          | insert element |
| `union()`        | combine sets   |
| `intersection()` | common values  |
| `difference()`   | unique values  |
| `discard()`      | remove safely  |

---

## 6. 🔹 Section 2: Priority Counting

### Code

```python
priority_count = {}
for issue in issues:
    p = issue['priority']
    if p in priority_count:
        priority_count[p] += 1
    else:
        priority_count[p] = 1
```

###  Explanation

* Manual frequency counting
* Equivalent to `Counter` (but implemented manually)

---

## 7. 🔹 Section 2: Status Grouping

```python
status_groups = {}
for issue in issues:
    s = issue['status']
    t = issue['title']
    if s in status_groups:
        status_groups[s].append(t)
    else:
        status_groups[s] = [t]
```

### Logic

* Groups issue titles by status
* Output example:

```python
{
  "Open": ["Bug 1", "Bug 2"],
  "Resolved": ["Fix 1"]
}
```

---

## 8. 🔹 Section 2: Top Reporter Logic

```python
reporter_counts = {}
for issue in issues:
    r = issue['reporter']
    if r in reporter_counts:
        reporter_counts[r] += 1
    else:
        reporter_counts[r] = 1
```

Then:

```python
for rep, count in reporter_counts.items():
    if count > highest_count:
        highest_count = count
        top_reporter = rep
```

###  Explanation

* First loop → count reports
* Second loop → find max manually
* No built-in functions used

---

## 9. 🔹 Dictionary Mutation (pop)

```python
popped_type = issues[0].pop('type')
```

* Removes `'type'` key permanently
* Returns removed value

---

## 10. 🔹 Section 3: File Handling

### Directory Creation

```python
folder_name = project[0].lower().replace(" ", "_")
os.makedirs(folder_name)
```

* Converts project name → folder-safe format

---

### Writing Files

#### TXT File

```python
with open(report_path, 'w') as f:
    f.write(...)
```

#### CSV File

```python
f.write("id,title,priority,reporter,status\n")
```

* Manual CSV writing (no `csv` module used)

---

### Safe Access

```python
iss.get('id', '')
```

* Prevents crash if key missing

---

## 11. 🔹 File Reading

### Methods Used

```python
f.read()
f.readline()
f.readlines()
```

### Filtering Example

```python
if 'Critical' in line or 'High' in line:
```

* String-based filtering

---

## 12. 🔹 Final Summary Output

Prints aggregated data:

```python
print(f"Issues: {len(issues)} Open: {open_count}")
```

* Combines multiple computed values

---

## 13. 🔹 Bonus: List Comprehension

```python
urgent = [i['title'] for i in issues if i['priority'] in ['Critical', 'High']]
```

### 🔍 Explanation

* Compact loop + condition
* More efficient and readable

---

## 14.  Code Design Limitations

* No functions → poor modularity
* No input validation
* Repetitive loops
* Hardcoded limits (4 contributors, 5 issues)

---

## 15. Suggested Refactoring

### Convert into Functions

Example:

```python
def count_open_issues(issues):
    return sum(1 for i in issues if i['status'] == 'Open')
```

---

### Use Built-ins

```python
from collections import Counter
Counter(issue['priority'] for issue in issues)
```

---

### Use CSV Module

```python
import csv
```

---

## 16. 🧠 Key Takeaways

* Shows real usage of Python data structures
* Demonstrates manual implementation of:

  * Counting
  * Grouping
  * Searching
* Good foundation for backend/data processing systems
