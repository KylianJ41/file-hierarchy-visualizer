import os
import sys
import fnmatch
import argparse

def generate_tree(startpath, exclude_dirs=None, exclude_patterns=None):
    if exclude_dirs is None:
        exclude_dirs = set()
    if exclude_patterns is None:
        exclude_patterns = []

    tree = []
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not any(fnmatch.fnmatch(d, pattern) for pattern in exclude_patterns)]
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = '│   ' * level + '├── '
        for f in sorted(files):
            if not any(fnmatch.fnmatch(f, pattern) for pattern in exclude_patterns):
                tree.append(f"{subindent}{f}")
    return '\n'.join(tree)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a file hierarchy tree.")
    parser.add_argument("project_root", help="Path to the project root")
    parser.add_argument("-o", "--output", help="Suffix for output file name")
    parser.add_argument("-d", "--exclude-dirs", nargs="*", default=[], help="Additional directories to exclude (exact names)")
    parser.add_argument("-p", "--exclude-patterns", nargs="*", default=[], help="Patterns to exclude (can match both files and directories)")
    args = parser.parse_args()

    project_root = args.project_root
    output_suffix = f"_{args.output}" if args.output else ""
    
    # Predefined exclusions
    exclude_dirs = {'.git', '.vscode', '__pycache__', 'node_modules', 'venv', 'env', 'build', 'dist'}
    exclude_patterns = [
        '*.o', '*.pyc', '*.class', '*.log', '*.tmp', '*.temp', '*.swp', '*.swo',
        '*.bak', '*.cache', '*.DS_Store', 'Thumbs.db', '*.pyo', '*.exe', '*.dll',
        '*.so', '*.dylib', '*.a', '*.obj', '*.db', '*.jar', '.gitignore', '.env',
        '*.pid', '*.out', '*.toc', '*.aux', '*.bbl', '*.blg',
    ]

    # Add user-specified exclusions
    exclude_dirs.update(args.exclude_dirs)
    exclude_patterns.extend(args.exclude_patterns)

    tree = generate_tree(project_root, exclude_dirs, exclude_patterns)
    
    # Generate the output file name
    output_file = f"project_structure{output_suffix}.txt"
    
    # Write the tree to the file
    with open(output_file, 'w') as f:
        f.write(tree)
    
    print(f"File hierarchy has been saved to '{output_file}'")
    print(f"Excluded directories (exact names): {', '.join(exclude_dirs)}")
    print(f"Excluded patterns (files and directories): {', '.join(exclude_patterns)}")
