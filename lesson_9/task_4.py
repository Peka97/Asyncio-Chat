from subprocess import Popen


def launcher_for_two_clients():
    running = True
    processes = []

    while running:
        user_enter = input(
            f'{"=" * 100}\n \
            \rМеню:\n\
            \r > start - Запуск сервера и двух клиентов\n\
            \r > quit - Выход\n\
            \r{"-" * 40}\n\
            \r Введите название одного из пунктов: '
        )
        if user_enter == 'start':
            processes.append(
                Popen('python3 ../lesson_3/server.py',
                      shell=True)
            )
            processes.append(
                Popen("python3 ../lesson_3/client.py localhost 7777 R",
                      shell=True)
            )
            processes.append(
                Popen("python3 ../lesson_3/client.py localhost 7777 W",
                      shell=True)
            )
        elif user_enter == 'quit':
            running = False
        else:
            print('\n-= Недопустимый ввод =-\n')

    [process.kill() for process in processes]


def launcher_for_n_clients(count: int):
    running = True
    processes = []

    while running:
        user_enter = input(
            f'{"=" * 100}\n \
            \rМеню:\n\
            \r > start - Запуск сервера и двух клиентов\n\
            \r > quit - Выход\n\
            \r{"-" * 40}\n\
            \r Введите название одного из пунктов: '
        )
        if user_enter == 'start':
            processes.append(
                Popen('python3 ../lesson_7/server.py',
                      shell=True)
            )
            for i in range(count):
                processes.append(
                    Popen("python3 ../lesson_7/client.py",
                          shell=True)
                )
        elif user_enter == 'quit':
            running = False
        else:
            print('\n-= Недопустимый ввод =-\n')

    [process.kill() for process in processes]


if __name__ == '__main__':
    # launcher_for_two_clients()
    launcher_for_n_clients(2)
