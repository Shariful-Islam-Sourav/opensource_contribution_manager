
# Open Source Project Management System

A Python-based utility designed to manage open-source project metadata, track contributors, and organize issue reports. This system automates the generation of project reports and CSV data exports for streamlined project oversight.

## Features

- **Project Metadata Tracking**: Securely stores project name, version, start year, and leadership info using immutable tuples.
- **Contributor Management**: Registers contributors with details on roles, technical stack, and commit counts.
- **Issue Tracking**: Catalogs bugs and features with status tracking (Open, In Progress, Resolved) and priority levels.
- **Set Operations**: Analyzes project health by identifying unique reporters and tech stack intersections.
- **Automated Reporting**: 
    - Generates a `project_report.txt` containing high-level summaries and urgent issues.
    - Exports detailed issue data to `issues.csv`.
- **File System Integration**: Automatically creates project-specific directories for data storage.

## How It Works

The script is divided into four main sections:

1.  **Project & Contributor Setup**: Collects core project data and registers 4 initial contributors.
2.  **Issue Management**: Processes 5 issue reports, calculates priorities, and identifies top reporters.
3.  **File Operations**: Creates a directory based on the project name and writes the summary reports and CSV logs.
4.  **Bonus Analytics**: Extracts urgent issues (Critical/High priority) and appends them to the final report.

## Requirements

- Python 3.x
- `os` module (standard library)

## Usage

1. Run the script:
   ```bash
   python task_5.py
