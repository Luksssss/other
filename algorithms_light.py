# очередь
from collections import deque 

# Рекурсия. Факториал
def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)
		
# print(fact (5))


# Рекурсия. Сумма массива
def sum_mas(mas):
    # вариант 1
    # if mas == []:
    #     return 0
    # else:
    #     return mas[0] + sum_mas(mas[1:])
    
    # вариант 2
    if len(mas) == 0:
        return 0
    return mas.pop() + sum_mas(mas)
		
# print(sum_mas([1,2,3,4,5]))


# Рекурсия. Количество элементов массива
def cnt_mas(mas):
	if mas == []:
		return 0
	return 1 + cnt_mas(mas[1:])
		
print(cnt_mas([1,2,3,4,5]))


# Рекурсия. Максимум в массиве
# при условии что массив более чем из 1 элемента.
def max_mas(mas):
	if len(mas) == 2:
		return mas[0] if mas[0] > mas[1] else mas[1]
	sub_max = max_mas(mas[1:])
	return mas[0] if mas[0] > sub_max else sub_max
		
# print(max_mas([1,2,3,4,5]))


def test_graph():
    '''
    ПОИСК В ШИРИНУ.
    Простой пример поиска по графу (самый короткий путь).
    Найдём кто из соседей продавец О.о
    Время выполнения: O(V+E); V-количество вершин, E - рёбра
    '''

    seller = 'thom'

    graph = {}
    graph['you'] = ['alice','bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = graph['peggy'] = graph['thom'] = graph['jonny'] =  []

    # создаём стек поиска и добавляем первый уровень графа
    search_deq = deque()
    search_deq.extend(graph['you'])

    # чтобы не проверять людей дважды и не зацикливаться
    human_check = []

    # проходим по первой очереди друзей, потом друзья друзей и т.д.
    while search_deq:
        human = search_deq.popleft()
        if human not in human_check:
            if human == seller:
                print ('%s seller!' % human)
                return
            else:
                print ('%s not seller!' % human)
                # добавляем его друзей в конец очереди
                search_deq.extend(graph[human])
                human_check.append(human)

            
def graph_deykstri(graph, costs, parents):
    '''
    Пример работы с взвешанным графом (однонаправленным)
    Возвращает путь по графу с минимальной стоимостью
    Алгоритм Дейкстры не работает с отрицательными весами(!)
    Для отрицательных весов - алгоритм Беллмана-Форда
    '''
    # отработанные узлы
    processed = []

    node_key = get_min_val_node(costs, processed)

    while node_key is not None:
        val = costs[node_key]
        neigboards = graph[node_key].keys()
        for n in neigboards:
            new_costs = val + graph[node_key][n]
            if new_costs < costs[n]:
                costs[n] = new_costs
                parents[n] = node_key
        processed.append(node_key)

        node_key = get_min_val_node(costs, processed)

    # print(costs['end'])
    # print([parents])


def get_min_val_node(costs, processed):
    '''
    Возвращает узел (необработанный) с минимальной стоимостью
    '''
    cost_node_k = None
    cost_node_v = infinity

    for k, val in costs.items():
        if val < cost_node_v and k not in processed:
            cost_node_k = k
            cost_node_v = val
    
    return cost_node_k

# ВХОДНЫЕ ДАННЫЕ
# Собственно граф
graph = {}
graph['beg'] = {} 
graph['a'] = {} 
graph['b'] = {}
graph['c'] = {}
graph['d'] = {}
graph['end'] = {}
graph['beg']['a'] = 5
graph['beg']['c'] = 2
graph['a']['d'] = 2
graph['a']['b'] = 4
graph['b']['end'] = 3
graph['b']['d'] = 6
graph['c']['d'] = 7
graph['c']['a'] = 8
graph['d']['end'] = 1

# стоимости узлов графа (т.е. за какую мин стомость можно дойти до него)
# Изначально указывается стоимость только начальных узлов (стоимость остальных не знаем) 
infinity = float("inf") # бесконечность
costs = {}
costs['a'] = 5
costs['c'] = 2
costs['b'] = infinity
costs['d'] = infinity
costs['end'] = infinity

# Родители узлов
parents = {}
parents['a'] = "beg"
parents['c'] = "beg"
parents['end'] = None

