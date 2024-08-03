import os
import sys
import fnmatch

def generate_tree(startpath, exclude_dirs=None, exclude_patterns=None):
    if exclude_dirs is None:
        exclude_dirs = set()
    if exclude_patterns is None:
        exclude_patterns = []

    tree = []
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = '│   ' * level + '├── '
        for f in sorted(files):
            if not any(fnmatch.fnmatch(f, pattern) for pattern in exclude_patterns):
                tree.append(f"{subindent}{f}")
    return '\n'.join(tree)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_project_root> [output_file_suffix]")
        sys.exit(1)

    project_root = sys.argv[1]
    
    # Check if an output file suffix was provided
    output_suffix = f"_{sys.argv[2]}" if len(sys.argv) > 2 else ""
    
    exclude_dirs = {'.git', '.vscode', '__pycache__', 'node_modules', 'venv', 'env', 'build', 'dist'}
    exclude_patterns = [
        '*.o', '*.pyc', '*.class', '*.log', '*.tmp', '*.temp', '*.swp', '*.swo',
        '*.bak', '*.cache', '*.DS_Store', 'Thumbs.db', '*.pyo', '*.exe', '*.dll',
        '*.so', '*.dylib', '*.a', '*.obj', '*.db', '*.jar', '.gitignore', '.env',
        '*.pid', '*.out', '*.toc', '*.aux', '*.bbl', '*.blg',
    ]

    tree = generate_tree(project_root, exclude_dirs, exclude_patterns)
    
    # Generate the output file name
    output_file = f"project_structure{output_suffix}.txt"
    
    # Write the tree to the file
    with open(output_file, 'w') as f:
        f.write(tree)
    
    print(f"File hierarchy has been saved to '{output_file}'")
