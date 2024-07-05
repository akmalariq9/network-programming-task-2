from socket import socket, AF_INET, SOCK_STREAM

def main():
    server_address = ('localhost', 45000)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(server_address)

    try:
        while True:
            message = input("Enter command (TIME or QUIT): ")
            if message == "TIME":
                client_socket.sendall(f"TIME\r\n".encode('utf-8'))
                response = client_socket.recv(32)
                print("Received:", response.decode('utf-8'))
            elif message == "QUIT":
                client_socket.sendall(f"QUIT\r\n".encode('utf-8'))
                break
            else:
                print("Invalid command. Please enter TIME or QUIT.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
