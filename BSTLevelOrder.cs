
public class TreeNode {
      public int val;
      public TreeNode left;
      public TreeNode right;
      public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        IList<TreeNode> queue = new List<TreeNode>();
        IList<IList<int>> result = new List<IList<int>>();
        if(root == null){
            return result;
        }

        queue.Add(root);
        while(queue.Count > 0){
            int len = queue.Count;
            IList<int> vals = new List<int>();
            for (int i=0;i<len;i++){
                TreeNode curr = queue[0];
                queue.RemoveAt(0);
                vals.Add(curr.val);
                if(curr.left != null){
                    queue.Add(curr.left);
                }
                if(curr.right != null){
                    queue.Add(curr.right);
                }
            }
            result.Add(vals);
        }
        return result;
    }
};
