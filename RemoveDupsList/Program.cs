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
    public ListNode DeleteDuplicates(ListNode head) {
        HashSet<int> uniques = new HashSet<int>();
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while(head != null){
            if(!uniques.Contains(head.val)){
                curr.next = head;
                curr = curr.next;
                uniques.Add(head.val);
            }else{
               curr.next = null;
            }
            head = head.next;
        }
        return dummy.next;
    }
}
