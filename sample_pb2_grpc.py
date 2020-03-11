# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sample_pb2 as sample__pb2


class RouteGeneratorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Generate = channel.unary_unary(
        '/RouteGenerator/Generate',
        request_serializer=sample__pb2.RouteRequest.SerializeToString,
        response_deserializer=sample__pb2.RouteResponse.FromString,
        )


class RouteGeneratorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Generate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RouteGeneratorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Generate': grpc.unary_unary_rpc_method_handler(
          servicer.Generate,
          request_deserializer=sample__pb2.RouteRequest.FromString,
          response_serializer=sample__pb2.RouteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RouteGenerator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
