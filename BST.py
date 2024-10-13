class Node:
  def __init__(self, key):
   self.left = None
   self.right = None
   self.val = key
def insert(root, key):
 if root is None:
  return Node(key)
 else:
  if key < root.val:
   root.left = insert(root.left, key)
  else:
     root.right = insert(root.right, key)
 return root
def inorder_traversal(root):
 if root:
   inorder_traversal(root.left)
   print(root.val, end=" ")
   inorder_traversal(root.right)
# Membuat tree
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print("Inorder traversal dari binary search tree:")
inorder_traversal(root)
