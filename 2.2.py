class Node:
    def __init__(self, val = None):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, list_of_nodes = [Node()]):
        self.head = list_of_nodes[0]

        count = 1
        if len(list_of_nodes) > 1:
            while count < len(list_of_nodes):
                self.add_node(list_of_nodes[count])
                count += 1


    def add_node(self, node):
        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = node
        

    def find_kth_to_last(self, k):
        if k < 1:
            raise Exception

        p1 = self.head
        p2 = self.head

        index = 0
        while index < k:
            p1 = p1.next
            index += 1

        while p1 != None:
            p1 = p1.next
            p2 = p2.next

        return p2


if __name__ == "__main__":
    list_of_nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]
    x_list = LinkedList(list_of_nodes)

    print(x_list.find_kth_to_last(4).value)
    
