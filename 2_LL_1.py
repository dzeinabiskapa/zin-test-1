class Node:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def is_empty(self): # returns true if stack is empty else false
        return self.height == 0

    def push(self, value, position):
        new_node = Node(value, position)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp

def balancets(s):
    stack = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}

    pos = 1
    for char in s:
        if char in brackets_map.values():  # If char is an opening bracket
            stack.push(char, pos)
        elif char in brackets_map.keys():  # If char is a closing bracket
            if stack.is_empty() or brackets_map[char] != stack.pop().value:
                return pos
        pos += 1  # Increment position for next character
    
    if not stack.is_empty():  # If there are unmatched opening brackets left on the stack
        return stack.pop().position
    
    return "Success"

s = input("Ievadiet rindu: ")
print(balancets(s))
