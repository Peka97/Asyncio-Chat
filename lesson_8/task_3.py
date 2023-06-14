from tabulate import tabulate

from task_2 import host_range_ping


def host_range_ping_tab(*args, **kwargs) -> None:
    result = host_range_ping(*args, **kwargs)
    return tabulate(result, 'keys')


if __name__ == '__main__':
    yandex_ip = '77.88.55.88'
    yandex_adr = 'yandex.ru'
    wrong_yandex = '77.88.55.87'

    print(host_range_ping_tab(yandex_ip, yandex_adr, wrong_yandex, max_count=3))
