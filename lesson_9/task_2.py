import re

from task_1 import host_ping


def host_range_ping(*args, max_count=255) -> None:
    addresses = dict().fromkeys(args)
    pattern_ip = re.compile(r'\d+.\d+.\d+.\d+')

    for ip in args:
        count = 1

        try:
            if not pattern_ip.match(ip):
                raise ValueError

            addresses[ip] = []

            last_oct = int(ip.split('.')[-1])

            while 0 < last_oct < 256 and count <= max_count:
                next_ip = f"{'.'.join(ip.split('.')[:3])}.{last_oct}"
                addresses[ip].append(next_ip)
                last_oct += 1
                count += 1

        except ValueError:
            continue

    to_ping = []
    [to_ping.extend(ip) for ip in addresses.values() if isinstance(ip, list)]
    to_ping = list(set(to_ping))  # Убираем дубли, оптимизируя работу скрипта

    return host_ping(*to_ping)


if __name__ == '__main__':
    yandex_ip = '77.88.55.88'
    yandex_adr = 'yandex.ru'
    wrong_yandex = '77.88.55.87'

    host_range_ping(yandex_ip, yandex_adr, wrong_yandex, max_count=3)
