from time import sleep
from datetime import datetime
from threading import Thread


def write_words(ord_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(ord_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
        print(f'Завершена запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Время выполнения функций: {time_end-time_start}')

time_start = datetime.now()
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
time_end = datetime.now()
print(f'Время выполнения потоков: {time_end-time_start}')
