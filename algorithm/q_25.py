class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen   # maxlen의 나머지 -> p2 < maxlen
            return True
        else:
            return False   # queue full
    def deQueue(self) -> bool:
        if self.q[self.p1] is not None:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        else:
            return False
    def Front(self) -> int:
        if self.q[self.p1] is not None:
            return self.q[self.p1]
        else:
            return -1
    def Rear(self) -> int:
        if self.q[self.p2-1] is None:
            return -1
        else:
            return self.q[self.p2-1]
    def isEmpty(self) -> bool:
        if self.p1 == self.p2:
            return self.q[self.p1] is None
        else:
            return False
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

