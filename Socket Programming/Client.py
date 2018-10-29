import socket
class Client:
    def create_client(self):
        """
        creating client side ,send and recieve  message from server
        :return:
        """

        # create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()

        port = 9999

        # connection to hostname on the port.
        client_socket.connect((host, port))

        # Receive no more than 1024 bytes
        msg = client_socket.recv(1024)

        client_socket.close()
        print(msg.decode('ascii'))



client_obj = Client()
client_obj.create_client()