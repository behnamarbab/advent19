import sys
sys.path.append('../')

from collections import defaultdict

from utils import *

def hashable(l):
    return ','.join([str(c) for c in l])

def solve_1(arr):
    d = defaultdict(lambda: 0)
    loc1 = [0, 0]
    dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    for a in arr[0]:
        while a[1]>0:
            loc1[0] += dirs[a[0]][0]
            loc1[1] += dirs[a[0]][1]
            d[hashable(loc1)] = 1
            a[1] -= 1
    locs = []
    loc1 = [0, 0]
    for a in arr[1]:
        while a[1]>0:
            loc1[0] += dirs[a[0]][0]
            loc1[1] += dirs[a[0]][1]
            if d[hashable(loc1)] == 1:
                locs.append(abs(loc1[0])+abs(loc1[1]))
            d[hashable(loc1)] = 2
            a[1] -= 1
    return min(locs)

def solve_2(arr):
    d = defaultdict(lambda: 0)
    loc1 = [0, 0]
    dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    cnt = 1
    for a in arr[0]:
        while a[1]>0:
            loc1[0] += dirs[a[0]][0]
            loc1[1] += dirs[a[0]][1]
            if d[hashable(loc1)] == 0:
                d[hashable(loc1)] = cnt
            cnt += 1
            a[1] -= 1
    d2 = defaultdict(lambda: 0)
    loc1 = [0, 0]
    cnt = 1
    mn = 102345678
    for a in arr[1]:
        while a[1]>0:
            loc1[0] += dirs[a[0]][0]
            loc1[1] += dirs[a[0]][1]
            if d[hashable(loc1)] > 0:
                mn = min(d[hashable(loc1)]+cnt, mn)
            if d2[hashable(loc1)] == 0:
                d2[hashable(loc1)] = cnt
            cnt += 1
            a[1] -= 1
    return mn

if __name__=="__main__":
    f = readinput('a_1.txt')
    f = [[[x[0], int(x[1:])] for x in y.split(',')] for y in f.split()]
    sol1 = solve_1(f)
    print("Result of A:", sol1)

    f = readinput('b_1.txt')
    f = [[[x[0], int(x[1:])] for x in y.split(',')] for y in f.split()]
    sol2 = solve_2(f)
    print("Result of B:", sol2)
