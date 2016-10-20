# Import to JCR script
This script will create a Python list of all html files in a specified directory (recursively), and then import all of those files to JCR nodes using a specified Apache Sling instance.

## Requirements
- `pip install requests`
- If pip is not installed, `easy_install pip` first

## Usage
```
import_to_jcr.py [options]

Options:
  -h, --help            show this help message and exit
  -d DIR, --source-dir=DIR
                        Source directory
  -e URI, --endpoint=URI
                        Apache Sling endpoint
```
## Defaults
```
-d, --source-dir: (current working directory)
-e, --endpoint: http://0.0.0.0:8080
```
