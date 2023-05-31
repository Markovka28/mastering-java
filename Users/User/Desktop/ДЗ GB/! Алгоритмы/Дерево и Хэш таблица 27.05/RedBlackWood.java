// преобразование дерева поиска в левостороннее красно-черное дерево. 
// реализация в дереве метода добавления новых элементов с балансировкой.
public class RedBlackTree{
    private void colorSwap (Node node){
    private Node root;
// обработка коренной ноды
    public boolean add(int value){
        if(root != null){
            boolean result = addNode(root, value);
            root = rebalance(root);
            root.color = Color.BLACK;       //Корень дерева всегда черный
            return result;
        }else{
            root = new Node();
            root.color = Color.BLACK;
            root.value = value;
            return true;
        }
    }
// метод добавляющий новую ноду
    private boolean addNode(Node node, int value){ 
        if (node.value == value){
            return false;
        }else{
            if (node.value > value){
                boolean result = addNode(node.leftChild, value);
                node.leftChild = rebalance(node.leftChild);
                return result;
            }else{
                node.leftChild = new Node();
                node.leftChild.color = Color.RED;           //Новая нода всегда красная
                node.leftChild.value = value;
                return true;
            }
        }else{
            if (node.rightChild != null){
                boolean result = addNode(node.rightChild, value);
                node.rightChild = rebalance(node.rightChild);
                return result;
            }else{
                node.rightChild = new Node();
                node.rightChild.color = Color.RED;              //Новая нода всегда красная
                node.rightChild.value = value;
                return true;
            }
        }
    } 
//ребалансировка
    private Node rebalance(Node node){
        Node result = node;
        boolean needRebalance;
        do{
            needRebalance = false;
            if(result.rightChild != null && result.rightChild.color == Color.RED &&
                (result.leftChild == null || result.leftChild.color == Color.BLACK)){
            needRebalance = true;
            result = rightSwap(result);
            }
            if(result.leftChild != null && result.leftChild.color == Color.RED &&
                result.leftChild.leftChild != null && result.leftChild.leftChild.color == Color.RED){
            needRebalance = true;
            result = leftSwap(result);
            }
            if (result.leftChild != null && result.leftChild.color == Color.RED &&
                    result.rightChild != null && result.rightChild.color == Color.RED){
                needRebalance = true;
                colorSwap(result);
            }
        }
        while(needRebalance):
        return result;
    }
//правосторонний поворот
    private Node rightSwap(Node node){
        Node rightChild = node.rightChild;
        Node betweenChild = rightChild.leftChild;
        rightChild.leftChild = node;
        node.rightChild = betweenChild;
        rightChild.color = node.color;
        node.color = Color.RED;
        return rightChild;
    }
//левосторонний поворот
    private Node leftSwap(Node node){
        Node leftChild = node.leftChild;            // берем левого ребенка в отдельную переменную
        Node betweenChild = leftChild.rightChild;   // промежуточный элемент сменяющий родителя
        leftChild.rightChild = node;                // вместо правого ребенка красной ноды назначем корренной элемент
        node.leftChild = betweenChild;              // левым элементом родителя становится промежуточный элемент (имеющий значение между красной нодой и коренной)
        leftChild.color = node.color;               // левый ребенок поолучает цвет своего родителя
        node.color = Color.RED;                     // корень опускаясь ниже становится красным
        return leftChild;
    }
// смена цвета
    private void colorSwap(Node node){          
        node.rightChild.color = Color.BLACK;    // берем детей ноды присваиваем им черные цвета
        node.leftChild.color = Color.BLACK;     // У КРАСНОЙ НОДЫ ВСЕ ДЕТИ ЧЕРНОГО ЦВЕТА 
        node.color = Color.RED;                 // а само дерево становится красным при этом изменение цвета происходит только тогда когда у ноды два черных ребенка
    }
}
// параметры дерева
private class Node{ 
    private int value;  // значение хранящеся в узле
    private Color color;
    private Node leftChild;
    private Node rightChild;

    @Override
    public String toString(){
        return "Node{" +
        "value=" + value +
        ", color=" + color +
        '}';
    }
    private enum Color {
        RED, BLACK                  //Каждая нода имеет цвет (красный или черный)
    }
}
}