from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number    # номер стола
        self.guest = None       # объект потока гостя за столом


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name        # имя гостя

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables        # содержит кортеж объектов столов
        self.queue = Queue()

    def guest_arrival(self, *guests):
        sit_guest = 0  # кол-во посаженных гостей
        for guest_i in guests:
            for table_i in self.tables:
                if table_i.guest is None:       # если стол свободен
                    table_i.guest = guest_i     # в атрибут guest помещаем поток
                    table_i.guest.start()       # запускаем поток
                    print(f'\033[32m{table_i.guest.name}\033[0m сел(-а) за стол номер '
                          f'{table_i.number}\n', end='')
                    sit_guest += 1
                    break
        if sit_guest < len(guests):
            for i in range(sit_guest, len(guests)):
                self.queue.put(guests[i])
                print(f'\033[32m{guests[i].name}\033[0m в очереди\n', end='')

    def discuss_guests(self):
        while True:
            for table_i in self.tables:
                if (table_i.guest is not None) and not table_i.guest.is_alive():
                    print(f'\033[32m{table_i.guest.name}\033[0m покушал(-а) и ушел(ушла)\n', end='')
                    print(f'Стол номер {table_i.number} свободен\n', end='')
                    table_i.guest = None
                    if not self.queue.empty():
                        qi = self.queue.get()
                        table_i.guest = qi
                        print(f'\033[32m{qi.name}\033[0m вышел(-ла) из очереди и сел(-а) за стол номер '
                              f'{table_i.number}\n', end='')
                        qi.start()
                        continue
            end = 0
            for _ in self.tables:
                if _.guest is None:
                    end += 1
                else:
                    break
            if end == len(self.tables): # выходим если кол-во столов равно количеству свободных столов
                break


# создаем списк из объектов класса Table
tables = [Table(number) for number in range(1, 6)]

# список гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# создаем список объектов потоков, один поток - один гость
guests = [Guest(name) for name in guests_names]

# создаем объект cafe и передаем список столов
cafe = Cafe(*tables)

# передаем список объектов потоков гостей
cafe.guest_arrival(*guests)

# обслуживание гостей
cafe.discuss_guests()

print('\033[31mКафе закрыто')
