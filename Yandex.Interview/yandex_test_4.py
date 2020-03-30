# from bisect import insort

# # Слияние k сортированных списков
# with open('/home/lukas/input3.txt') as f:    
#     n = int(f.readline().strip())
#     len_ind_max = None
#     len_max = 0
#     res = []
#     for i in range(n):
#         this_len = int(f.read(1))

#         if this_len > len_max:
#             len_ind_max = i
#             len_max = this_len
#         tmp = map(int, f.readline().strip().split())
#         res.append(tmp)
# if len_ind_max:
#     big_mas = res.pop(len_ind_max)
# else:
#     big_mas = []

# for rr in res:
#     for el in rr:
#         insort(big_mas, el)

# print " ". join(map(str, big_mas))


from collections import Counter

# Слияние k сортированных списков
# РАБОЧИй ВАРИАНТ
with open('/home/lukas/input3.txt') as f:    
    n = int(f.readline().strip())
    a = Counter()
    res = ''
    for _ in range(n):
        a += Counter(f.readline().strip()[1:])
    del a[' ']
    for key, c in sorted(a.items(), key = lambda el: int(el[0])):
        # print("{} ".format(key * c))
        res += (key + ' ') * c
    res.strip()