FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY proto/calculator_pb2.py calculator_pb2.py
COPY proto/calculator_pb2_grpc.py calculator_pb2_grpc.py

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "client.py" ]
