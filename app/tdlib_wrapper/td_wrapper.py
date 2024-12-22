import ctypes
import os

td_lib_dll = ctypes.CDLL("libs/libTDLibWrapper.so")

def create_client_id():
    td_lib_dll.td_create_client_id_wrapper()
