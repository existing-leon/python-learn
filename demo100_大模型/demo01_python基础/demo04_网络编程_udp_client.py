"""udp客户端"""

import socket

# 创建udp套接字
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while True:
    try:
        # 发送数据
        server_ip = "127.0.0.1"
        server_port = 8888
        udp_socket.sendto(input(f"{server_ip}:{server_port}<< ").encode("utf-8"), (server_ip, server_port))
        # 接收数据
        recv_data, client_addr = udp_socket.recvfrom(1024)
        client_ip = client_addr[0]
        client_port = client_addr[1]
        print(f"{client_ip}:{client_port}>> {recv_data.decode("utf-8")}")
    except KeyboardInterrupt:
        break
# 关闭套接字
udp_socket.close()
