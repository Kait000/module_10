from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, str, int):
        self.str = str
        self.int = int
        super().__init__()

    def run(self):
        power = 100
        day = 0
        print(f'{self.str}, на нас напали!')
        while power > 0:
            power -= self.int
            day += 1
            sleep(1)
            # без данной запись в print(...\n', end='') перенос не всегда срабатывает вовремя
            print(f'{self.str} сражается {day} {self.year_ending(day)}..., осталось {power} воинов.\n', end='')
        print(f'{self.str} одержал победу спустя {day} {self.year_ending(day)}!\n', end='')

    def year_ending(self, num_day):
        if 11 <= num_day <= 14:
            return 'дней'
        while num_day >= 10:
            num_day -= 10
        match num_day:
            case 1: return 'день'
            case 2 | 3 | 4: return 'дня'
            case 0 | 5 | 6 | 7 | 8 | 9: return 'дней'


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')


# # проверка окончания для дат
# for i in range(100):
#     print(i, first_knight.year_ending(i))
