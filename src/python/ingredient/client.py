import json
import random
import logging
import uuid

import grpc

from google.protobuf.json_format import MessageToJson

import src.python.services.ingredient_pb2 as ingredient_pb2
import src.python.services.ingredient_pb2_grpc as ingredient_pb2_grpc


logger = logging.getLogger(__name__)

def run():
  # NOTE(gRPC Python Team): .close() is possible on a channel and should be
  # used in circumstances in which the with statement does not fit the needs
  # of the code.
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = ingredient_pb2_grpc.IngredientServiceStub(channel)
    example_ingredient = {}
    example_ingredient["id"] = str(uuid.uuid4())
    example_ingredient["name"] = "water"
    example_ingredient["description"] = "H2O, water!"
    example_ingredient["photo_url"] = None
    ingredient = ingredient_pb2.Ingredient(id=example_ingredient["id"],
      name=example_ingredient["name"],
      description=example_ingredient["description"],
      photo_url=example_ingredient["photo_url"])
    logger.info('\n{ingredient}'.format(ingredient=MessageToJson(ingredient)))
    logger.info("-------------- GetIngredient --------------")
    """
    guide_get_feature(stub)
    print("-------------- ListFeatures --------------")
    guide_list_features(stub)
    print("-------------- RecordRoute --------------")
    guide_record_route(stub)
    print("-------------- RouteChat --------------")
    guide_route_chat(stub)
    """


if __name__ == '__main__':
  FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logging.basicConfig(format=FORMAT, level=logging.INFO)
  # logging
  # logging.setLevel(logging.INFO)
  run()
