class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.tail = list_of_nodes[0]
            self.length = 1
            
            index = 1
            while index < len(list_of_nodes):
                self.add_node(list_of_nodes[index])
                index += 1

            
    def add_node(self, node):
        if self.head == self.tail == None:
            self.head = self.tail = node
            self.length += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.length += 1


    def __len__(self):
        return self.length


class Stack(DoublyLinkedList):
    def push(self, val):
        self.add_node(Node(val))


    def pop(self):
        if self.head == self.tail == None:
            raise Exception("Can't pop from empty Stack!")
        elif self.head == self.tail:
            val = self.tail.val
            self.head = self.tail = None
            
            self.length -= 1
            return val
        else:
            val = self.tail.val
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = self.tail.next = None
            
            self.length -= 1
            return val

class SetNode:
    def __init__(self, stack):
        self.prev = None
        self.next = None
        self.stack = stack

class SetOfStacks:
    def __init__(self, list_of_values = [], threshold = 2):
        self.threshold = threshold
        self.s_head = None
        self.s_tail = None
        index = 0
        while index < len(list_of_values):
            self.push(list_of_values[index])
            index += 1

    
    def push(self, val):
        if self.s_head == self.s_tail == None:
            self.s_head = self.s_tail = SetNode(Stack([Node(val)]))
        elif len(self.s_tail.stack) < self.threshold:
            self.s_tail.stack.push(val)
        else:
            self.s_tail.next = SetNode(Stack([Node(val)]))
            self.s_tail.next.prev = self.s_tail
            self.s_tail = self.s_tail.next


    def pop(self):
        if self.s_head == self.s_tail == None:
            raise Exception("There are no stacks in the set!")
        elif (self.s_tail == self.s_head) and (len(self.s_tail.stack) == 1):
            val = self.s_tail.stack.pop()
            self.s_head = self.s_tail = None
            return val
        else:
            if len(self.s_tail.stack) == 0:
                temp = self.s_tail
                self.s_tail = self.s_tail.prev
                self.s_tail.next = temp.prev = None
                return self.pop()
            else:
                return self.s_tail.stack.pop()
                

if __name__ == "__main__":
    x_set_of_stacks = SetOfStacks([7,4,3,1,5])
    print(len(x_set_of_stacks.s_head.stack))
    print()
    print(x_set_of_stacks.pop())
    print(x_set_of_stacks.pop())
    print(x_set_of_stacks.pop())
    print(x_set_of_stacks.pop())
    print(x_set_of_stacks.pop())
