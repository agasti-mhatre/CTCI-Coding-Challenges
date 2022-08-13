class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None


    def add_node(self, node):
        if node.val == self.val:
            return
        elif node.val < self.val:
            if self.left == None:
                self.left = node
            else:
                self.left.add_node(node)
        elif node.val > self.val:
            if self.right == None:
                self.right = node
            else:
                self.right.add_node(node)


class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.tail = list_of_nodes[0]

            index = 1
            while index < len(list_of_nodes):
                self.add_node(list_of_nodes[index])
                index += 1


    def add_node(self, node):
        if self.head == self.tail == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
    

class Queue(LinkedList):
    def enqueue(self, node):
        self.add_node(node)


    def dequeue(self):
        if self.head == None:
            raise Exception("Can't dequeue from an empty queue!")
        elif self.head == self.tail:
            node = self.head
            self.head = self.tail = None
            return node
        else:
            node = self.head
            self.head = self.head.next
            node.next == None
            return node

    
    def isEmpty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False


def find_val(tree, search_val):
    if search_val == tree.val:
        pointer = tree
        return pointer
    elif search_val < tree.val:
        if tree.left != None:
            return find_val(tree.left, search_val)
        else:
            return None
    elif search_val > tree.val:
        if tree.right != None:
            return find_val(tree.right, search_val)
        else:
            return None
    

def is_subtree(t1, t2):
    if t2 == None:
        return True
    else:
        root_t1 = find_val(t1, t2.val)

        if root_t1 != None:
            t1_q1 = Queue()
            t1_q2 = Queue()
            t2_q1 = Queue()
            t2_q2 = Queue()

            switch = 1

            t1_q1.enqueue(Node(root_t1))
            t2_q1.enqueue(Node(t2))

            while not(t2_q1.isEmpty()) or not(t2_q2.isEmpty()):
                if switch:
                    node_t1 = t1_q1.dequeue().val
                    node_t2 = t2_q1.dequeue().val

                    if node_t1.val != node_t2.val:
                        return False

                    if node_t2.left != None:
                        if node_t1.left != None:
                            t1_q2.enqueue(Node(node_t1.left))
                        else:
                            return False
                        t2_q2.enqueue(Node(node_t2.left))
                     
                    if node_t2.right != None:
                        if node_t1.right != None:
                            t1_q2.enqueue(Node(node_t1.right))
                        else:
                            return False
                        t2_q2.enqueue(Node(node_t2.right))

                    if t2_q1.isEmpty():
                        switch = 0
                else:
                    node_t1 = t1_q2.dequeue().val
                    node_t2 = t2_q2.dequeue().val

                    if node_t1.val != node_t2.val:
                        return False

                    if node_t2.left != None:
                        if node_t1.left != None:
                            t1_q1.enqueue(Node(node_t1.left))
                        else:
                            return False
                        t2_q1.enqueue(Node(node_t2.left))
     
                    if node_t2.right != None:
                        if node_t1.right != None:
                            t1_q1.enqueue(Node(node_t1.right))
                        else:
                            return False
                        t2_q1.enqueue(Node(node_t2.right))

                    if t2_q2.isEmpty():
                        switch = 1

            return True
        else:
            return False



if __name__ == "__main__":
    t1 = TreeNode(4)
    t1.add_node(TreeNode(2))
    t1.add_node(TreeNode(3))
    t1.add_node(TreeNode(1))
    t1.add_node(TreeNode(6))
    t1.add_node(TreeNode(5))
    t1.add_node(TreeNode(7))

    t2 = TreeNode(4)
    t2.add_node(TreeNode(2))
    t2.add_node(TreeNode(3))
    t2.add_node(TreeNode(1))
    t2.add_node(TreeNode(6))
    t2.add_node(TreeNode(5))


    print(is_subtree(t1, t2))