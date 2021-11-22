"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
import ipaddress
import socket
import subprocess


def host_ping(host_list):
    for host in host_list:
        try:
            ip = ipaddress.ip_address(host)
        except ValueError:
            try:
                ip = socket.gethostbyname(host)
            except socket.gaierror:
                print(f'{host} - Узел не доступен')
                continue
        args = ['ping', '-c', '1', '-W', '.5', str(ip)]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        proc.wait()
        if proc.returncode == 0:
            print(f'{host} - Узел доступен')
        else:
            print(f'{host} - Узел не доступен')


host_ping(['yandex.ru', '198.167.0.1', 'mail.ru'])
