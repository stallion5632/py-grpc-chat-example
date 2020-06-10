# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/grpc_out/chat.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/grpc_out/chat.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1a\x63lient/grpc_out/chat.proto\x12\x04grpc\"\x07\n\x05\x45mpty\"\t\n\x07Nothing\"\'\n\x07Message\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t2f\n\x08\x43hatting\x12-\n\rMessageStream\x12\x0b.grpc.Empty\x1a\r.grpc.Message0\x01\x12+\n\x0bSendMessage\x12\r.grpc.Message\x1a\r.grpc.Nothingb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=43,
)


_NOTHING = _descriptor.Descriptor(
  name='Nothing',
  full_name='grpc.Nothing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=54,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='grpc.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='grpc.Message.author', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='grpc.Message.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Nothing'] = _NOTHING
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'client.grpc_out.chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

Nothing = _reflection.GeneratedProtocolMessageType('Nothing', (_message.Message,), {
  'DESCRIPTOR' : _NOTHING,
  '__module__' : 'client.grpc_out.chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Nothing)
  })
_sym_db.RegisterMessage(Nothing)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'client.grpc_out.chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Message)
  })
_sym_db.RegisterMessage(Message)



_CHATTING = _descriptor.ServiceDescriptor(
  name='Chatting',
  full_name='grpc.Chatting',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=97,
  serialized_end=199,
  methods=[
  _descriptor.MethodDescriptor(
    name='MessageStream',
    full_name='grpc.Chatting.MessageStream',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='grpc.Chatting.SendMessage',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_NOTHING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATTING)

DESCRIPTOR.services_by_name['Chatting'] = _CHATTING

# @@protoc_insertion_point(module_scope)
