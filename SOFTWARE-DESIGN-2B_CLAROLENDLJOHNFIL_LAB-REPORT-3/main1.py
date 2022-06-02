#a.1
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def deleteNode(self, position):

        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def sortLinkedList(self, head):
        current = head
        index = Node(None)
        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)
    print('linked list:')
    llist.printList()
    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()
    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")
    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()'''

#b.1
'''class Node:
    def __init__(self):
        self.coeff = None
        self.power = None
        self.next = None

def addnode(start, coeff, power):
    newnode = Node();
    newnode.coeff = coeff;
    newnode.power = power;
    newnode.next = None;
    if (start == None):
        return newnode;
    ptr = start;
    while (ptr.next != None):
        ptr = ptr.next;
    ptr.next = newnode;
    return start;

def printList(ptr):
    while (ptr.next != None):
        print(str(ptr.coeff) + 'x^' + str(ptr.power), end='')
        if (ptr.next != None and ptr.next.coeff >= 0):
            print('+', end='')
        ptr = ptr.next
    print(ptr.coeff)

def removeDuplicates(start):
    ptr2 = None
    dup = None
    ptr1 = start;
    while (ptr1 != None and ptr1.next != None):
        ptr2 = ptr1;
        while (ptr2.next != None):
            if (ptr1.power == ptr2.next.power):
                ptr1.coeff = ptr1.coeff + ptr2.next.coeff;
                dup = ptr2.next;
                ptr2.next = ptr2.next.next;
            else:
                ptr2 = ptr2.next;
        ptr1 = ptr1.next;

def multiply(poly1, Npoly2, poly3):
    ptr1 = poly1;
    ptr2 = poly2;

    while (ptr1 != None):
        while (ptr2 != None):
            coeff = ptr1.coeff * ptr2.coeff;
            power = ptr1.power + ptr2.power;
            poly3 = addnode(poly3, coeff, power);
            ptr2 = ptr2.next;
        ptr2 = poly2;
        ptr1 = ptr1.next;
    removeDuplicates(poly3);
    return poly3;

if __name__ == '__main__':
    poly1 = None
    poly2 = None
    poly3 = None;

    poly1 = addnode(poly1, 3, 3);
    poly1 = addnode(poly1, 6, 1);
    poly1 = addnode(poly1, -9, 0);
    poly2 = addnode(poly2, 9, 3);
    poly2 = addnode(poly2, -8, 2);
    poly2 = addnode(poly2, 7, 1);
    poly2 = addnode(poly2, 2, 0);

    print("1st Polynomial:- ", end='');
    printList(poly1);

    print("2nd Polynomial:- ", end='');
    printList(poly2);

    poly3 = multiply(poly1, poly2, poly3);

    print("Resultant Polynomial:- ", end='');
    printList(poly3);'''

#a.2
'''class stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100

    def isEmpty(self):

        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):

        if self.top == self.max - 1:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print('Stack OverFlow')
            return
        else:
            self.top += 1
            self.array.append(data)

    def pop(self):

        if self.isEmpty():
            print('Stack UnderFlow')
            return
        else:
            self.top -= 1
            return self.array.pop()

class SpecialStack(stack):

    def __init__(self):
        super().__init__()
        self.Min = stack()

    def push(self, x):
        if self.isEmpty():
            super().push(x)
            self.Min.push(x)
        else:
            super().push(x)
            y = self.Min.pop()
            self.Min.push(y)
            if x <= y:
                self.Min.push(x)
            else:
                self.Min.push(y)

    def pop(self):
        x = super().pop()
        self.Min.pop()
        return x

    def getmin(self):
        x = self.Min.pop()
        self.Min.push(x)
        return x

if __name__ == '__main__':
    s = SpecialStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.getmin())
    s.push(5)
    print(s.getmin())'''

#b.2
'''class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()'''

#a.3
'''class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)'''

#b.3
'''class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),

def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)'''

#c.3
'''class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def left_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.left
    return ht

def right_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.right
    return ht

def TotalNodes(root):
    if (root == None):
        return 0
    lh = left_height(root)
    rh = right_height(root)
    if (lh == rh):
        return (1 << lh) - 1
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)

print(TotalNodes(root))'''

#a.4
'''import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)'''

#a.5
'''def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'L')
insert(HashTable, 25, 'E')
insert(HashTable, 20, 'N')
insert(HashTable, 9, 'D')
insert(HashTable, 21, 'L')
insert(HashTable, 21, 'C')

display_hash(HashTable)'''