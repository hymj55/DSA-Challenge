#Preorder: Root - left - right
#Inorder: left - Root - right
#Postorder: left - right - Root


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):    #preOrderTraversal(우리가 찾을 노드 1개):
    if node is None:
        return

    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def inOrderTraversal(node):
    if node is None:
        return

    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)


def postOrderTraversal(node):
    if node is None:
        return

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=" ")


#Main Program/Part

root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("Preorder Traversal")
preOrderTraversal(root)


print("\nInorder Traversal")
inOrderTraversal(root)

print("\nPostorder Traversal")
postOrderTraversal(root)