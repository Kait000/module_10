from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)
    file.close()


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    t_start = datetime.now()
    for i in filenames:
        read_info(i)
    t_end = datetime.now()
    print(f'Последовательная обработка {t_end-t_start}')

    with multiprocessing.Pool(processes=4) as pool:
        t_start = datetime.now()
        pool.map(read_info, filenames)
    t_end = datetime.now()
    print(f'Обработка в процессах {t_end-t_start}')
