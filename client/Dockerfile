FROM python:3.9

WORKDIR /app

# gRPC関連のファイルをコピー
COPY requirements.txt .
COPY proto/calculator_pb2.py proto/calculator_pb2.py
COPY proto/calculator_pb2_grpc.py proto/calculator_pb2_grpc.py

# テスト用のファイルをコピー
COPY client.py client.py
COPY test_client.py test_client.py

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "python client.py & pytest -s -v --rootdir=/app"]
