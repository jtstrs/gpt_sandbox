from app.tdlib_wrapper.td_wrapper import td_json_client_create, td_json_client_destroy

def main():
    client = td_json_client_create()
    td_json_client_destroy(client)

main()