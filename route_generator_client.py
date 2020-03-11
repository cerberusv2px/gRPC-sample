import grpc

import sample_pb2
import sample_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sample_pb2_grpc.RouteGeneratorStub(channel)
        response = stub.Generate(sample_pb2.RouteRequest(
            num_dse=5,
            max_distance=5000,
            max_outlet=40,
            start_locations=[0, 0, 0, 0, 0],
            end_locations=[0, 0, 0, 0, 0],
            outlets=[
                sample_pb2.Outlet(id=1, name="Outlet1", latitude=27.18182, longitude=85.3423),
                sample_pb2.Outlet(id=2, name="Outlet2", latitude=27.11182, longitude=85.4523),
                sample_pb2.Outlet(id=3, name="Outlet3", latitude=27.14182, longitude=85.4523)
            ]
        ))
    for outlet in response.outlets:
        print(str(outlet))


if __name__ == '__main__':
    run()
