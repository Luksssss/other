# РАБОЧИЙ ВАРИАНТ
# На входе: неубывающий массив с дублями чисел
# Удаление дублей, сортировка, считывание файла по частям.
# NOTE: можно попробовать ещё через from itertools import islice
# with open('input.txt') as f:
with open('/home/lukas/input2.txt') as f:    
    n = f.readline().strip()
    un_data = []
    last_el = None
    while True:
        raw_data = f.read(10240)
        if not raw_data:
            break
        else:
            if raw_data[-1] != '\n':
                # можем не захватить всю строку
                # поэтому добиваем до конца
                while True:
                    raw_data = raw_data + f.read(1)
                    if raw_data[-1] == '\n':
                        break
            for el in raw_data.strip().split():
				if el != last_el:
					un_data.append(el)
					last_el = el

print "\n".join(un_data)