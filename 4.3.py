class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    
    def add_node(self, node):
        if node.val < self.val:
            if self.left == None:
                self.left = node
            else:
                self.left.add_node(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.add_node(node)


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            self.tail = None
        else:
            self.head = list_of_nodes[0]
            self.tail = self.head

            index = 1
            while index < len(list_of_nodes):
                self.add_node(list_of_nodes[index])
                index += 1


    def add_node(self, node):
        if (self.head == None) and (self.tail == None):
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next


class Queue(LinkedList):
    def enqueue(self, node):
        self.add_node(node)


    def dequeue(self):
        if (self.head == None) and (self.tail == None):
            raise Exception("Cannot dequeue from empty queue!")
        elif (self.head == self.tail):
            temp = self.head
            self.head = self.tail = None
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None

            return temp


    def isEmpty(self):
        if (self.head == None) and (self.tail == None):
            return True
        else:
            return False


def find_levels(tree):
    levels = 1
    queue_one = Queue([Node(tree)])
    queue_two = Queue()
    levels_tree = dict()
    switch = 1

    while not(queue_one.isEmpty()) or not(queue_two.isEmpty()):
        if switch == 1:
            node = queue_one.dequeue()
            if node.val.left != None:
                queue_two.enqueue(Node(node.val.left))
            if node.val.right != None:
                queue_two.enqueue(Node(node.val.right))
            
            if levels in levels_tree:
                levels_tree[levels].append(node.val)
            else:
                levels_tree[levels] = [node.val]

            if queue_one.isEmpty():
                switch = 2
                levels += 1

        elif switch == 2:
            node = queue_two.dequeue()
            if node.val.left != None:
                queue_one.enqueue(Node(node.val.left))
            if node.val.right != None:
                queue_one.enqueue(Node(node.val.right))
            
            if levels in levels_tree:
                levels_tree[levels].append(node.val)
            else:
                levels_tree[levels] = [node.val]

            if queue_two.isEmpty():
                switch = 1
                levels += 1

    return levels_tree


def create_linkedlists(levels_tree):
    list_of_LLs = list()
    index = 0
    for node_list in levels_tree.values():
        list_of_LLs.append(LinkedList())
        for node in node_list:
            list_of_LLs[index].add_node(Node(node.val))
        
        index += 1

    return list_of_LLs




if __name__ == "__main__":
    tree = TreeNode(4)
    tree.add_node(TreeNode(2))
    tree.add_node(TreeNode(1))
    tree.add_node(TreeNode(3))
    tree.add_node(TreeNode(6))
    tree.add_node(TreeNode(5))
    tree.add_node(TreeNode(7))

    
    list_of_LLs = create_linkedlists(find_levels(tree))
    for LiL in list_of_LLs:
        temp = LiL.head
        while temp != None:
            print(temp.val, end = ' --> ')
            temp = temp.next

        print()