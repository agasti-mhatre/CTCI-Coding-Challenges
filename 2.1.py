'''
###First method - Temporary Buffer Allowed
class Node:
    def __init__(self, val = None):
        self.value = val
        self.next = None

    def get_val(self):
        return self.value

    def set_val(self, val):
        self.value = val


class LinkedList:
    def __init__(self, list_of_nodes = [Node()]):
        self.head = list_of_nodes[0]

        if len(list_of_nodes) > 1:
            count = 1
            while count < len(list_of_nodes):
                self.add_node(list_of_nodes[count])
                count += 1


    def add_node(self, node):
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = node


    def print_nodes(self):
        temp = self.head
        while temp.next != None:
            print(temp.value)
            temp = temp.next

        print(temp.value)


    def remove_duplicates(self):
        duplicates = dict()

        prev = self.head
        temp = self.head
        while temp.next != None:
            if temp.value in duplicates: 
                prev.next = temp.next
                temp.next = None
                temp = prev.next
            else:
                duplicates[temp.value] = temp.value
                prev = temp
                temp = temp.next

        if prev.next != None:
            if prev.next.value in duplicates: 
                prev.next = temp.next
                temp.next = None



if __name__ == "__main__":
    list_nodes = [Node(6), Node(1), Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]
    e = LinkedList(list_nodes)
    e.remove_duplicates()
    
    e.print_nodes()
'''




#Second method - No Temporary Buffer

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


    def print_list(self):
        temp = self.head
        while temp.next != None:
            print(temp.value, end=" ")
            temp = temp.next

        print(temp.value, end=" ")

    def remove_duplicates(self):
        stationary = self.head
        moving = None

        while stationary.next != None:
            moving = stationary.next
            temp = stationary
            while moving.next != None:
                #print(stationary.value, " ", moving.value)
                if stationary.value == moving.value:
                    temp.next = moving.next
                    moving.next = None
                    moving = temp.next
                else:
                    temp = temp.next
                    moving = moving.next

            
            #print(stationary.value, " ", moving.value)
            if stationary.value == moving.value:
                temp.next = moving.next
                moving.next = None
                moving = temp.next

            if stationary.next == None:
                break
            stationary = stationary.next
                

if __name__ == "__main__":
    list_nodes = [Node(1), Node(1), Node(5), Node(5), Node(6), Node(6)]
    x_list = LinkedList(list_nodes)

    x_list.remove_duplicates()
    x_list.print_list()