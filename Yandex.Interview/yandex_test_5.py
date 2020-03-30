
# Генерация скобочных последовательностей (на рекурсии)
with open('/home/lukas/input5.txt') as ff:
	k = int(ff.readline().strip()) * 2

init = [None for _ in range(k)] # пустой список, куда кладем скобки
cnt = 0 # разница между скобками
ind = 0 # индекс, по которому кладем скобку в список 

def f(cnt, ind, k, init):
    # кладем откр. скобку, только если хватает места
    if (cnt <= k-ind-2):
        init[ind] = '('
        f(cnt+1, ind+1, k, init)
    # закр. скобку можно положить всегда, если cnt > 0
    if cnt > 0:
        init[ind] = ')'
        f(cnt-1, ind+1, k, init)
    # выходим из цикла и печатаем
    if ind == k:
        if cnt == 0:
            print (''.join(init))

f(cnt, ind, k, init)