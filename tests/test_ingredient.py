import os
import sys
import json
import unittest
import logging

test_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(test_dir)
sys.path.append(root_dir)
logger = logging.getLogger(__name__)
logger.info(json.dumps(sys.path, indent=2))

import src.python.ingredient.client as ingredient_client

class TestIngredient(unittest.TestCase):
    def test_hello_world(self):
        logger.info('test_hello_world')
        ingredient_client.run()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()