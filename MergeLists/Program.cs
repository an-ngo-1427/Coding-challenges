// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int val=0, ListNode next=null) {
          this.val = val;
          this.next = next;
      }
  }
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null && list2 == null){
            return list1;
        }
        ListNode result = new ListNode();
        ListNode dummy = result;
        while(list1 != null || list2 != null){

            if(list1 == null){
                dummy.next = list2;
                break;
            }
            if(list2 == null){
                dummy.next = list1;
                break;
            }
            ListNode node1 = new ListNode(list1.val);
            ListNode node2 = new ListNode(list2.val);
            if(node1.val < node2.val){
                dummy.next = node1;
                list1 = list1.next;
            }else{
                dummy.next = node2;
                list2 = list2.next;
            }

            dummy = dummy.next;

        }
        return result.next;
    }
}
