# クライアント（呼び出す側）

必要なものをインストールする

```
brew install protobuf
pip install grpcio
pip install grpcio-tools
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
