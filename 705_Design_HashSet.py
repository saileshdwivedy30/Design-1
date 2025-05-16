# This approach uses an array of fixed size (based on the problem constraints) to represent the HashSet.
# The add method marks an index corresponding to the key as True in the array, the remove method sets the index to False.
# The contains method checks if the index corresponding to the key is True (key exists) or False (key does not exist).
# TC: O(1) for all operations
# SC: O(10^6) for the array bucket which stores the True/False values for each possible key.
# Did this code successfully run on Leetcode : yes
class MyHashSet:

    def __init__(self):
        self.bucket = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.bucket[key] = True

    def remove(self, key: int) -> None:
        self.bucket[key] = False

    def contains(self, key: int) -> bool:
        return self.bucket[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)