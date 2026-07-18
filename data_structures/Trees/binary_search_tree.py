class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __contains__(self, value):
        return self.search(value)
    
    def __len__(self):
        return self.count_nodes()
    
    def __repr__(self):
        return f"BinarySearchTree({self.inorder()})\n"
    
    def __str__(self):
        return (
            f"BinarySearchTree with root value: {self.root.value if self.root else None}\n"
            f"Height: {self.height()}\n"
            f"Nodes: {self.count_nodes()}\n"
            f"Leaves: {self.count_leaves()}\n"
            f"Inorder: {self.inorder()}\n"
        )
    
    def is_empty(self):
        return self.root is None
    
    def clear(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return TreeNode(value)

        if value < node.value:
            node.left = self.__insert(node.left, value)

        elif value > node.value:
            node.right = self.__insert(node.right, value)

        return node
    
    def search(self, value):
        return self.__search(self.root, value)
    
    def __search(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self.__search(node.left, value)

        return self.__search(node.right, value)
    
    def count_nodes(self):
        return self.__count_nodes(self.root)
    
    def __count_nodes(self, node):
        if node is None:
            return 0
        
        return self.__count_nodes(node.left) + self.__count_nodes(node.right) + 1
    
    def height(self):
        return self.__height(self.root)
    
    def __height(self, node):
        if node is None:
            return 0

        height_left = self.__height(node.left) + 1
        height_right = self.__height(node.right) + 1

        return max(height_left, height_right)
    
    def count_leaves(self):
        return self.__count_leaves(self.root)
    
    def __count_leaves(self, node):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        count = self.__count_leaves(node.left) + self.__count_leaves(node.right)

        return count

    def minimum(self):
        if self.root is None:
            return "Empty Tree"
        
        node = self.root
        
        while node.left:
            node = node.left

        return node.value
    
    def maximum(self):
        if self.root is None:
            return "Empty Tree"
        
        node = self.root
        
        while node.right:
            node = node.right

        return node.value
    
    def inorder(self):
        return self.__inorder(self.root)
    
    def __inorder(self, node):
        if node is None:
            return []

        return self.__inorder(node.left) + [node.value] + self.__inorder(node.right)
    
    def preorder(self):
        return self.__preorder(self.root)
    
    def __preorder(self, node):
        if node is None:
            return []

        return [node.value] + self.__preorder(node.left) + self.__preorder(node.right)
    
    def postorder(self):
        return self.__postorder(self.root)
    
    def __postorder(self, node):
        if node is None:
            return []

        return self.__postorder(node.left) + self.__postorder(node.right) + [node.value]

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        if node is None:
            raise KeyError(value)

        if value < node.value:
            node.left = self.__delete(node.left, value)

        elif value > node.value:
            node.right = self.__delete(node.right, value)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self.__minimum(node.right)
            node.value = successor.value
            node.right = self.__delete(node.right, successor.value)

        return node

    def __minimum(self, node):
        while node.left is not None:
            node = node.left
        return node