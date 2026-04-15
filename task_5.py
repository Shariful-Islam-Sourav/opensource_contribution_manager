import os


# Section 1

print("=" * 40)
print("Open Source Project Setup")
print("=" * 40)

# Collect Project Info
p_name = input("Enter project name: ")
p_version = input("Enter project version: ")
p_year = int(input("Enter year started: "))
p_lang = input("Enter main programming language: ")
p_lead = input("Enter your name (Project Lead): ")

# Store in a tuple
project = (p_name, p_version, p_year, p_lang, p_lead)

print("\n--- Project Info (By Index) ---")
print(f"Name    : {project[0]}")
print(f"Version : {project[1]}")
print(f"Year    : {project[2]}")
print(f"Language: {project[3]}")
print(f"Lead    : {project[4]}")

# Slicing the first three fields
print(f"First 3 fields: {project[:3]}")

# count() and index()
print(f"Language count: {project.count(p_lang)}")
print(f"Language index: {project.index(p_lang)}")

# TUPLE IMMUTABILITY COMMENT:
# project[0] = "NewName" -> This is a TypeError.
# Tuples are immutable, which means once they are created values cannot be modified.
# This is best for storing core, permanent data


contributors = []
print("\n--- Register 4 Contributors ---")
for i in range(4):
    print(f"\nContributor {i + 1}:")
    c_name = input("Name: ")
    c_role = input("Role: ")
    c_lang = input("Language: ")
    c_commits = int(input("Commits: "))
    c_country = input("Country: ")

    contrib_dict = {
        'name': c_name,
        'role': c_role,
        'language': c_lang,
        'commits': c_commits,
        'country': c_country
    }
    contributors.append(contrib_dict)

# Extract, sort, and print names
names = []
for c in contributors:
    extracted_name = c['name']
    names.append(extracted_name)
    names.sort()
print(f"\nSorted names: {names}")

# Slicing first two using negative indexing
# If length is 4, -4 to -2 extracts the first two
first_two = names[:-2]
print(f"First two names : {first_two}")

# Add status using update()
for c in contributors:
    c.update({'status': 'Active'})

# get() and copy() on first contributor
print(f"Contributor 1 status: {contributors[0].get('status')}")
backup_contributor = contributors[0].copy()
print(f"Backup of first contributor: {backup_contributor}")

# Section 2

issues = []
print("\n--- Register 5 Issues ---")
for i in range(5):
    print(f"\nIssue {i + 1}:")
    i_id = input("ID (e.g., ISS-001): ")
    i_title = input("Title: ")
    i_type = input("Type (Bug/Feature): ")
    i_priority = input("Priority (Critical/High/Medium/Low): ")
    i_reporter = input("Reporter: ")
    i_status = input("Status (Open/In Progress/Resolved): ")

    issue_dict = {
        'id': i_id,
        'title': i_title,
        'type': i_type,
        'priority': i_priority,
        'reporter': i_reporter,
        'status': i_status
    }
    issues.append(issue_dict)

# Count 'Open' issues with loop and counter
open_count = 0
for issue in issues:
    if issue['status'] == 'Open':
        open_count += 1
print(f"\nOpen issues: {open_count}")

# Change first issue's priority via index
issues[0]['priority'] = 'Critical'
print(f"First issue priority updated to: {issues[0]['priority']}")

# Slice last two issues
print(f"Last two issues: {issues[-2:]}")

# Set operations
reporters = {issue['reporter'] for issue in issues}
tech_stack = {c['language'] for c in contributors}

tech_stack.add('Docker')
combined_set = tech_stack.union(reporters)
tech_stack.discard('Java')  # Will silently do nothing if 'Java' isn't there
common_items = tech_stack.intersection(reporters)
diff_reporters = reporters.difference(tech_stack)

print(f"\nReporters set: {reporters}")
print(f"Tech stack set: {tech_stack}")
print(f"Union: {combined_set}")
print(f"Intersection: {common_items}")
print(f"Difference (Reporters not in tech stack): {diff_reporters}")

# Check for 'Critical' in all priorities
all_priorities = {issue['priority'] for issue in issues}
if 'Critical' in all_priorities:
    print("YES - Critical priority present. Flag for immediate review.")

# Build priority_count dict
priority_count = {}
for issue in issues:
    p = issue['priority']
    if p in priority_count:
        priority_count[p] += 1
    else:
        priority_count[p] = 1

# Build status_groups dict
status_groups = {}
for issue in issues:
    s = issue['status']
    t = issue['title']
    if s in status_groups:
        status_groups[s].append(t)
    else:
        status_groups[s] = [t]

