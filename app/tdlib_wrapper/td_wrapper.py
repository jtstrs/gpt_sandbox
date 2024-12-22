import ctypes


td_lib_dll = ctypes.CDLL("libs/libTDLibWrapper.so")

td_lib_dll.td_create_client_id_wrapper.restype = ctypes.c_int32

td_lib_dll.td_send_wrapper.argtypes = [ctypes.c_int32, ctypes.c_char_p]

td_lib_dll.td_receive_wrapper.restype = ctypes.c_char_p
td_lib_dll.td_receive_wrapper.argtypes = [ctypes.c_double]

td_lib_dll.td_execute_wrapper.restype = ctypes.c_char_p
td_lib_dll.td_execute_wrapper.argtypes = [ctypes.c_char_p]

td_lib_dll.td_json_client_create_wrapper.restype = ctypes.c_void_p

td_lib_dll.td_json_client_destroy_wrapper.argtypes = [ctypes.c_void_p]

td_lib_dll.td_json_client_send_wrapper.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

td_lib_dll.td_json_client_receive_wrapper.restype = ctypes.c_char_p
td_lib_dll.td_json_client_receive_wrapper.argtypes = [ctypes.c_void_p, ctypes.c_double]

td_lib_dll.td_json_client_execute_wrapper.restype = ctypes.c_char_p
td_lib_dll.td_json_client_execute_wrapper.argtypes = [ctypes.c_void_p, ctypes.c_char_p]


def td_create_client_id() -> int:
    return td_lib_dll.td_create_client_id_wrapper()

def td_send(client_id: int, request: str):
    td_lib_dll.td_send_wrapper(client_id, request)

def td_receive(timeout: float) -> str:
    td_lib_dll.td_receive_wrapper(timeout)

def td_execute(request: str) -> str:
    td_lib_dll.td_execute_wrapper(request)

def td_set_log_message_callback(max_verbosity_level: int, callback):
    td_lib_dll.td_set_log_message_callback_wrapper(max_verbosity_level, callback)

def td_json_client_create():
    return td_lib_dll.td_json_client_create_wrapper()

def td_json_client_destroy(client):
    td_lib_dll.td_json_client_destroy_wrapper(client)

def td_json_client_send(client, message):
    td_lib_dll.td_json_client_send_wrapper(client, message)

def td_json_client_receive(client, message):
    return td_lib_dll.td_json_client_receive_wrapper(client, message)

def td_json_client_execute(client, message):
    return td_lib_dll.td_json_client_execute_wrapper(client, message)
