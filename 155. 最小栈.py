class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = None

    def push(self, x: int) -> None:
        if self.stack_min is not None:
            if self.stack_min > x:
                self.stack_min = x
        else:
            self.stack_min = x

        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            top = self.stack[-1]
            self.stack = self.stack[:-1]
            if self.stack_min == top:
                if self.stack:
                    self.stack_min = self.sortList()
                else:
                    self.stack_min = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min

    def sortList(self):

        tmp = self.stack[0]
        for i in range(len(self.stack) - 1):
            if tmp > self.stack[i + 1]:
                tmp = self.stack[i + 1]
        return tmp


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()