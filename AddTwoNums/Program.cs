// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
/* *
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * } */

public class Solution {
    public class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int val=0, ListNode next=null) {
            this.val = val;
            this.next = next;
        }
    }
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        int carry = 0;
        while(l1 != null || l2!= null || carry >0){
            int val1 = l1 != null? l1.val:0;
            int val2 = l2 != null? l2.val:0;
            int val = val1 + val2 + carry;
            carry = val / 10;
            // Console.WriteLine($"{val1} + {val2} + {carry} = {val}");
            // Console.WriteLine(carry);
            ListNode newNode = new ListNode(val%10);
            curr.next = newNode;
            curr = curr.next;

            l1 = l1 != null? l1.next:null;
            l2 = l2 != null? l2.next:null;

        }
        return dummy.next;
    }


}
