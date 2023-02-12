import socket

socket_client = socket.socket()

socket_client.connect(("127.0.0.1", 8080))

while True:
    try:
        msg = input("请输入要给服务端发送的消息")
        if msg == "exit":
            break
        socket_client.send(msg.encode("UTF-8"))
        recv_data = socket_client.recv(1024)
        print(f"服务端恢复了消息 {recv_data.decode('UTF-8')}")
    except Exception as e:
        print(e)
