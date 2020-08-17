# Runing pytest in virtual environment

In virtual environment, you need to run `python -m pytest <test-name>.py` to run pytest in virtual environment.
```
python -m pytest test_ingredient.py
```
ref: https://stackoverflow.com/questions/35045038/how-do-i-use-pytest-with-virtualenv

# Handling python paths
To handle python paths, the following code is added to allow relative imports
```
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)
```


