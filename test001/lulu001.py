class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0
    def pathMulMax2(self,root):
        if root == None:
            return 1,1
        lmin,lmax = self.pathMulMax2(root.left)
        rmin,rmax = self.pathMulMax2(root.right)
        a = [lmin * root.val, lmax * root.val, rmin * root.val, rmax * root.val, root.val]
        self.result = max([lmin*rmin*root.val,lmin*rmax*root.val,lmax*rmin*root.val,lmax*rmax*root.val]+[self.result]+a)
        return min(a),max(a)
    def pathMulMax(self,root):
        if root == None:
            return None
        self.pathMulMax2(self,root)
        return self.result


a = TreeNode(1)
b = TreeNode(2)
