res = "0"
hash = {}

with open("input.txt") as f:
    target = int(f.readline().strip())

    while True:
        raw_data = f.read(10240)
        if not raw_data:
            break
        else:
            if raw_data[-1] != ' ':
                while True:
                    symbol = f.read(1)
                    if symbol == '':
                        break
                    raw_data = raw_data + symbol
                    if raw_data[-1] == ' ' :
                        break
            for ind, el in enumerate(raw_data.strip().split()):
                el2 = target - int(el)
                
                if el2 in hash:
                    res = "1"
                    break
                else:
                    hash[int(el)] = ind
        if res == "1":
            break

with open("output.txt", "w") as ff:
    ff.writelines(res) 