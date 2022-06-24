#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class MyCircularDeque:
    class Node:
        def __init__(self, value = 0, left = None, right = None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = self.rear = self.Node(value)
            else:
                self.front.left = self.front = self.Node(value, None, self.front)
            self.size += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = self.rear = self.Node(value)
            else:
                self.rear.right = self.rear = self.Node(value, self.rear, None)
            self.size += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            front = self.front.right
            del self.front
            self.front = front
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            rear = self.rear.left
            del self.rear
            self.rear = rear
            self.size -= 1
            return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.front.value

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.rear.value

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

