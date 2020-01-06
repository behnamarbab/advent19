def readinput(path):
    f = open(path, 'r')
    ret = f.read()
    f.close()
    return ret