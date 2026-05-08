class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # dummy node
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: 
            return -1
        cur = self.head.next # first real node
        for _ in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        temp = ListNode(val)
        temp.next = self.head.next
        self.head.next = temp
        if self.length == 0:
            self.tail = temp
        self.length += 1

    def insertTail(self, val: int) -> None:
        temp = ListNode(val)
        self.tail.next = temp
        self.tail = temp
        self.length += 1

    # REMOVE LOGIC CLEAR NHI H, ISKI PRACTICE KARNE KI JARURAT H
    # KHUDSE JO LIKHA CODE USME ERROR AA RHE THE BAAR BAR
    # TO YE DEKH KAR KARA H
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        prev = self.head # dummy
        for _ in range(index):
            prev = prev.next
        to_remove = prev.next
        prev.next = to_remove.next
        if to_remove is self.tail:
            self.tail = prev if prev is not self.head else self.head
            if self.length - 1 == 0:
                self.tail = self.head
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        arr = []
        cur = self.head.next
        for _ in range(self.length):
            arr.append(cur.val)
            cur = cur.next
        return arr