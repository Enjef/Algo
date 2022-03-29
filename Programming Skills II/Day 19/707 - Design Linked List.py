class MyLinkedList:
    def __init__(self):  # 99.19% 87.00%
        self.list = []

    def get(self, index: int) -> int:
        if not -1 < index < len(self.list):
            return -1
        return self.list[index]

    def addAtHead(self, val: int) -> None:
        self.list.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.list.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if not(-1 < index <= len(self.list)):
            return -1
        if index == len(self.list):
            self.addAtTail(val)
            return
        self.list.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if not(-1 < index < len(self.list)):
            return
        self.list.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


class MyLinkedList_best_speed:
    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
        if len(self.arr)>index:
            return self.arr[index]
        return -1

    def addAtHead(self, val: int) -> None:
        if len(self.arr)!=0:
            self.arr.insert(0,val)
        else:
            self.arr.append(val)

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.arr)>=index:
            self.arr.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if len(self.arr)>index:
            self.arr.pop(index)
