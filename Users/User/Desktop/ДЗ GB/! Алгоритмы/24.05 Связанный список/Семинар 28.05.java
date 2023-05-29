public static class List{
    private Node Head; // чтобы ноду никто не достал
    // все что ниже это нода
    private class Node {
    private int value; // значение и ссылка на следующий объект
    private Node next;
    }
    // МЕТОД ДОБАВЛЕНИЯ В НАЧАЛО ОДНОСВЯЗАННОГО СПИСКА и удаления 1го эл-та
void push(int value){ // параметр который пришел в качестве добавляемого
    Node node = new Node(); // создали новую ноду, хеад будт ссылаться на новую ноду которую мы только что создали
    node.value = value;
    node.next = Head; // null
    Head = node;        // сдвигаем хеад на новый начальный эл-т
}
//МЕТОД УДАЛЯЮЩИЙ 1Й ЭЛЕМЕНТ НОДЫ
Integer pop(){
    if(Head != null){
        Integer value = Head.value;
        Head = Head.next; //новый хэд это следуующий за нашим
        return value;
    }
    return null;
}
//МЕТОД КОТОРЫЙ ДОБАВЛЯЕТ НОДУ В КОНЕЦ
void pushBack(int value){
        Node node = new Node(); 
        node.value = value;
        Node current = Head;
        if (current != null){
            while (current.next != null){  // сюда просто так нельзя обращаться т.к. хеад мб пустым
            current = current.next; 
        }  
        current.next = node; // вставляем новый эл - т
    }else{
        Head = node;
    }
}
//МЕТОД ВЫВОДЯЩИЙ ВЕСЬ СПИСОК НА ЭКРАН
Node find(int value){ //это для того чтобы можно было вернуть 0 если ничего не нашли
    Node current = Head;
    while (current != null){ // пока в ноде есть ссылка на следующую ноду
        if(current.value == value){    //сравнить значение каррент с тем которое мы проверяем
        return current;
        }
        // System.out.println(current.value);
        current = current.next; // сдвигаем карент на карент некст
        }
        return null;
    } 
}


public static void main(String[] args) {
    List list = new List();
    list.pushBack(1); //добавить в лист элементы
    list.pushBack(2);
    list.pushBack(3);
    list.print();
    System.out.println(list.pop());
    list.print();
}
