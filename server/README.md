# サーバー（呼ばれる側）

必要なものをインストールする

```
brew install protobuf
pip install grpcio
pip install grpcio-tools
```

ビルド

```
docker build -t grpc-python-server .
```

サーバー起動

```
docker run -p 50051:50051 grpc-python-server
```
