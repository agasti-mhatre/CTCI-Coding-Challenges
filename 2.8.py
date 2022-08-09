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


def has_cycle(x_LL):
    temp = x_LL.head
    values_seen = dict()

    while temp != None:
        if temp.val in values_seen:
            return temp
        else:
            values_seen[temp.val] = temp.val

        temp = temp.next

    print("This linked list has no cycles")
    return None


if __name__ == "__main__":
    x_LL = LinkedList([Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('C')])

    print(has_cycle(x_LL).val)