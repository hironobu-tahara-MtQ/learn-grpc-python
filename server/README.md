# サーバー（呼ばれる側）

ビルド

```
    docker build -t grpc-python-server .
```

サーバー起動

```
    docker run -p 50051:50051 grpc-python-server
```
