import sys
sys.path.append('../')

from utils import *
from TEST import TEST

def solve_1(arr, inputs):
    test = TEST(arr, inputs)
    indx = 0
    while indx < len(test.arr):
        indx += test.run_instruction(indx)
        if test.halt:
            break
    return test.outputs[-1]

if __name__=="__main__":
    f = readinput('a_1.txt')
    f = [int(x) for x in f.split(',')]
    sol1 = solve_1(f, [1])
    print("Result of A:", sol1)

    f = readinput('b_1.txt')
    f = [int(x) for x in f.split(',')]
    sol2 = solve_1(f, [5])
    print("Result of B:", sol2)
