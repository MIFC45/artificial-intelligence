"""
This module defines the stack data structure.

"""

class Stack(list):

    def push(self, item):
        self.append(item)

    def pop(self):
        return list.pop(self)

    def is_empty(self):
        return len(self) == 0

# Example usage
if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(7)
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())
