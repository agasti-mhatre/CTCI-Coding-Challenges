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
        else:
            self.head = self.tail = list_of_nodes[0]

            if len(list_of_nodes) > 1:
                index = 1
                while index < len(list_of_nodes):
                    self.add_node(list_of_nodes[index])
                    index += 1


    def add_node(self, node):
        if (self.head == None) and (self.tail == None):
            self.head = self.tail = node
        else:
            self.tail.next = node
            temp = self.tail
            self.tail = self.tail.next
            self.tail.prev = temp
            
    def print(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" ")
            temp = temp.next

        print()


class Stack(DoublyLinkedList):
    def push(self, node):
        self.add_node(node)


    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from empty stack!")
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

            return temp


    def peek(self):
        return self.tail


    def isEmpty(self):
        if (self.head == None) and (self.tail == None):
            return True
        else:
            return False


def sorted_stack(x_stack): 
    if x_stack.isEmpty() or (x_stack.head == x_stack.tail):
        return x_stack
    else:
        s_stack = Stack()
        while x_stack.head != None:
            greatest = checker = x_stack.head
            while checker != None:
                if checker.val > greatest.val:
                    greatest = checker

                checker = checker.next

            s_stack.push(Node(greatest.val))
            
            before = greatest.prev
            after = greatest.next
            
            if (before == None) and (after == None):
                break
            elif (before == None) and (after != None):
                x_stack.head = x_stack.head.next
                after.prev = greatest.prev
            elif (before != None) and (after == None):
                before.next = greatest.next
            elif (before != None) and (after != None):
                before.next = greatest.next
                after.prev = greatest.prev
            
            greatest.prev = None
            greatest.next = None

        return s_stack


if __name__ == "__main__":
    x_stack = Stack([Node(4), Node(3), Node(5), Node(6), Node(1)])
    x_stack.print()
    s_stack = sorted_stack(x_stack)
    s_stack.print()
