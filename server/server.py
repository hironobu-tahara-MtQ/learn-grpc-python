import grpc
from concurrent import futures

from calculator_pb2 import AddRequest, AddResponse, SubtractRequest, SubtractResponse, MultiplyRequest, MultiplyResponse, DivideRequest, DivideResponse
from calculator_pb2_grpc import CalculatorServicer, add_CalculatorServicer_to_server


class CalculatorServicer(CalculatorServicer):
    def Add(self, request: AddRequest, context) -> AddResponse:
        result = request.a + request.b
        return AddResponse(result=result)

    def Subtract(self, request: SubtractRequest, context) -> SubtractResponse:
        result = request.a - request.b
        return SubtractResponse(result=result)

    def Multiply(self, request: MultiplyRequest, context) -> MultiplyResponse:

        result = request.a * request.b
        return MultiplyResponse(result=result)

    def Divide(self, request: DivideRequest, context) -> DivideResponse:
        dividend = request.a
        divisor = request.b
        if divisor == 0:
            # ゼロ除算のエラーレスポンスを返す
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Cannot divide by zero.")
            return DivideResponse()
        result = dividend / divisor
        return DivideResponse(result=result)


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
    add_CalculatorServicer_to_server(
        CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
