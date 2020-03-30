# Алгоритм с загнивающими апельсинами
# https://leetcode.com/problems/rotting-oranges/
def orangesRotting(grid) -> int:
    mas_rotten = []
    mas_fresh = {}
    check_cell = {}
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == 1:
                mas_fresh[(i, j)] = None
            elif el == 2:
                mas_rotten.append((i, j))
    
    days = 0
    while mas_fresh:
        
        flag = False
        for ind in range(len(mas_rotten)):
            el = mas_rotten[ind]
            line = el[0]
            j = el[1]

            # заносим элемент в словарь чтобы не проверять 
            # элементы по несколько раз
            check_cell[el] = None
            
            var1 = (line + 1, j)
            var2 = (line - 1, j)
            var3 = (line, j - 1)
            var4 = (line, j + 1)
            
            if var1 in mas_fresh:
                mas_fresh.pop(var1)
                if var1 not in check_cell:
                    mas_rotten.append(var1)
                    flag = True
            if var2 in mas_fresh:
                mas_fresh.pop(var2)
                if var2 not in check_cell:
                    mas_rotten.append(var2)
                    flag = True
            if var3 in mas_fresh:
                mas_fresh.pop(var3)
                if var3 not in check_cell:
                    mas_rotten.append(var3)
                    flag = True                    
            if var4 in mas_fresh:
                mas_fresh.pop(var4)
                if var4 not in check_cell:
                    mas_rotten.append(var4)
                    flag = True                    
                    
        if flag:
            days +=1
        else:
            return -1
    
    return days


# print('res5 = ', orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))    


def letterCombinations(digits: str):
    if not digits: return []
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = ['']
    for idx in range(len(digits)):
        result = [prev + l for prev in result for l in digit_map[digits[idx]]]
        print(result)
    return result

print('res6 = ', letterCombinations('23'))


# Возврат простых чисел (подобие алгоритма решето)
# Тут ошибка с перебором элементов (из-за индексов)
def simple_num(n):
    if n < 2:
        return []
    res = [2]
    tmp = [el for el in range(3, n+1)]

    while tmp:
        for el in tmp:
            if el % res[-1] == 0:
                tmp.remove(el)

        res.append(tmp.pop(0))

    return res


# за сколько шагов можно дойти до нуля при деление на 2
# если число нечётное, то -1
def numberOfSteps (num: int) -> int:
    cnt = 0
    while True:
        cnt += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num // 2
            cnt += 1
        if num == 1:
            return cnt + 1

# print('res = ', numberOfSteps(14))

# вернуть количество элементов меньше текущего
# output [4, 0, 1, 1, 3]
def smallerNumbersThanCurrent(nums):

    nums_sort = sorted(nums)
    res = [nums_sort.index(el) for el in nums]

    return res

# print('res2 = ', smallerNumbersThanCurrent([8,1,2,2,3]))


def rankTeams(votes) -> str:
    cnt_team = len(votes[0])
    rating = {}
    for el in votes:
        for ind, team in enumerate(el):
            rating[team][ind] = rating.setdefault(team, [0]*cnt_team)[ind] + 1
            # rating[team] = rating[team] + ind if team in rating else ind
    rating_sort = sorted(sorted(rating.items()), key = lambda el: el[1], reverse = True)
    
    res = ''
    
    for s in rating_sort:
        res += s[0]
        
    return res

# правильное решение (не моё)
def rankTeams2(votes) -> str:
    ranking = dict()
    for vote in votes: 
        for i, x in enumerate(vote): 
            ranking.setdefault(x, [0]*len(vote))[i] += 1
    return "".join(sorted(sorted(vote), key=ranking.get, reverse=True))

print('res3 = ', rankTeams(
["BCA","CAB","CBA","ABC","ACB","BAC"]))

from itertools import combinations_with_replacement
def combinationSum(scandidates, target: int):
    res = []
    min_el = min(scandidates)
    max_cnt = target // min_el
    for ind in range(1, max_cnt+1):
        tmp_res = [el for el in combinations_with_replacement(scandidates, ind) if sum(el) == target]
        print(tmp_res)
        res += tmp_res

    return res

# print('res4 = ', combinationSum([2,3,6,7], 7))


def duplicateZeros(arr) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            arr.insert(i+1, 0)
            arr.pop()
            i += 1
            print(arr, i)
        i += 1

# print('res5 = ', duplicateZeros([1,0,2,3,0,4,5,0]))