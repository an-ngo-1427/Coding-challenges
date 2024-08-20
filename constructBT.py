class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if (not preorder and not inorder):
        return
    root = TreeNode(preorder[0])
    leftTreeLen = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:leftTreeLen+1],inorder[:leftTreeLen])
    root.right = buildTree(preorder[leftTreeLen+1:],inorder[leftTreeLen+1:])

    return root


buildTree([3,9,20,15,7],[9,3,15,20,7])
