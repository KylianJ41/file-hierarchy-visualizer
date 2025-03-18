# File Hierarchy Generator

Implementation of the tree cmd

## Features

- Generates a tree-like structure of your project's file hierarchy
- Excludes common non-essential directories (e.g., .git, node_modules) and files (e.g., .pyc, .o)
- Allows for custom output file naming
- Supports custom exclusion of directories and files/directories by pattern

## Usage

Run the script from the command line with the following syntax:

```
python file_hierarchy.py <path_to_project_root> [options]
```

- `<path_to_project_root>`: The path to the root directory of the project you want to analyze (required)

### Options:

- `-o OUTPUT, --output OUTPUT`: Suffix for output file name
- `-d [EXCLUDE_DIRS ...], --exclude-dirs [EXCLUDE_DIRS ...]`: Additional directories to exclude (exact names)
- `-p [EXCLUDE_PATTERNS ...], --exclude-patterns [EXCLUDE_PATTERNS ...]`: Patterns to exclude (can match both files and directories)

### Examples:

1. Generate a file hierarchy for the current directory:
   ```
   python file_hierarchy.py .
   ```
   This will create a file named `project_structure.txt` in the current directory.

2. Generate a file hierarchy for a specific project with a custom suffix:
   ```
   python file_hierarchy.py /path/to/your/project -o myproject
   ```
   This will create a file named `project_structure_myproject.txt` in the current directory.

3. Generate a file hierarchy excluding specific directories:
   ```
   python file_hierarchy.py /path/to/your/project -d logs backups
   ```
   This will exclude the 'logs' and 'backups' directories from the hierarchy.

4. Generate a file hierarchy excluding files and directories by pattern:
   ```
   python file_hierarchy.py /path/to/your/project -p "*.pdf" "test_*"
   ```
   This will exclude all PDF files and any file or directory starting with "test_".

5. Combine multiple options:
   ```
   python file_hierarchy.py /path/to/your/project -o myproject -d logs backups -p "*.pdf" "test_*"
   ```
   This will create `project_structure_myproject.txt`, excluding 'logs' and 'backups' directories, all PDF files, and anything starting with "test_".

## Output

The script generates a text file containing a tree-like structure of your project. For example:

```
my_project/
├── src/
│   ├── main.py
│   └── utils/
│       ├── helpers.py
│       └── config.py
├── tests/
│   └── test_main.py
├── docs/
│   └── user_guide.md
└── README.md
```
