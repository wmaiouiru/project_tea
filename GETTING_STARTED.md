



# Generating grpc stub functions
Run the following from root path to generate the grpc client and server files.
```
python -m grpc_tools.protoc -I./proto  --python_out=./src/python/services/ --grpc_python_out=./src/python/services/ ./proto/ingredient.proto
```

## TODO grpc run_codegen.py
```
"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc

protoc.main((
    '',
    '-I../../protos',
    '--python_out=.',
    '--grpc_python_out=.',
    '../../protos/route_guide.proto',
))
```
where
  -I is the reference to proto
  --python_out is where the protobuf will be generated to
  --grpc_python_out is where the grpc will be generated to
  last argument is the proto file