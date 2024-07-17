// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
public class Node {
    public int val;
    public Node next;
    public Node random;

    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
public class Solution {
    public Node CopyRandomList(Node head) {
        List<Node> randoms = new List<Node>();
        randoms.Add(head.random);
        Node copy = new Node(head.val);
        Node curr = copy;
        while(head != null){
            head = head.next;
            randoms.Add(head.random);
            Node newNode = new Node(head.val);
            curr.next = newNode;
            curr = curr.next;
        }

        Node copyCurr = copy;
        for( int i=0;i<randoms.Count;i++){
            copyCurr.random = randoms[i];
            copyCurr = copyCurr.next;
        }
        return copy;
    }
}
