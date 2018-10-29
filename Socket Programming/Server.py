import socket

class ServerAndClient:
    """
    class for creating Server
    """

    def creating_server(self):
        """
        method for creating the server and for binding,listening the request
        :return:
        """



        # create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()

        port = 65432

        # bind to the port
        server_socket.bind((host, port))

        #  5 requests
        server_socket.listen(5)

        while True:
            # establish a connection
            client_socket, address = server_socket.accept()

            print("Got a connection from " + str(address))

            msg = 'Thank you for connecting' + " " + str(host)
            client_socket.send(msg.encode('ascii'))
            client_socket.close()







obj = ServerAndClient()
obj.creating_server()