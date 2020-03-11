from concurrent import futures

import grpc

import sample_pb2
import sample_pb2_grpc


class RouteGeneratorServer(sample_pb2_grpc.RouteGeneratorServicer):
    def Generate(self, request, context):
        print(request)
        return sample_pb2.RouteResponse(outlets=[
            sample_pb2.Outlet(id=1, name="Outlet1", latitude=27.18182, longitude=85.3423),
            sample_pb2.Outlet(id=2, name="Outlet2", latitude=27.11182, longitude=85.4523)
        ])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_RouteGeneratorServicer_to_server(RouteGeneratorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
