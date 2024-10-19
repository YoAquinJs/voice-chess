# comunicacion con el server(si se llega a utilizar)
import socket 
import select

def send_command_to_cpp(command):
    client_socket = None
    try:
        print("Connecting to the server in Python...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 8080))
        print("Connected to the C++ server.")

        client_socket.sendall(command.encode('utf-8'))
        print(f"Command sent: {command}")

        timeout = 2
        readable, _, _ = select.select([client_socket], [], [], timeout)
        if readable:
            response = client_socket.recv(1024).decode('utf-8')
            if not response:
                print("The connection was closed by the server.")
                return 
            print(f"Response from C++ server {response}")
            if "Closing connection" in response or command == "stop":
                print("The server has closed the connection. will not reconnect.")
                return
            else:
                print("Timeout while waiting for a response.")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        if client_socket:
            client_socket.close()