from itertools import islice
# with open('input.txt') as f:
with open('/home/lukas/input2.txt') as f:
    n = f.readline().strip()
    un_data = set()
    while True:
        sl = islice(f, 3)
        data = set(int(s.strip()) for s in sl if s.strip().isdigit())
        if not data:
            break
        else:
            un_data = un_data.union(data)
res = sorted(un_data)
print "\n".join(map(str, res))