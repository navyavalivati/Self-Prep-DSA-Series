class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
        this.next = null;
    }
    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}

public class ArraytoLL {
    
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        Node head = convertToLL(arr);
        while(head != null) {
            System.out.print(head.data + "->");
            head = head.next;
        }
    }
    public static Node convertToLL(int[] arr) {
        Node head = new Node(arr[0]);
        Node mover = head;
        for(int i=1;i<arr.length;i++) {
            Node temp = new Node(arr[i]);
            mover.next = temp;
            mover = mover.next;
        }
        return head;
    }
}