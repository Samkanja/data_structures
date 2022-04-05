class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Binary_search:
    def __init__(self):
        self.root = None

    
    def insert(self, e):
        if self.root is None:
            self.root = Node(e)
        else:
            self.insertNode(e, self.root)
    
    def insertNode(self, e, node):
        if e  < node.val:
            if node.left:
                self.insertNode(e, node.left)
            else:
                node.left = Node(e)

        elif e > node.val:
            if node.right:
                self.insertNode(e, node.right)
            else:
                node.right = Node(e)

        else:
            print('node already exits')
    
    def traverse(self):
        if self.root:
            self.inordertraverse(self.root)
    
    def inordertraverse(self, node):
        
        if node.left:
            self.inordertraverse(node.left)
        print(node.val)
        if node.right:
            self.inordertraverse(node.right)

    def getmin(self):
        if self.root:
            return self.findMin(self.root)
    
    def findMin(self, node):
        if node.left:
            return self.findMin(node.left)
        return node.val
    
    def getmax(self):
        if self.root:
            return self.findMax(self.root)
    def findMax(self, node):
        if node.right:
            return self.findMax(node.right)
        return node.val
    
    def search(self, e):
        if self.root:
            return self.searchNode(e, self.root)
        else:
            return False
    
    def searchNode(self,e, node):
        if e == node.val:
            return True
        elif e < node.val:
            if node.left:
                return self.searchNode(e, node.left)
        else:
            if node.right:
                return self.searchNode(e, node.right)
        return False

    def remove(self, e):
        if self.root:
            self.root = self.removeNode(e, self.root)
    def removeNode(self, e,node):
        if e < node.val:
            node.left = self.removeNode(e, node.left)
        elif e > node.val:
            node.right = self.removeNode(e, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            left_max = self.getPredecessor(node.left)
            node.val = left_max.val
            node.left = self.removeNode(left_max.val, node.left)
        return node
            

    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node

            





def build_tree(elements):
    tree = Binary_search()
    for i in range(len(elements)):
        tree.insert(elements[i])
    return tree


if __name__ == '__main__':
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(nums)
    print(tree.traverse())
    print(tree.getmax())
    print(tree.getmin())
    print(tree.search(10))
    print(tree.remove(20))
    print(tree.traverse())