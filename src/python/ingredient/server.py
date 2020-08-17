from concurrent import futures
import os
import sys
import json
import random
import logging
import uuid
import traceback

import grpc

from google.protobuf.json_format import MessageToJson

ingredient_dir = os.path.dirname(os.path.realpath(__file__))
python_dir = os.path.dirname(ingredient_dir)
src_dir = os.path.dirname(python_dir)
root_dir = os.path.dirname(src_dir)
sys.path.append(root_dir)

import src.python.services.ingredient_pb2 as ingredient_pb2
import src.python.services.ingredient_pb2_grpc as ingredient_pb2_grpc
logger = logging.getLogger(__name__)
class IngredientServiceServicer(ingredient_pb2_grpc.IngredientServiceServicer):
  """Provides methods that implement functionality of Ingredient server."""

  def __init__(self):
    logger.info("IngredientServiceServicer __init__")

  def CreateIngredient(self, request, context):
    logger.info("called  CreateIngredient")
    try:
      logger.info(f"\n{request}")
      logger.info("\n{request}".format(request=MessageToJson(request)))
      ingredient = ingredient_pb2.Ingredient(id=request.ingredient.id,
        name=request.ingredient.name,
        description=request.ingredient.description,
        photo_url=request.ingredient.photo_url)
      logger.info('\n{ingredient}'.format(ingredient=MessageToJson(ingredient)))
      logger.info("TODO insert to DB")
      return ingredient_pb2.CreateIngredientResponse(ingredient=ingredient)
    except:
      logger.error(traceback.format_exc())
  def ListIngredient(self, request, context):
    logger.info("called  ListIngredient")
    new_id = str(uuid.uuid4())
    name = "water"
    description = "H2O, water!"
    photo_url = None
    ingredient = ingredient_pb2.Ingredient(id=new_id,
      name=name,
      description=description,
      photo_url=photo_url)
    print(ingredient)
    logger.info("return ListIngredient")
    return ingredient_pb2.ListIngredientResponse(ingredient=ingredient)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  ingredient_pb2_grpc.add_IngredientServiceServicer_to_server(
    IngredientServiceServicer(), server)
  server.add_insecure_port('[::]:50051')
  logger.info("server started")
  server.start()
  server.wait_for_termination(timeout=30)
  logger.info("server terminated")


class IngredientServer(object):
  def __init__(self) -> None:
    self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ingredient_pb2_grpc.add_IngredientServiceServicer_to_server(
      IngredientServiceServicer(), self.server)
    self.server.add_insecure_port('[::]:50051')
    super().__init__()
  def start(self) -> None:
    """
      Start the server
    """
    logger.info("server started")
    self.server.start()

  def stop(self) -> None:
    """
      Stop the server
    """
    grace = 30
    self.server.stop(grace)
    logger.info("server terminated")

  def serve(self) -> None:
    """
      Start the server and wait for termination
    """
    self.server.start()
    self.server.wait_for_termination(timeout=30)
    logger.info("server terminated")

if __name__ == '__main__':
  FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logging.basicConfig(format=FORMAT, level=logging.INFO)
  serve()
