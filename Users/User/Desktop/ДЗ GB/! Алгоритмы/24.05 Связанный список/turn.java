public static class List{
    private Node Head;          // чтобы Node никто не достал
    private class Node {
    private int value;          // значение и ссылка на следующий объект
    private Node next;
    }
    void push(int value){       // параметр который пришел в качестве добавляемого
        Node node = new Node(); // создали новую Node, Head будет ссылаться на новую только что созданную Node
        node.value = value;
        node.next = Head;       // null
        Head = node;            // сдвигаем Head на новый начальный эл-т
        }
        // МЕТОД РАЗВОРОТА 
    public void turn() {
        Node curNode = head;
        while(curNode != null){             // до тех пор пока проходим по списку 
            Node.next=curNode.next;
            Node previous = curNode previous
            curNode.next = previous;
            curNode.previous = next;
            curNode = next;
            if(previous == null){
            tail = curNode;
            }         
                if(next = null){
                head = curNode; 
                }
            }
        }
    }
//Разворот запускается если есть хотябы 2 Node
public static void main(String[] args) {
    List list = new List();
    list.print();
}