class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop(-1)
    
    def top(self):
        return self.__data[-1]
    
    def empty(self):
        return not len(self.__data) > 0