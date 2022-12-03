# ** means collecting data in dictionary
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', '3000'),
        'user': options.get('user', 'guest'),
    }
    print(conn_params)
    # db.connect()


connect()
connect( user='Marwan Hisham', port=8080)