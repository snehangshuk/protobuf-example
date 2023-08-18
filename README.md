# protobuf-example
Simple example to showcase protobuf

The `main.py` file creates a JSON file containing `Employee` object.

Then, we use `main2.py` to creates same file to hold `Employee` data using the its binary format.
And, we compare the size of the both the files (JSON file, and binary file usign protobuf).

To generate the protobuf class to be used in Python, we used `protoc` compile the schema defined in `employee.proto`.
Here the command:

`protoc --proto_path=./proto --python_out=. ./proto/employee.proto`
