def readinput(path):
    f = open(path, 'r')
    ret = f.read()
    f.close()
    return ret

def solve_1(arr):
    res = 0
    for l in arr:
        res += l//3-2
    return res

def solve_2(arr):
    res = 0
    for l in arr:
        x = l
        while x > 0:
            x = x//3-2
            res += max(x, 0)
    return res

if __name__=="__main__":
    f = readinput('a_1.txt')
    f = [int(x) for x in f.split()]
    sol1 = solve_1(f)
    print("Result of A:", sol1)

    f = readinput('b_1.txt')
    f = [int(x) for x in f.split()]
    sol2 = solve_2(f)
    print("Result of B:", sol2)
