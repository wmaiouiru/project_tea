import os
import sys
ingredient_dir = os.path.dirname(os.path.realpath(__file__))
python_dir = os.path.dirname(ingredient_dir)
src_dir = os.path.dirname(python_dir)
root_dir = os.path.dirname(src_dir)
sys.path.append(root_dir)
