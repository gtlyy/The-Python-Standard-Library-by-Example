#!/usr/bin/env python3
"""Using groupby()
"""

#end_pymotw_header
from itertools import *
from operator import itemgetter

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.items(), key=itemgetter(1))

# print(type(di))
# <class 'list'>
# print(di)
# [('a', 1), ('c', 1), ('e', 1), ('b', 2), ('d', 2), ('f', 2), ('g', 3)]

for k, g in groupby(di, key=itemgetter(1)):
    # print(k, *g)
    # 1 ('a', 1)('c', 1)('e', 1)
    # 2 ('b', 2)('d', 2)('f', 2)
    # 3 ('g', 3)

    # print(k, list(g))
    # 1 [('a', 1), ('c', 1), ('e', 1)]
    # 2 [('b', 2), ('d', 2), ('f', 2)]
    # 3 [('g', 3)]

    # print(k, list(map(itemgetter(0), g)))
    # 1 ['a', 'c', 'e']
    # 2 ['b', 'd', 'f']
    # 3 ['g']

    print(k, *map(itemgetter(0), g))
    # 1 a c e
    # 2 b d f
    # 3 g
