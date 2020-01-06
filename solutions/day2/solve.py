import sys
sys.path.append('../')

from utils import *

def solve_1(arr, n=12, v=2):
    arr[1] = n
    arr[2] = v
    for i in range(0, len(arr), 4):
        op_code = arr[i]
        if op_code == 99:
            return arr[0]
        if i+3>=len(arr):
            print("Halting for misconfiguration")
            return arr[0]
        op1 = arr[arr[i+1]]
        op2 = arr[arr[i+2]]
        if op_code == 1:
            arr[arr[i+3]] = op1 + op2
        elif op_code == 2:
            arr[arr[i+3]] = op1 * op2

def solve_2(arr):
    for n in range(100):
        for v in range(100):
            arr2 = arr[:]
            res = solve_1(arr2, n, v)
            if res == 19690720:
                return 100*n+v

if __name__=="__main__":
    f = readinput('a_1.txt')
    f = [int(x) for x in f.split(',')]
    sol1 = solve_1(f)
    print("Result of A:", sol1)

    f = readinput('b_1.txt')
    f = [int(x) for x in f.split(',')]
    sol2 = solve_2(f)
    print("Result of B:", sol2)
