// See https://aka.ms/new-console-template for more information
public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int val=0, ListNode next=null) {
          this.val = val;
          this.next = next;
      }
  }
public class Solution {
    public ListNode SwapPairs(ListNode head) {
        if(head == null){
            return head;
        }

        List<ListNode> nodes = new List<ListNode>();
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        while(head != null){
            nodes.Add(head);
            head = head.next;
        }
        if(nodes.Count == 1){
            return nodes[0];
        }
        for(int i=0; i<nodes.Count-1;i+=2){
            (nodes[i],nodes[i+1]) = (nodes[i+1],nodes[i]);
        }
        foreach(ListNode node in nodes){
            Console.Write(node.val);
        }

        for(int j = 0; j<nodes.Count;j++){
            curr.next = nodes[j];
            curr = curr.next;

            if(j == nodes.Count-1){
                curr.next = null;
            }
        }
        return dummy.next;
    }
}
