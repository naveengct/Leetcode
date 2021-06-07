
class Solution(object):
    def kthSmallest(self, root, k):
        res = []
        def inorder(root):
            if root is None:
                return
            else:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
                
        inorder(root)
        return res.pop(k-1)
