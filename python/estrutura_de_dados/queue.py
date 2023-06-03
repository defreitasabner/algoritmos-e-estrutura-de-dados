class Queue:
    def __init__(self):
        self.__data = []

    def insert(self, item):
        self.__data.append(item)

    def remove(self):
        self.__data.pop(0)

    def empty(self):
        return len(self.__data) == 0
 