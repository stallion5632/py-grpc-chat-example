# A simple console chat on Python and gRPC

A simple console chat on Python and gRPC

## Requirements

- Python 3.7+

## Installing dependencies
```shell script
pip install -r requirements.txt
```

## Generation python modules on proto files
```shell script
compile_proto.bat
```

## Run

##### Running  server
```shell script
python -m server
```

##### Running  client
```shell script
python -m client
```

### About generated files

Two files are generated
- Ending on '_pb2.py': module describing types and services
- Ending on '_pb2_grpc.py': a module that implements gRPC.



