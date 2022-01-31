import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return  # = return None
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        print(self.table[index])
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        target = self.table[index]
        prev = None
        while target:
            if target.key == key:
                # 삭제할 노드가 첫번째인 경우: table[index]->'target node'->node->...
                if target == self.table[index]:
                    if target.next == None:
                        self.table[index].next = ListNode()
                        return
                    else:
                        self.table[index] = target.next
                        target.next = None
                        return
                # 삭제할 노드가 중간인 경우
                else:
                    prev.next = target.next
                    target.next = None
                    return

                prev, target = target, target.next

        return None
    # 성공. remove()는 책에 나온 코드가 더 깔끔함.

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return  # = return None
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        print(self.table[index])
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[indxe] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
        prev, p = p, p.next
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
param_2 = obj.get(3)
obj.put(2,1)
param_3 = obj.get(2)
obj.remove(2)
param_4 = obj(2)

print(f'{},{},{},{},{},{},{},{}')