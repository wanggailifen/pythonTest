import socket

socket_server = socket.socket()
socket_server.bind(("127.0.0.1", 8080))
socket_server.listen(2)
conn, address = socket_server.accept()
print(f"接收到客户端连接 address = {address}")

while True:
    # 1024 bytes 缓冲区大小
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"接收到消息 data = {data}")

    msg = input("请输入需要回复的消息")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))

conn.close()
socket_server.close()
