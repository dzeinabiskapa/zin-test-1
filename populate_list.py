class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def sum(self):
        sum = 0
        n = self.head
        sum += n.value
        n = n.next
        n = self.head
        sum += n.next.value
        sum += n.next.value
        return sum

my_linked_list = LinkedList(1)
my_linked_list.append(7)
my_linked_list.append(6)
my_linked_list.append(9)

total_sum = my_linked_list.sum()
print("Total sum:", total_sum)