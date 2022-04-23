# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/sandbox.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tinkoff.invest.grpc import common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2
from tinkoff.invest.grpc import orders_pb2 as tinkoff_dot_invest_dot_grpc_dot_orders__pb2
from tinkoff.invest.grpc import operations_pb2 as tinkoff_dot_invest_dot_grpc_dot_operations__pb2
from tinkoff.invest.grpc import users_pb2 as tinkoff_dot_invest_dot_grpc_dot_users__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!tinkoff/invest/grpc/sandbox.proto\x12%tinkoff.public.invest.api.contract.v1\x1a tinkoff/invest/grpc/common.proto\x1a tinkoff/invest/grpc/orders.proto\x1a$tinkoff/invest/grpc/operations.proto\x1a\x1ftinkoff/invest/grpc/users.proto\"\x1b\n\x19OpenSandboxAccountRequest\"0\n\x1aOpenSandboxAccountResponse\x12\x12\n\naccount_id\x18\x01 \x01(\t\"0\n\x1a\x43loseSandboxAccountRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\x1d\n\x1b\x43loseSandboxAccountResponse\"l\n\x13SandboxPayInRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x41\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"Z\n\x14SandboxPayInResponse\x12\x42\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue2\xae\x0c\n\x0eSandboxService\x12\x99\x01\n\x12OpenSandboxAccount\x12@.tinkoff.public.invest.api.contract.v1.OpenSandboxAccountRequest\x1a\x41.tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse\x12\x8b\x01\n\x12GetSandboxAccounts\x12\x39.tinkoff.public.invest.api.contract.v1.GetAccountsRequest\x1a:.tinkoff.public.invest.api.contract.v1.GetAccountsResponse\x12\x9c\x01\n\x13\x43loseSandboxAccount\x12\x41.tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest\x1a\x42.tinkoff.public.invest.api.contract.v1.CloseSandboxAccountResponse\x12\x85\x01\n\x10PostSandboxOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x85\x01\n\x10GetSandboxOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x8b\x01\n\x12\x43\x61ncelSandboxOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x86\x01\n\x14GetSandboxOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12\x88\x01\n\x13GetSandboxPositions\x12\x37.tinkoff.public.invest.api.contract.v1.PositionsRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PositionsResponse\x12\x8b\x01\n\x14GetSandboxOperations\x12\x38.tinkoff.public.invest.api.contract.v1.OperationsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.OperationsResponse\x12\x88\x01\n\x13GetSandboxPortfolio\x12\x37.tinkoff.public.invest.api.contract.v1.PortfolioRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponse\x12\x87\x01\n\x0cSandboxPayIn\x12:.tinkoff.public.invest.api.contract.v1.SandboxPayInRequest\x1a;.tinkoff.public.invest.api.contract.v1.SandboxPayInResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')



_OPENSANDBOXACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['OpenSandboxAccountRequest']
_OPENSANDBOXACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['OpenSandboxAccountResponse']
_CLOSESANDBOXACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['CloseSandboxAccountRequest']
_CLOSESANDBOXACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['CloseSandboxAccountResponse']
_SANDBOXPAYINREQUEST = DESCRIPTOR.message_types_by_name['SandboxPayInRequest']
_SANDBOXPAYINRESPONSE = DESCRIPTOR.message_types_by_name['SandboxPayInResponse']
OpenSandboxAccountRequest = _reflection.GeneratedProtocolMessageType('OpenSandboxAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENSANDBOXACCOUNTREQUEST,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OpenSandboxAccountRequest)
  })
_sym_db.RegisterMessage(OpenSandboxAccountRequest)

OpenSandboxAccountResponse = _reflection.GeneratedProtocolMessageType('OpenSandboxAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENSANDBOXACCOUNTRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse)
  })
_sym_db.RegisterMessage(OpenSandboxAccountResponse)

CloseSandboxAccountRequest = _reflection.GeneratedProtocolMessageType('CloseSandboxAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESANDBOXACCOUNTREQUEST,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest)
  })
_sym_db.RegisterMessage(CloseSandboxAccountRequest)

CloseSandboxAccountResponse = _reflection.GeneratedProtocolMessageType('CloseSandboxAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESANDBOXACCOUNTRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CloseSandboxAccountResponse)
  })
_sym_db.RegisterMessage(CloseSandboxAccountResponse)

SandboxPayInRequest = _reflection.GeneratedProtocolMessageType('SandboxPayInRequest', (_message.Message,), {
  'DESCRIPTOR' : _SANDBOXPAYINREQUEST,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SandboxPayInRequest)
  })
_sym_db.RegisterMessage(SandboxPayInRequest)

SandboxPayInResponse = _reflection.GeneratedProtocolMessageType('SandboxPayInResponse', (_message.Message,), {
  'DESCRIPTOR' : _SANDBOXPAYINRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SandboxPayInResponse)
  })
_sym_db.RegisterMessage(SandboxPayInResponse)

_SANDBOXSERVICE = DESCRIPTOR.services_by_name['SandboxService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _OPENSANDBOXACCOUNTREQUEST._serialized_start=215
  _OPENSANDBOXACCOUNTREQUEST._serialized_end=242
  _OPENSANDBOXACCOUNTRESPONSE._serialized_start=244
  _OPENSANDBOXACCOUNTRESPONSE._serialized_end=292
  _CLOSESANDBOXACCOUNTREQUEST._serialized_start=294
  _CLOSESANDBOXACCOUNTREQUEST._serialized_end=342
  _CLOSESANDBOXACCOUNTRESPONSE._serialized_start=344
  _CLOSESANDBOXACCOUNTRESPONSE._serialized_end=373
  _SANDBOXPAYINREQUEST._serialized_start=375
  _SANDBOXPAYINREQUEST._serialized_end=483
  _SANDBOXPAYINRESPONSE._serialized_start=485
  _SANDBOXPAYINRESPONSE._serialized_end=575
  _SANDBOXSERVICE._serialized_start=578
  _SANDBOXSERVICE._serialized_end=2160
# @@protoc_insertion_point(module_scope)
