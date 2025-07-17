"""udp服务端"""

import socket

# 创建udp套接字
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 绑定ip和端口
udp_socket.bind(("127.0.0.1", 8888))
while True:
    # 接收数据
    recv_data, client_addr = udp_socket.recvfrom(1024)
    client_ip = client_addr[0]
    client_port = client_addr[1]
    print(f"{client_ip}:{client_port}>> {recv_data.decode("utf-8")}")
    # 发送数据
    udp_socket.sendto("你好".encode("utf-8"), client_addr)
# 关闭套接字
udp_socket.close()
