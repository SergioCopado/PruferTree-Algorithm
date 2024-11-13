class Heap:
    def __init__(self):
        self.__array = []
        self.__size = 0

    def __str__(self):
        return str(self.__array)

    def __father(self, n):
        if n % 2:
            i = n // 2
        else:
            i = n // 2 - 1
        if i < 0:
            i = 0
        return i

    def __heapify(self, n):
        minor = n
        left = 2 * n + 1      # left  child
        right = 2 * n + 2     # right child
        if left < self.__size and self.__array[left] < self.__array[minor]:
            minor = left
        if right < self.__size and self.__array[right] < self.__array[minor]:
            minor = right
        if minor != n:
            self.__array[n], self.__array[minor] = self.__array[minor], self.__array[n]
            self.__heapify(minor)

    def is_empty(self):
        return self.__array == []

    def build_heap(self, l):
        assert self.is_empty(), 'The heap is not empty'
        self.__array = l
        self.__size = len(l)
        initial_node = self.__size // 2 - 1
        for i in range(initial_node, -1, -1):
            self.__heapify(i)

    def insert(self, ele):
        self.__array.append(ele)
        self.__size += 1
        n = self.__size - 1
        i = self.__father(n)
        while i >= 0 and self.__array[n] < self.__array[i]:
            self.__array[n], self.__array[i] = self.__array[i], self.__array[n]
            n = i
            i = self.__father(i)

    def delete(self):
        minimum = self.__array[0]
        self.__size -= 1
        self.__array[0] = self.__array[self.__size]
        self.__array.pop()
        self.__heapify(0)
        return minimum

    def peek(self):
        return self.__array[0]