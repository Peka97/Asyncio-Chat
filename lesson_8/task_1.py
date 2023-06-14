import re
from subprocess import call, PIPE
from ipaddress import ip_address


def host_ping(*args) -> None:
    pattern_ip = re.compile(r'\d+.\d+.\d+.\d+')
    result = {
        'available': [],
        'unavailable': []
    }
    for ip in args:
        if pattern_ip.match(ip):
            ip = ip_address(ip)

        status_code = call(['ping', '-c', '1', str(ip)], stdout=PIPE)

        if status_code == 0:
            result['available'].append(str(ip))
        else:
            result['unavailable'].append(str(ip))

    return result


if __name__ == '__main__':
    yandex_ip = '77.88.55.88'
    yandex_adr = 'yandex.ru'
    wrong_yandex = '77.88.55.87'

    result = host_ping(yandex_ip, yandex_adr, wrong_yandex)

    for status, adresses in result.items():
        for ip in adresses:
            print(f'{ip} - {status}')
