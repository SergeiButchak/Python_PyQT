"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress
import subprocess


def host_range_ping(host):
    try:
        ip = ipaddress.ip_address(host)
        ip._ip = ip._ip & 0xffffff00
        for _ in range(256):
            args = ['ping', '-c', '1', '-W', '.5', str(ip)]
            proc = subprocess.Popen(args, stdout=subprocess.PIPE)
            proc.wait()
            if proc.returncode == 0:
                print(f'{str(ip)} - Узел доступен')
            else:
                print(f'{str(ip)} - Узел не доступен')
            ip += 1
    except ValueError:
        print(f'{host} - Некорректный ip адрес')


host_range_ping('192.168.88.14')
