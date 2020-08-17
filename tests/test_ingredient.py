import os
import sys
import json
import unittest
import logging
import threading

test_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(test_dir)
sys.path.append(root_dir)
logger = logging.getLogger(__name__)
logger.info(json.dumps(sys.path, indent=2))

import src.python.ingredient.client as ingredient_client
import src.python.ingredient.server as ingredient_server
from src.python.ingredient.server import IngredientServer
class TestIngredient(unittest.TestCase):
  def test_hello_world(self):
    logger.info('test_hello_world')
    ingredient_client.run_proto()
    self.assertEqual(True, True)
  def test_client_server_hello_world(self):
    logger.info('test_client_server_hello_world')
    server = IngredientServer()
    thread = threading.Thread(target=server.start)
    thread.start()
    ingredient_client.run()
    server.stop()
    self.assertEqual(True, True)
if __name__ == '__main__':
  unittest.main()