import grpc

from calculator_pb2 import AddRequest, AddResponse, SubtractRequest, SubtractResponse, MultiplyRequest, MultiplyResponse, DivideRequest, DivideResponse
from calculator_pb2_grpc import CalculatorStub


def run():
    # # サーバーのアドレスとポート番号
    # server_address = '172.17.0.2:50051'

    # # サーバーの証明書ファイルパス
    # cert_file = '/path/to/server.crt'

    # # 証明書の読み込み
    # with open(cert_file, 'rb') as f:
    #     cert_data = f.read()

    # # SSL/TLSの設定
    # credentials = grpc.ssl_channel_credentials(root_certificates=cert_data)
    # channel = grpc.secure_channel(server_address, credentials)

    # # サービスの利用やリクエストの送信の処理を追加する

    # # クライアントの接続の確立
    # stub = calculator_pb2_grpc.CalculatorStub(channel)

    channel = grpc.insecure_channel('172.17.0.2:50051')
    stub = CalculatorStub(channel)
    try:
        # gRPCサーバーのメソッドを呼び出す例
        request = DivideRequest(a=10, b=0)
        response: DivideResponse = stub.Divide(request)
        print("Response:", response.result)
        print("Type:", type(response))
        print("All:", response)
    except grpc.RpcError as e:
        print("共通のエラーハンドリング:", e)


if __name__ == '__main__':
    run()
