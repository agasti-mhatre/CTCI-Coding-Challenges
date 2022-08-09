class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
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
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next


            temp.next = node


    def print_nodes(self):
        temp = self.head

        while temp != None:
            print(temp.val)
            temp = temp.next


def intersecting_node(x_LL, y_LL):
    hash_map_nodes = dict()

    temp_x = x_LL.head

    while temp_x != None:
        hash_map_nodes[temp_x] = None
        temp_x = temp_x.next

    temp_y = y_LL.head

    while temp_y != None:
        if temp_y in hash_map_nodes.keys():
            return temp_y

        temp_y = temp_y.next

    return None


if __name__ == "__main__":
    #does not have an intersection
    a_LL = LinkedList([Node('a'), Node('b'), Node('c'), Node('d')])
    b_LL = LinkedList([Node('e'), Node('f'), Node('g'), Node('h')])

    print(intersecting_node(a_LL, b_LL))
    
    
    #has an intersection
    i = Node('i')
    i.next = Node('j')

    x_LL = LinkedList([Node('a'), Node('b'), i])
    y_LL = LinkedList([Node('e'), Node('f'), Node('g'), i])

    print(intersecting_node(x_LL, y_LL))

