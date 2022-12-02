class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    # Time: O(n)
    def push(self, x: int) -> None:
        # Copy items to Q2
        while len(self.q1) != 0:
            self.q2.append(self.q1.pop(0))
        # Add the new element to Q1
        self.q1.append(x)
        # Transfer the elements back to Q1
        while len(self.q2) != 0:
            self.q1.append(self.q2.pop(0))

    # Time: O(1)
    def pop(self) -> int:
        return self.q1.pop(0)

    # Time: O(1)
    def top(self) -> int:
        return self.q1[0]

    # Time: O(1)
    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()