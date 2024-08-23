class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if(not root):
            return None
        self.flatten(root.left)
        self.flatten(root.right)

        if(root.left):
            right = root.right
            root.right = root.left
            root.left = None
            last = root
            while(last.right):
                last = last.right
            last.right = right
