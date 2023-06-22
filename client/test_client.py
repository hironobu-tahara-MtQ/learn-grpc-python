import pytest
import grpc
from proto.calculator_pb2 import AddRequest
from proto.calculator_pb2_grpc import CalculatorStub


@pytest.fixture(scope='module')
def client():

    # gRPC クライアントを作成する
    channel = grpc.insecure_channel('172.17.0.2:50051')
    client = CalculatorStub(channel)

    yield client


def test_add(client):
    request = AddRequest(a=2, b=3)
    response = client.Add(request)
    assert response.result == 5

# 他のメソッドのテストケースも追加する


if __name__ == '__main__':
    pytest.main(["-s", "-v", "--rootdir=/app"])
