class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    
class LinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            return None
        else:
            self.head = list_of_nodes[0]

        if len(list_of_nodes) > 1:
            index = 1
            while index < len(list_of_nodes):
                self.add_node(list_of_nodes[index])
                index += 1

    
    def add_node(self, node):
        if self.head == None:
            self.head = node
            return None

        temp = self.head
        
        while temp.next != None:
            temp = temp.next

        temp.next = node

    def print_nodes(self):
        temp = self.head

        while temp.next != None:
            print(temp.val, end=' ')
            temp = temp.next

        print(temp.val)


def partition_list(x_LL, pivot = 0):
    temp = x_LL.head
    less = LinkedList()
    greater_or_equal = LinkedList()
    merged_list = LinkedList()

    while temp.next != None:
        if temp.val < pivot:
            less.add_node(Node(temp.val))
        else:
            greater_or_equal.add_node(Node(temp.val))

        temp = temp.next


    if temp.val < pivot:
        less.add_node(Node(temp.val))
    else:
        greater_or_equal.add_node(Node(temp.val))


    temp = less.head
    while temp != None:
        if temp.next == None:
            print(temp.val, end='')
            merged_list.add_node(Node(temp.val))
            break
        print(temp.val, end=' -> ')
        merged_list.add_node(Node(temp.val))
        temp = temp.next    
        
    print('\t->\t', end='')

    temp = greater_or_equal.head
    while temp != None:
        if temp.next == None:
            print(temp.val, end='')
            merged_list.add_node(Node(temp.val))
            break
        print(temp.val, end=' -> ')
        merged_list.add_node(Node(temp.val))
        temp = temp.next    

    return merged_list
    
if __name__ == "__main__":
    list_of_nodes = [Node(3), Node(5), Node(8), Node(5), Node(10), Node(2), Node(1)]
    x_LL = LinkedList(list_of_nodes)

    merged_list = partition_list(x_LL, 5)

    merged_list.print_nodes()