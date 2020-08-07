# List Android project large files
Script to list large classes in Android project `(default >= 300 lines)`.
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
