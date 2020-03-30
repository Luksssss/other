# Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

# Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.
# Формат ввода

# Первая строка входного файла содержит одно число n, n ≤ 10000. Каждая из следующих n строк содержит ровно одно число — очередной элемент массива.
# Формат вывода

# Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц во входном массиве.

with open("/home/lukas/input.txt") as f:
    n = int(f.readline().strip())

    max_cnt = 0
    this_cnt = 0
    last_val = None
    while n > 0:
        this_val = f.readline().strip()
        print(last_val, this_val)
        if last_val == this_val:
            this_cnt += 1
        else:
            if this_cnt > max_cnt:
                max_cnt = this_cnt
            this_cnt = 1
        last_val = this_val
        n -= 1


print(max_cnt if max_cnt > this_cnt else this_cnt)
