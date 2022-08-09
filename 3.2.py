class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None
        self.current_min = val

class DoublyLinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            self.tail = None
        else:
            self.head = list_of_nodes[0]
            self.tail = self.head
            
            if len(list_of_nodes) > 1:
                index = 1
                while index < len(list_of_nodes):
                    self.push(list_of_nodes[index])
                    index += 1
        

    def push(self, node):
        if (self.head == None) and (self.tail == None):
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            temp = self.tail
            self.tail = self.tail.next
            self.tail.prev = temp

            if self.tail.prev.current_min < self.tail.current_min:
                self.tail.current_min = self.tail.prev.current_min


    def pop(self):
        if self.tail == None:
            raise Exception("List is empty. Nothing to pop.")
        elif self.head == self.tail:
            node = self.head

            self.head.next = None
            self.head.prev = None
            self.tail.next = None
            self.tail.prev = None
            self.head = None
            self.tail = None

            return node
        else:
            node = self.tail

            temp = self.tail.prev
            temp.next = None
            self.tail.prev = None
            self.tail = temp


            return node


    def min(self):
        return self.tail.current_min



if __name__ == "__main__":
    #x_LL = DoublyLinkedList([Node(3), Node(1), Node(2), Node(0), Node(4)])
    x_LL = DoublyLinkedList([Node(3)])
    x_LL.push(Node(1))
    print(x_LL.min())
    x_LL.push(Node(2))
    print(x_LL.min())
    x_LL.push(Node(0))
    print(x_LL.min())
    x_LL.push(Node(4))
    print(x_LL.min())
    print(x_LL.pop().val)
    print(x_LL.pop().val)
    print(x_LL.pop().val)
    print(x_LL.pop().val)
    print(x_LL.pop().val)
    x_LL.push(Node(5))
    print(x_LL.min())
