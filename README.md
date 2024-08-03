# File Hierarchy Generator

This tool generates a visual representation of your project's file structure. It's particularly useful for providing context to AI language models like Claude about how your project files are organized.

## Features

- Generates a tree-like structure of your project's file hierarchy
- Excludes common non-essential directories (e.g., .git, node_modules) and files (e.g., .pyc, .o)
- Allows for custom output file naming

## Usage

Run the script from the command line with the following syntax:

```
python file_hierarchy.py <path_to_project_root> [output_file_suffix]
```

- `<path_to_project_root>`: The path to the root directory of the project you want to analyze (required)
- `[output_file_suffix]`: An optional suffix for the output file name (optional)

### Examples:

1. Generate a file hierarchy for the current directory:
   ```
   python file_hierarchy.py .
   ```
   This will create a file named `project_structure.txt` in the current directory.

2. Generate a file hierarchy for a specific project with a custom suffix:
   ```
   python file_hierarchy.py /path/to/your/project myproject
   ```
   This will create a file named `project_structure_myproject.txt` in the current directory.

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

