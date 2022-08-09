class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, list_of_nodes = [Node(None)]):
        self.head = list_of_nodes[0]
        self.length = 1
        if len(list_of_nodes) > 1:
            index = 1
            while index < len(list_of_nodes):
                self.add_node(list_of_nodes[index])
                index += 1


    def add_node(self, node):
        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = node

        self.length += 1

        return None


    def print_nodes(self):
        if self.length > 1:
            temp = self.head
            while temp.next != None:
                print(temp.val, end='')
                temp = temp.next

            print(temp.val)            
        else:
            print(self.head.val, end='')

        print()
        
        return None


    def middle_node(self):
        index_middle = self.length // 2

        middle_node = self.head
        count = 1
        while (count < index_middle) and (middle_node.next != None):
            middle_node = middle_node.next
            count += 1

        return middle_node

    def remove_node_call(self):
        remove_node(self.middle_node())
        self.length -= 1

def remove_node(node):
    if node.next == None:
        raise Exception("Cannot delete middle node")

    prev = node
    next = node.next

    while next.next != None:
        prev.val = next.val
        prev = next
        next = next.next

    prev.val = next.val
    prev.next = None


if __name__ == "__main__":
    list_of_nodes = [Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f')]
    x_list = LinkedList(list_of_nodes)

    x_list.print_nodes()
    x_list.remove_node_call()
    x_list.print_nodes()
