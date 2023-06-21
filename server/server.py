import grpc
from concurrent import futures

import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calculator_pb2.AddResponse(result=result)

    def Subtract(self, request, context):
        response = calculator_pb2.SubtractResponse()
        response.result = request.a - request.b
        return response

    def Multiply(self, request, context):
        response = calculator_pb2.MultiplyResponse()
        response.result = request.a * request.b
        return response

    def Divide(self, request, context):
        dividend = request.a
        divisor = request.b
        if divisor == 0:
            # ゼロ除算のエラーレスポンスを返す
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Cannot divide by zero.")
            return calculator_pb2.DivideResponse()
        result = dividend / divisor
        return calculator_pb2.DivideResponse(result=result)


if __name__ == '__main__':
    # 鍵と証明書のpath
    # cert_file = '/path/to/server.crt'
    # key_file = '/path/to/server.key'

    # # gRPCサーバーの設定
    # server = grpc.server(futures.ThreadPoolExecutor())

    # # 証明書と秘密鍵の読み込み
    # with open(cert_file, 'rb') as f:
    #     cert_data = f.read()
    # with open(key_file, 'rb') as f:
    #     key_data = f.read()

    # # SSL/TLSの設定
    # credentials = grpc.ssl_server_credentials(((key_data, cert_data,),))
    # server.add_secure_port('[::]:50051', credentials)

    server = grpc.server(futures.ThreadPoolExecutor())
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
