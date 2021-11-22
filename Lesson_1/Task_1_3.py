"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable       Unreachable
-------------   -------------
10.0.0.1        10.0.0.3
10.0.0.2        10.0.0.4
"""
import ipaddress
import subprocess
import tabulate


def host_range_ping_tab(host):
    table = {
        'Reachable': [],
        'Unreachable': [],
    }
    try:
        ip = ipaddress.ip_address(host)
        ip._ip = ip._ip & 0xffffff00
        for _ in range(256):
            args = ['ping', '-c', '1', '-W', '.5', str(ip)]
            proc = subprocess.Popen(args, stdout=subprocess.PIPE)
            proc.wait()
            if proc.returncode == 0:
                table['Reachable'].append(str(ip))
            else:
                table['Unreachable'].append(str(ip))
            ip += 1
        print(tabulate.tabulate(table, headers='keys'))
    except ValueError:
        print(f'{host} - Некорректный ip адрес')


host_range_ping_tab('192.168.88.14')
