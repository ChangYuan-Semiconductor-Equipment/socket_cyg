"""client_example."""
import os

from socket_cyg.socket_client import SocketClient


if __name__ == '__main__':
    file_path = r"D:\python_workspace\equipment_cyg.rar"

    client1 = SocketClient()
    client1.client_open()
    client1.run_receive_thread()
    with open(file_path, mode="rb+") as f:
        data = f.read()
        dir_path = f"{os.getcwd()}/a"
        client1.client_send(dir_path.encode("UTF-8") + b"-_-" + data + b"@__@")

    client2 = SocketClient()
    client2.client_open()
    client2.run_receive_thread()
    with open(file_path, mode="rb+") as f:
        data = f.read()
        dir_path = f"{os.getcwd()}/b"
        client2.client_send(dir_path.encode("UTF-8") + b"-_-" + data + b"@__@")

    client3 = SocketClient()
    client3.client_open()
    client3.run_receive_thread()
    with open(file_path, mode="rb+") as f:
        data = f.read()
        dir_path = f"{os.getcwd()}/c"
        client3.client_send(dir_path.encode("UTF-8") + b"-_-" + data + b"@__@")

    client4 = SocketClient()
    client4.client_open()
    client4.run_receive_thread()
    with open(file_path, mode="rb+") as f:
        data = f.read()
        dir_path = f"{os.getcwd()}/d"
        client4.client_send(dir_path.encode("UTF-8") + b"-_-" + data + b"@__@")