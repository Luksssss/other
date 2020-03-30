# Анаграммы
with open('/home/lukas/input2.txt') as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

print s1, s2
if len(s1) != len(s2):
    print 0
else:
    s11 = sorted(s1)
    s22 = sorted(s2)

    test = [el for ind, el in enumerate(s11) if el == s22[ind]]

    if len(s2) == len(test):
        print 1
    else:
        print 0