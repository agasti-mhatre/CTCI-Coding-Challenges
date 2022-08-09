from math import ceil
'bruhbbhurb'
#self.char_length = 10
#b = 1, 5, 6, 10
#r = 2, 9
#u = 3, 8
#h = 4, 7

'bruhbxbhurb'
#self.char_length = 11
#middle = 6


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            self.char_length = 0
        else:
            if (len(list_of_nodes[0].val) > 1):
                raise Exception("Only one character is allowed per node!")
            if list_of_nodes[0].val == ' ':
                raise Exception("No spaces allowed!")
            self.head = list_of_nodes[0]
            self.char_length = 1
            if len(list_of_nodes) > 1:
                index = 1
                while index < len(list_of_nodes):
                    self.add_node(list_of_nodes[index])
                    index += 1


    def add_node(self, node):
        if len(node.val) > 1:
            raise Exception("Only one character is allowed per node!")
        if node.val == ' ':
            raise Exception("No spaces allowed!")
        
        if self.head == None:
            self.head = node
            self.char_length = 0
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = node
        
            self.char_length += 1


def find_indexes(x_LL):
    if x_LL.char_length % 2 == 0:
        hash_map = dict()
        index = 1
        temp = x_LL.head
        while temp != None:
            if temp.val in hash_map:
                hash_map[temp.val].append(index)
            else:
                hash_map[temp.val] = [index]

            temp = temp.next
            index += 1
        
        return hash_map
    else:
        hash_map = dict()
        index = 1
        temp = x_LL.head
        while temp != None:
            if index == ceil(x_LL.char_length / 2):
                temp = temp.next
                index += 1              
                continue
            if temp.val in hash_map:
                hash_map[temp.val].append(index)
            else:
                hash_map[temp.val] = [index]

            temp = temp.next
            index += 1
        
        return hash_map

def is_LL_palindrome(x_LL):
    hash_map = find_indexes(x_LL)
    for index_list in hash_map.values():
        if len(index_list) % 2 == 0:
            start = 1
            end = x_LL.char_length
            i = 0
            for j in range(len(index_list) - 1, 0, -1):
                if i > j:
                    break
                if (index_list[i] - start) != (end - index_list[j]): 
                    return False

                i += 1
        else:
            return False

    return True





if __name__ == "__main__":
    #x_LL = LinkedList([Node('b'), Node('r'), Node('u'), Node('h'), Node('b'),  Node('b'), Node('h'), Node('u'), Node('r'), Node('b')])
    x_LL = LinkedList([Node('b'), Node('r'), Node('u'), Node('h'), Node('b'),  Node('x'), Node('b'), Node('h'), Node('u'), Node('r'), Node('b')])
    
    print(is_LL_palindrome(x_LL))