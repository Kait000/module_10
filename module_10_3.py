from time import sleep
from random import randint
from threading import Thread, Lock


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            sum = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += sum
            print(f'Пополнение: {sum}. Баланс: {self.balance}\n', end='')
            sleep(0.001)

    def take(self):
        for i in range(100):
            take_sum = randint(50, 500)
            print(f'Запрос на {take_sum}\n', end='')
            if take_sum <= self.balance:
                self.balance -= take_sum
                print(f'Снятие: {take_sum}. Баланс: {self.balance}\n', end='')
            else:
                print('Запрос отклонён, недостаточно средств\n', end='')
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
