class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0]*capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.size < self.capacity:
            self.arr[self.size] = n
            self.size += 1
        else:
            self.resize()
            self.arr[self.size] = n
            self.size += 1
        return None

    def popback(self) -> int:
        self.size -= 1
        v = self.arr[self.size]
        return v

    def resize(self) -> None:
        self.arr = self.arr + [0]*self.capacity
        self.capacity *= 2
        return None

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
