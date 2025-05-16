# This approach uses two stacks: one for the regular stack and one for tracking the minimum values.
# The push operation adds elements to both stacks, and the pop operation removes from both.
# The getMin operation returns the top of the minimum stack which always contains the current minimum element.
# TC: O(1) for all operations
# SC: O(n) no of elements in stack
# Did this code successfully run on Leetcode : yes
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped_value = self.stack.pop()
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()