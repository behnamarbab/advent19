import sys
sys.path.append('../')

from collections import defaultdict

from utils import *


def solve_1(f):
    d = defaultdict(lambda: [])
    costs = defaultdict(lambda: 0)
    
    for item in f:
        d[item[0]].append(item[1])

    queue = ["COM"]
    res = 0

    while len(queue):
        front = queue.pop()
        for c in d[front]:
            if costs[c] > 0:
                continue
            costs[c] = costs[front]+1
            queue.append(c)

    return sum([costs[x] for x in costs])

def solve_2(f):
    d = defaultdict(lambda: [])
    costs = defaultdict(lambda: 0)
    
    for item in f:
        d[item[0]].append(item[1])
        d[item[1]].append(item[0])

    queue = ["YOU"]
    res = 0

    while len(queue):
        front = queue.pop()
        for c in d[front]:
            if costs[c] > 0 and c!="YOU":
                continue
            costs[c] = costs[front]+1
            queue.append(c)

    return costs['SAN']-2


if __name__=="__main__":
    f = readinput('a_1.txt')
    f = [x.split(')') for x in f.split('\n') if len(x)==7]
    sol1 = solve_1(f)
    print("Result of A:", sol1)

    f = readinput('b_1.txt')
    f = [x.split(')') for x in f.split('\n') if len(x)==7]
    sol2 = solve_2(f)
    print("Result of A:", sol2)
