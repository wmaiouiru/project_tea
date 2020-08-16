



# Generating grpc stub functions
Run the following from root path to generate the grpc client and server files.
```
python -m grpc_tools.protoc -I./proto  --python_out=./src/python/ --grpc_python_out=./src/python/ ./proto/ingredient.proto
```