# Print using keys(), values(), and items()
print(f"\nPriority Keys: {list(priority_count.keys())}")
print(f"Priority Values: {list(priority_count.values())}")
print("Status Groups (Items):")
for key, value in status_groups.items():
    print(f" - {key}: {value}")

# Find top reporter without max() or Counter()
reporter_counts = {}
for issue in issues:
    r = issue['reporter']
    if r in reporter_counts:
        reporter_counts[r] += 1
    else:
        reporter_counts[r] = 1

top_reporter = ""
highest_count = 0
for rep, count in reporter_counts.items():
    if count > highest_count:
        highest_count = count
        top_reporter = rep

print(f"\nTop reporter: {top_reporter} ({highest_count} issues)")

# pop() 'type' from first issue
popped_type = issues[0].pop('type')
print(f"\nPopped type from first issue: {popped_type}")
print(f"First issue after pop: {issues[0]}")


# Section 3

print("\n--- File Operations ---")
folder_name = project[0].lower().replace(" ", "_")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder created: {folder_name}/")
else:
    print(f"Folder already exists: {folder_name}/")

report_path = os.path.join(folder_name, 'project_report.txt')
csv_path = os.path.join(folder_name, 'issues.csv')

# Writing Files
try:
    with open(report_path, 'w') as f:
        f.write(f"PROJECT REPORT: {project[0]}\n")
        f.write(f"Version: {project[1]} | Lead: {project[4]}\n")
        f.write(f"Total Contributors: {len(contributors)}\n")
        f.write(f"Total Issues: {len(issues)}\n")
        f.write(f"Top Reporter: {top_reporter}\n")

    with open(csv_path, 'w') as f:
        f.write("id,title,priority,reporter,status\n")
        for iss in issues:
            # issue[0] no longer has 'type' because we popped it
            i_id = iss.get('id', '')
            i_title = iss.get('title', '')
            i_prio = iss.get('priority', '')
            i_rep = iss.get('reporter', '')
            i_stat = iss.get('status', '')
            f.write(f"{i_id},{i_title},{i_prio},{i_rep},{i_stat}\n")

    print(f"Files saved successfully in {folder_name}/")
except IOError as e:
    print(f"An error occurred while writing files: {e}")

print(f"Folder contents: {os.listdir(folder_name)}")

# Reading Files
try:
    print("\n--- read() ---")
    with open(report_path, 'r') as f:
        print(f.read())

    print("--- readline() ---")
    with open(report_path, 'r') as f:
        print(f"Line 1: {f.readline().strip()}")
        print(f"Line 2: {f.readline().strip()}")

    print("\n--- readlines() ---")
    with open(csv_path, 'r') as f:
        all_lines = f.readlines()
        print(f"Total CSV lines: {len(all_lines)}")
        crit_high_count = 0
        for line in all_lines:
            if 'Critical' in line or 'High' in line:
                crit_high_count += 1
                print(f"Match: {line.strip()}")
        print(f"Critical/High lines: {crit_high_count}")

except FileNotFoundError as e:
    print(f"File not found: {e}")

# Final Printed Summary
print("\n" + "=" * 40)
print(f"{project[0]} FINAL SUMMARY")
print("=" * 40)
print(f"Project: {project[0]} Version: {project[1]} Lead: {project[4]}")
print(f"Contributors: {len(contributors)} Names: {names}")
print(f"Tech Stack : {list(tech_stack)}")
print(f"Issues: {len(issues)} Open: {open_count} Reporters: {len(reporters)}")
print(f"Top Reporter: {top_reporter} ({highest_count} issues)")
print(
    f"Critical:{priority_count.get('Critical', 0)} High:{priority_count.get('High', 0)} Medium:{priority_count.get('Medium', 0)}")
print(f"Report: {report_path}")
print(f"CSV   : {csv_path}")
print(f"{project[0]} complete. Thank you for contributing to open source!")

# Section 4

print("\n--- Bonus Section ---")
# Part 1
urgent = [i['title'] for i in issues if i['priority'] == 'Critical' or i['priority'] == 'High']
print(f"Urgent Issues List: {urgent}")
print(f"Length of Urgent Issues: {len(urgent)}")

# Part 2
try:
    with open(report_path, 'a') as f:
        f.write("\nURGENT ISSUES\n")
        for u_title in urgent:
            f.write(f"- {u_title}\n")

    with open(report_path, 'r') as f:
        lines = f.readlines()
        print("\nLast 6 lines of report:")
        for line in lines[-6:]:
            print(line.strip())
except IOError as e:
    print(f"An error occurred: {e}")