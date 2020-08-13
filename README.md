# List Android project large files
Script to list large classes in Android project `(default >= 300 lines)`
> Large classes in projects can be hard to maintain, often contains code smells and lacks refactoring. This script helps you to find theses large classes.

```python
python list_large_files.py --project [PROJECT_DIR]
```
## Options
```
Show the largest files in Android project

options:
  -h, --help            show this help message and exit
  --project             Project dir
  --limit               Lines count limit
  --include_test        Include test files
  --output              File to save the results
  ```
