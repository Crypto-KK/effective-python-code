from collections import deque, OrderedDict, defaultdict
from heapq import heappop, heappush, nsmallest
'''双端队列'''
print('双端队列')
fifo = deque()
fifo.append(1)
fifo.popleft()
print(fifo)
print('=' * 50)


'''
有序字典
'''
print('有序字典')
a = OrderedDict()
b = OrderedDict()
a['foo'] = 1
a['bar'] = 2
b['foo'] = 'red'
b['bar'] = 'blue'
for value1, value2 in zip(a.values(), b.values()):
    print(value1, value2)
print('=' * 50)

'''
默认值的字典
'''
print('默认值的字典')
d = {}
d.setdefault('key', 0)
d['key'] += 1
print(d)

stats = defaultdict(int)
stats['my_counter'] += 1
print(stats)

print('=' * 50)


'''
堆队列（优先级队列）
'''
print('堆队列')
a =[]
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
#print(heappop(a), heappop(a), heappop(a),heappop(a))
print(a)
print('=' * 50)


