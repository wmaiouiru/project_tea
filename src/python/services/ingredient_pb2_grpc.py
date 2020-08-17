# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ingredient_pb2 as ingredient__pb2


class IngredientServiceStub(object):
  """Missing associated documentation comment in .proto file."""

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateIngredient = channel.unary_unary(
        '/ingredient.IngredientService/CreateIngredient',
        request_serializer=ingredient__pb2.CreateIngredientRequest.SerializeToString,
        response_deserializer=ingredient__pb2.CreateIngredientResponse.FromString,
        )
    self.GetIngredient = channel.unary_unary(
        '/ingredient.IngredientService/GetIngredient',
        request_serializer=ingredient__pb2.GetIngredientRequest.SerializeToString,
        response_deserializer=ingredient__pb2.GetIngredientResponse.FromString,
        )
    self.ListIngredient = channel.unary_unary(
        '/ingredient.IngredientService/ListIngredient',
        request_serializer=ingredient__pb2.ListIngredientRequest.SerializeToString,
        response_deserializer=ingredient__pb2.ListIngredientResponse.FromString,
        )


class IngredientServiceServicer(object):
  """Missing associated documentation comment in .proto file."""

  def CreateIngredient(self, request, context):
    """Missing associated documentation comment in .proto file."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetIngredient(self, request, context):
    """Missing associated documentation comment in .proto file."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListIngredient(self, request, context):
    """Missing associated documentation comment in .proto file."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IngredientServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateIngredient': grpc.unary_unary_rpc_method_handler(
          servicer.CreateIngredient,
          request_deserializer=ingredient__pb2.CreateIngredientRequest.FromString,
          response_serializer=ingredient__pb2.CreateIngredientResponse.SerializeToString,
      ),
      'GetIngredient': grpc.unary_unary_rpc_method_handler(
          servicer.GetIngredient,
          request_deserializer=ingredient__pb2.GetIngredientRequest.FromString,
          response_serializer=ingredient__pb2.GetIngredientResponse.SerializeToString,
      ),
      'ListIngredient': grpc.unary_unary_rpc_method_handler(
          servicer.ListIngredient,
          request_deserializer=ingredient__pb2.ListIngredientRequest.FromString,
          response_serializer=ingredient__pb2.ListIngredientResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ingredient.IngredientService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IngredientService(object):
  """Missing associated documentation comment in .proto file."""

  @staticmethod
  def CreateIngredient(request,
      target,
      options=(),
      channel_credentials=None,
      call_credentials=None,
      insecure=False,
      compression=None,
      wait_for_ready=None,
      timeout=None,
      metadata=None):
    return grpc.experimental.unary_unary(request, target, '/ingredient.IngredientService/CreateIngredient',
      ingredient__pb2.CreateIngredientRequest.SerializeToString,
      ingredient__pb2.CreateIngredientResponse.FromString,
      options, channel_credentials,
      insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

  @staticmethod
  def GetIngredient(request,
      target,
      options=(),
      channel_credentials=None,
      call_credentials=None,
      insecure=False,
      compression=None,
      wait_for_ready=None,
      timeout=None,
      metadata=None):
    return grpc.experimental.unary_unary(request, target, '/ingredient.IngredientService/GetIngredient',
      ingredient__pb2.GetIngredientRequest.SerializeToString,
      ingredient__pb2.GetIngredientResponse.FromString,
      options, channel_credentials,
      insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

  @staticmethod
  def ListIngredient(request,
      target,
      options=(),
      channel_credentials=None,
      call_credentials=None,
      insecure=False,
      compression=None,
      wait_for_ready=None,
      timeout=None,
      metadata=None):
    return grpc.experimental.unary_unary(request, target, '/ingredient.IngredientService/ListIngredient',
      ingredient__pb2.ListIngredientRequest.SerializeToString,
      ingredient__pb2.ListIngredientResponse.FromString,
      options, channel_credentials,
      insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
