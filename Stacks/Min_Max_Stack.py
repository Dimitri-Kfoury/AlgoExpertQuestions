# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None

    def pop(self):
        self.min_max.pop()
        return self.stack.pop()

    def push(self, number):
        if len(self.min_max):
            min_max = [min(self.min_max[len(self.min_max) - 1][0], number),
                       max(number, self.min_max[len(self.min_max) - 1][1])]
        else:
            min_max = [number, number]
        self.min_max.append(min_max)
        return self.stack.append(number)

    def getMin(self):
        if len(self.min_max):
            return self.min_max[len(self.min_max) - 1][0]
        return None

    def getMax(self):
        if len(self.min_max):
            return self.min_max[len(self.min_max) - 1][1]
        return None


array = [0, 1, 2, 2, 3]

print(array[len(array) - 1])
