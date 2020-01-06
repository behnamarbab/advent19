import sys
sys.path.append('../')

from utils import *

def is_double(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return True
    return False

def is_improved_double(s):
    for c in [chr(x) for x in range(ord('0'), ord('9')+1)]:
        if s.count(c)==2:
            return True
    return False

def is_increasing(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

def solve_1(l=128392, r=643281):
    res = 0
    for i in range(l, r+1):
        if is_double(str(i)) and is_increasing(str(i)):
            res += 1
    return res

def solve_2(l=128392, r=643281):
    res = 0
    for i in range(l, r+1):
        if is_improved_double(str(i)) and is_increasing(str(i)) and is_double(str(i)):
            res += 1
    return res

if __name__=="__main__":
    sol1 = solve_1()
    print("Result of A:", sol1)

    sol2 = solve_2()
    print("Result of B:", sol2)
