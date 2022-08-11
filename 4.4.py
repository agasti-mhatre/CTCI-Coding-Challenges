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
                return self.left.add_node(node)
        elif node.val > self.val:
            if self.right == None:
                self.right = node
            else:
                return self.right.add_node(node)
        
class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None


class Stack:
    def __init__(self, list_of_nodes = []):
        if len(list_of_nodes) == 0:
            self.head = None
            self.tail = None
        else:
            self.head = list_of_nodes[0]
            self.tail = self.head
            
            index = 1
            while index < len(list_of_nodes):
                self.push(list_of_nodes[index])
                index += 1


    def push(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next


    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from empty stack!")
        elif self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            node.prev = None
            self.tail.next = None
            return node


    def isEmpty(self):
        return (self.head == None) and (self.tail == None)


def is_balanced(tree):
    parent_nodes = Stack()
    visited = dict()
    root = tree
    parent_nodes.push(Node(root))

    while not(parent_nodes.isEmpty()):
        #node = parent_nodes.head
        #while node != None:
        #    print(node.val.val, end = "->")
        #    node = node.next
        #print()

        if (root.left == None) and (root.right == None):
            visited[root] = 0
            root = parent_nodes.pop().val
        elif (root.left in visited) and (root.right in visited):
            if abs(visited[root.left] - visited[root.right]) > 1:
                return False
            else:
                visited[root] = visited[root.left] + visited[root.right] + 2
                root = parent_nodes.pop().val
        elif (root.left in visited) and (root.right == None):
            if visited[root.left] > 1:
                return False
            else:
                visited[root] = visited[root.left] + 1
                root = parent_nodes.pop().val
        elif (root.left == None) and (root.right in visited):
            if visited[root.right] > 1:
                return False
            else:
                visited[root] = visited[root.right] + 1
                root = parent_nodes.pop().val

        if (root.left != None) and (root.left not in visited):
            parent_nodes.push(Node(root))
            root = root.left
        elif (root.right != None) and (root.right not in visited):
            parent_nodes.push(Node(root))
            root = root.right



        #for node, level in visited.items():
        #    print(node.val, ":", level, end= '\t')
        #print()

    #for node, level in visited.items():
    #    print(node.val, ":", level, end= '\t')
    #print()

    return True
    
'''
        4
      /    \
     2      6
    / \    / \
   1   3  5   7

'''
        
if __name__ == "__main__":
    tree = TreeNode(4)
    tree.add_node(TreeNode(2))
    tree.add_node(TreeNode(1))
    tree.add_node(TreeNode(3))
    tree.add_node(TreeNode(6))
    tree.add_node(TreeNode(5))
    tree.add_node(TreeNode(7))
    
 
    print(is_balanced(tree))