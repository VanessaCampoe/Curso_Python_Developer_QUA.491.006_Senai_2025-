import os 
import platform
import psutil
import socket

print(f"Sistema Operacional: {platform.system()} {platform.release()}")
print(f"Nome do usuário: {os.environ.get('USERNAME')}")
print(f"IPv4: {socket.gethostbyname(socket.gethostname())}")


#  coleta as portas abertas 


print(f"Portas abertas:\n")
cannectall = psutil.net_connections(kind='inet')
only_udp = [conn for conn in psutil.net_connections(kind='inet') if conn.type == socket.SOCK_DGRAM]


# separa as informações sobre as portas

only_tcp_listening_ports = [conn.laddr for conn in cannectall if conn.status == psutil.CONN_LISTEN] # tcp


only_udp_listening_ports = [conn.laddr for conn in only_udp ] # udp

# remover as portas repetidas da lista
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

# organiza as portas da sequencia
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()
# exibe as portas
print(f"Portas TCP em escuta: {only_tcp_listening_ports}")
for port in only_udp_listening_ports:
    print(f"Portas UDP : {port} aberta.")
    

print(f"Portas UDP : {only_udp_listening_ports}")
for port in only_udp_listening_ports:
    print(f"Portas UDP : {port} aberta.")

# mostrar as portas em escuta