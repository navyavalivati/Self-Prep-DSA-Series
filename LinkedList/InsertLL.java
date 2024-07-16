/* Inserting at different positions in the linked list */
import java.io.*;
import java.util.*;
class Node {
        int data;
        Node next;
        Node() {
            this.data = 0;
            this.next = null;
        }
        Node(int data) {
            this.data = data;
            this.next = null;
        }
        Node(int data, Node next) {
            this.data =data;
            this.next = next;
        }
    }  

public class InsertLL {
    
    static private Node head;
    public InsertLL() {
        head = null;
    }
    /* Insert at beginning of the linked list */
    public static void insertBegin(int data) {
        Node new_node = new Node(data);
        new_node.next = head;
        head = new_node;
         
    }

    /*Insert after a give node in linked list */
    public static void insertAfterNode(Node prev_node , int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = prev_node.next;
        prev_node.next = new_node;
    }
    
    /* Insert at End of the linked list */
    public static void insertEnd(int data) {
        Node new_node = new Node(data);
        if(head == null) {
            head = new_node;
            return;
        }
        Node last = head;
        while(last.next != null) {
            last = last.next;
        }
        last.next = new_node;
    }

    public static void printList() {
        Node temp = head;
        while(temp != null) {
            System.out.print(temp.data + "->");
            temp = temp.next;
        }
    }
    public static void main(String[] args) {
        InsertLL list = new InsertLL();
        
        list.insertBegin(5);
        list.insertBegin(10);
        list.insertAfterNode(head, 15);
        list.insertEnd(20);
        list.printList();
    }
}