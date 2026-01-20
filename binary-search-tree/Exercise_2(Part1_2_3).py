# The Employee Hierarchy System
# You are managing a company database where every employee has a unique Employee ID.
# The hierarchy follows a Binary Search Tree structure.

# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Part 1: Building the Structure (Insertion)
def insert(root, key):
    # Base Case - when you have an empty spot
    if root is None:
        return Node(key)
    else:
        # Recursive Case - decide left or right
        if key < root.val:
            root.left = insert(root.left, key)
        elif key > root.val:
            root.right = insert(root.right, key)
    # Return the root so that updated child nodes are kept and passed up to the top
    return root


# Part 2: The Roll Call (Traversal) using In-order Traversal
def print_roll_call(root):
    if root is None:
        return
    # Traverse left subtree first (smaller IDs)
    print_roll_call(root.left)
    # Visit current node (print ID)
    print(root.val, end=" ")
    # Traverse right subtree (larger IDs)
    print_roll_call(root.right)


# Part 3: The Audit (Validation)
def is_valid_bst(root, min_allowed=None, max_allowed=None):
    # None means no minimum or maximum limit (used for root node)

    # Base case: An empty tree is valid because there are no rules to break. so, return True.
    if root is None:
        return True

    # Current node check:
    if min_allowed is not None:
        if root.val <= min_allowed:
            return False

    if max_allowed is not None:
        if root.val >= max_allowed:
            return False

    # Recursively check the left and right subtrees
    # Left child: max changes to parent's value
    # Right child: min changes to parent's value
    left_valid = is_valid_bst(root.left, min_allowed, root.val)
    right_valid = is_valid_bst(root.right, root.val, max_allowed)

    # return True only if both are true
    return left_valid and right_valid


#=========Test Cases=========

print("PART 1 & 2: Building Tree and Roll Call")

# Example Input from instruction
keys = [50, 30, 20, 40, 70]

# Build the tree
root = None
for key in keys:
    root = insert(root, key)

# Expected Result:
print(f"Print all Employee IDs (ascending order): ", end="")
print_roll_call(root)
print("\n")


print("PART 3: BST Validation")
# Test 1: Valid BST
print("1) Test 1: Valid BST")
root1 = Node(50)
root1.left = Node(30)
root1.right = Node(70)
root1.left.left = Node(20)
root1.left.right = Node(40)
root1.right.left = Node(60)
root1.right.right = Node(80)
print(f"Valid BST? {is_valid_bst(root1)}")  # True

# Test 2: Invalid BST
print("\n2) Test 2: Invalid BST")
root2 = Node(50)
root2.left = Node(30)
root2.right = Node(70)
root2.left.left = Node(20)
root2.left.right = Node(40)
root2.right.left = Node(25)  # Invalid part: 25 < 50, but in right subtree
root2.right.right = Node(80)
print(f"Valid BST? {is_valid_bst(root2)}")  # False