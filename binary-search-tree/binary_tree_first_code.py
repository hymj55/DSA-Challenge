class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Create node
# root = TreeNode(13)
# node_a = TreeNode(20)
# node_b = TreeNode(30)
#
# root.left = node_a
# root.right = node_b
#
# print("Root node data:", root.data)
# print("Path data is (Root -> Left):", root.left.data)
# print("Path data is (Root -> Left -> Left):", root.left.left.data )


# Create nodes
root = TreeNode("R")
nodeA, nodeB = TreeNode("A"), TreeNode("B")
nodeC, nodeD, nodeE, nodeF, nodeG = TreeNode("C"), TreeNode("D"), TreeNode("E"), TreeNode("F"), TreeNode("G")

# Connections
root.left, root.right = nodeA, nodeB
nodeA.left, nodeA.right = nodeC, nodeD
nodeB.left, nodeB.right = nodeE, nodeF
nodeF.left = nodeG

# Leaf 노드  height = 0 이 되는 이유, leaf노드기준, leaf.left = 0, leaf.right = 0
# 그럼 리프 바로 아래에 자식이 실제로 없지만, 논리적으로 ‘빈 서브트리’까지 내려가는 방식에 의해 1을 똑같이 더하는것!!
# leaf노드부터 하단 노드까지(없는게 확인되기 전까진 자식이 있다는 가정하에) 1, 따라서 리프노드의 높이는 1 + max(-1, -1) = 0
# Empty subtree (None) height = -1

def calculate_height(node):
    #Base condition:
    if node is None: #None까지 내려가야 leaf노드 인지 판단 가능
        return -1       # Height of the empty list
    #Height formula = 1 + max(left subtree, right subtree)

    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    max_value = max(left_height, right_height)

    return 1 + max_value

height = calculate_height(root)
print(f"the height of the tree is the max edges from root to last leaf = {height}")