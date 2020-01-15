from utils import *

class TEST:
    def __init__(self, arr, inputs):
        self.arr = arr
        self.inputs = inputs
        self.input_indx = 0
        self.outputs = []
        self.halt = False
        self.falsy = False

    def get_input(self):
        ret = self.inputs[self.input_indx]
        self.input_indx += 1
        return ret

    def sum(self, a, b):
        return self.arr[a]+self.arr[b]

    def multiply(self, a, b):
        return self.arr[a] * self.arr[b]
    
    def less_than(self, a, b):
        return self.arr[a] < self.arr[b]

    def equals(self, a, b):
        return self.arr[a] == self.arr[b]

    def is_zero(self, a):
        return self.arr[a] == 0

    def get_new_pos(self, curr, a):
        return self.arr[a]-curr

    def get_values(self, pm, indx, n):
        values = []
        for i in range(n):
            if pm[i]:
                values.append(indx+i+1)
            else:
                values.append(self.arr[indx+i+1])
        return values
    
    def run_instruction(self, indx):
        op_code = self.arr[indx]
        parameter_mode = [op_code//100&1, op_code//1000&1, op_code//10000&1]
        op_code %= 100
        ret = 0
        values = []

        if op_code in [1, 2, 7, 8]:
            values = self.get_values(parameter_mode, indx, 3)

            if op_code == 1:
                self.arr[values[2]] = self.sum(values[0], values[1])
            elif op_code == 2:
                self.arr[values[2]] = self.multiply(values[0], values[1])
            elif op_code == 7:
                self.arr[values[2]] = self.less_than(values[0], values[1])
            elif op_code == 8:
                self.arr[values[2]] = self.equals(values[0], values[1])
            return 4
        
        if op_code in [5, 6]:
            values = self.get_values(parameter_mode, indx, 2)
            
            if op_code == 5:
                if not self.is_zero(values[0]):
                    return self.get_new_pos(indx, values[1])
            elif op_code==6:
                if self.is_zero(values[0]):
                    return self.get_new_pos(indx, values[1])
            return 3

        elif op_code in [3, 4]:
            values = self.get_values(parameter_mode, indx, 1)

            if op_code == 3:
                self.arr[values[0]] = self.get_input()
                
            elif op_code == 4:
                self.outputs.append(self.arr[values[0]])
            return 2
        elif op_code == 99:
            self.halt = True
            return 0
        else:
            self.falsy = True
            return 1
