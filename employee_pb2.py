# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: employee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x65mployee.proto\"3\n\x08\x45mployee\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\")\n\tEmployees\x12\x1c\n\temployees\x18\x01 \x03(\x0b\x32\t.Employeeb\x06proto3')



_EMPLOYEE = DESCRIPTOR.message_types_by_name['Employee']
_EMPLOYEES = DESCRIPTOR.message_types_by_name['Employees']
Employee = _reflection.GeneratedProtocolMessageType('Employee', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYEE,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:Employee)
  })
_sym_db.RegisterMessage(Employee)

Employees = _reflection.GeneratedProtocolMessageType('Employees', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYEES,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:Employees)
  })
_sym_db.RegisterMessage(Employees)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPLOYEE._serialized_start=18
  _EMPLOYEE._serialized_end=69
  _EMPLOYEES._serialized_start=71
  _EMPLOYEES._serialized_end=112
# @@protoc_insertion_point(module_scope)
