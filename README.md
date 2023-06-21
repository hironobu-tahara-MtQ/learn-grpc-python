# Consider microservices.

Gradually isolate services. Or create a new one.
Investigate migrating to microservices Repository

## Install Protoc

Install what you need.

```
brew install protobuf
pip install grpcio
pip install grpcio-tools
```

## Server (the called party)

Go to the server directory.

```

cd server

```

Output files for Python.

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. . /proto/calculator.proto

```

Build.

```

docker build -t grpc-python-server .

```

Start the server.

```

docker run -p 50051:50051 grpc-python-server

```

## Client (caller)

Go to the client directory.

```

cd client
```

Output files for Python.

```

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. . /proto/calculator.proto

```

Check the container IP address of the server
**Correct 172.17.0.2 in client.py to the confirmed IP address**.

```

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container ID

```

build

```

docker build -t grpc-python-client .

```

Start the server.

```

docker run grpc-python-client

```
