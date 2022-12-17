from matplotlib import pyplot as plt
import os


# class PlotSaver:


def print_directory(root_dir, max_depth=1):
    """

    eg.
    ├── lstm
    │   ├── lstm.py
    │   ├── lstm_test.py
    │   └── README.md
    ├── lstm_res
    │   ├── accuracy.png

    print tree brackets too
    
    """
    ignore = [".git", ".idea", "__pycache__"]

    for root, dirs, files in os.walk(root_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in ignore]
        depth = root[len(root_dir):].count(os.sep)
        if depth <= max_depth:
            print(f"{'    ' * depth}├── {os.path.basename(root)}")
            for file in files:
                print(f"{'    ' * (depth + 1)}├── {file}")