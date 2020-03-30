
with open('input.txt') as ff:
	k = int(ff.readline().strip()) * 2

init = [None for _ in range(k)]
cnt = 0
ind = 0

def f(cnt, ind, k, init):
    if (cnt <= k-ind-2):
        init[ind] = '('
        f(cnt+1, ind+1, k, init)
    if cnt > 0:
        init[ind] = ')'
        f(cnt-1, ind+1, k, init)
    if ind == k:
        if cnt == 0:
            print (''.join(init))

f(cnt, ind, k, init)