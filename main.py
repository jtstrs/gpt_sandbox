from app.tdlib_wrapper.td_wrapper import *

def main():
    timeout = 3000

    client = td_json_client_create()

    res = td_json_client_receive(client,  timeout)
    print("RESULT", res)

    td_json_client_destroy(client)

main()