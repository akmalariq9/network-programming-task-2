from socket import socket, AF_INET, SOCK_STREAM
import threading
import logging
import time

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        try:
            while True:
                data = self.connection.recv(32)
                if data:
                    message = data.decode('utf-8')
                    if message.startswith("TIME") and message.endswith("\r\n"):
                        # Print or log the request received
                        print("Request Received")
                        logging.info("Request Received")

                        current_time = time.strftime("%H:%M:%S")
                        response = f"JAM {current_time}\r\n"
                        self.connection.sendall(response.encode('utf-8'))
                    elif message.startswith("QUIT") and message.endswith("\r\n"):
                        break
                else:
                    break
        except Exception as e:
            logging.warning(f"Error: {e}")
        finally:
            self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket(AF_INET, SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 45000))
        self.my_socket.listen(1)
        logging.warning("Server is running on port 45000")
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"Connection from {self.client_address}")
            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    logging.basicConfig(level=logging.INFO)
    svr = Server()
    svr.start()

if __name__ == "__main__":
    main()
