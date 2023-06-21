# マイクロサービス化を検討する

サービスを徐々に分離する。または新規作成。
マイクロサービスへ移行するための調査 Repository

## Protoc をインストール

必要なものをインストールする

```
brew install protobuf
pip install grpcio
pip install grpcio-tools
```

## サーバー（呼ばれる側）

サーバーのディレクトリに移動

```
cd server
```

Python 用のファイルを出力する

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/calculator.proto
```

ビルド

```
docker build -t grpc-python-server .
```

サーバー起動

```
docker run -p 50051:50051 grpc-python-server
```

## クライアント（呼び出す側）

クライアントのディレクトリに移動

```
cd client
```

Python 用のファイルを出力する

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/calculator.proto
```

サーバーのコンテナ IP Address を確認
**client.py の 172.17.0.2 を確認した IP Address に修正**

```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' コンテナID

```

ビルド

```
docker build -t grpc-python-client .
```

サーバー起動

```
docker run grpc-python-client
```
