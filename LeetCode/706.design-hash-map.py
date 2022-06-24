#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
import collections

class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
        else:
            node = self.table[index]
            while node:
                if node.key == key:
                    node.value = value
                    return

                if node.next is None:
                    break # 삽입을 위해 미리 탈출한다.
                node = node.next
            node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev is None:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                del node
                return
            prev, node = node, node.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

