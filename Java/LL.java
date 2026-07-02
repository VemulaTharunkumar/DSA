import java.util.*;
class Node {
    int data;
    Node next;
    Node(int d){
        data=d;
        next=null;
    }
}
public class LL{
    static Node head=null;
    public static Node insert(Node head,int d){
        Node t=new Node(d);
        if(head==null){
            head=t;
            return head;
        }
        Node curr=head;
        while(curr.next!=null){
            curr=curr.next;
        }
        curr.next=t;
        return head;
    }
    public static void display(Node head){
        if(head==null){
            return;
        }
        Node curr=head;
        while(curr!=null){
            System.out.print(curr.data+"-> ");
            curr=curr.next;
        }
    }
    public static Node reverse(Node head){
        Node prev=null;
        Node curr=head;
        Node n=null;
        while(curr.next!=null){
            n=curr.next;
            curr.next=prev;
            prev=curr;
            curr=n;
        }
        head=prev;
        return head;
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        LL l=new LL();
        while(true){
            int x=sc.nextInt();
            switch (x) {
                case 1:
                    int c=sc.nextInt();
                    head=l.insert(head,c);
                    break;
                case 2:
                    l.display(head);
                    break;  
                case 3:
                    head=l.reverse(head);
                    break;
                case 4:
                    System.exit(0);    
                default:
                    System.out.print("Invalid choice");          
            }}
        }
    }
