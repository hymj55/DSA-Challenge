#Insertion and Search a value

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def search(node, target): #매개변수: 현재출발할노드, 찾을값
    #Case 1, could not find anything
    if node is None:    # tree is empty
        return None

    #Case 2: found the target
    elif node.data == target:
        return node

    #Case 3: Target is less than the node you are at
    elif target < node.data:
        return search(node.left, target)

    #Case 4: Target is greater than the node
    elif target > node.data:
        return search(node.right, target)


def insert(node, data):  #여기서 매개변수 node는 처음은 root node가 될수있겠지만, 실질적으로는 현재 탐색중인 노드//현재 바라보고있는 위치의 노드
    #Base Case - when you have an empty spot(child)
    if node is None:
        return TreeNode(data)

    else:
        if data < node.data:
            node.left = insert(node.left, data)

        elif data > node.data:
            node.right = insert(node.right, data)
    return node     #결국은 새노드를 삽입할 자리찾기는 return TreeNode(data) 이 라인에서 함수가 종료되지만,
                    #재귀호출 덕분에 그 추가된 노드의 부모노드로 거슬러올라가면서 계속 자식이 업데이트된 새로운 부모를 반환하고, 결국에는 처음 넣은 루트노드까지 업데이트된 채로 반환된다.

# Leaf 위치에서 새 노드 생성 > return TreeNode(data) > 그 순간 함수 종료
# 재귀 호출 덕분에 새 노드가 바로 위 부모의 node.left 또는 node.right에 연결
# 부모 노드 함수는 마지막 return node를 통해 자기 자신(이제 자식이 업데이트된 상태)을 다시 위 부모에게 반환
# 이 과정이 루트까지 반복 > 최종적으로 루트 노드가 업데이트된 전체 트리 구조를 갖고 반환됨

root = None
root = insert(root, 13) #first insert니까 13이  if node is None: return TreeNode(data) 이 조건에 해당되서 바로 루트노드가됨

insert(root, 7)
insert(root, 15)
insert(root, 3)
insert(root, 8)
insert(root, 14)
insert(root, 19)
insert(root, 18)

#Check if this is actually a binary search tree or not
print("Inorder traversal")
inOrderTraversal(root)

print("\n")

#Searching
print("Searching for value 8")
found_node = search(root, 8)
if found_node:
    print(f"I found the node with data {found_node.data}")
else:
    print("Node not found")