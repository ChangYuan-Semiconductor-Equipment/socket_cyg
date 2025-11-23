# pylint: skip-file
import time

from socket_cyg.socket_client import SocketClient


if __name__ == "__main__":

    client = SocketClient("127.0.0.1", 9001)
    if client.connect():
        try:
            client.send_data(b"ffffff")
            time.sleep(500000)
        finally:
            client.disconnect()