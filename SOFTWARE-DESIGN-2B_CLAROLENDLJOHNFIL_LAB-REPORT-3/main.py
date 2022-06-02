'''
#7.1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findSecondLastNode(head):
    temp = head

    if (temp == None or temp.next == None):
        return -1

    while (temp != None):
        if (temp.next.next == None):
            return temp.data
        temp = temp.next

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head

if __name__ == '__main__':
    head = None
    head = push(head, 12)
    head = push(head, 29)
    head = push(head, 11)
    head = push(head, 23)
    head = push(head, 8)

    print(findSecondLastNode(head))
'''


'''class LinkedList:
    def __init__(self):
        self.head = None

    def list_is_empty(self):
        return not self.head

    def add_to_front(self, new_node):
        if self.list_is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        list = ""
        current = self.head

        while current != None:
            list += f"{current.value} -> "
            current = current.next
        list += "None"
        return list

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_front(Node(1))
    linked_list.add_to_front(Node(2))
    linked_list.add_to_front(Node(3))
    linked_list.add_to_front(Node(4))
    linked_list.add_to_front(Node(5))'''

#7.3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

if __name__ == '__main__':
    llist = SinglyList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print("Count of nodes is :", llist.getCount())'''

#7.4
'''class LinkedList(object):
    def __init__(self):
        self.head = None

    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    def swapNodes(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def push(self, new_data):
        new_Node = self.Node(new_data)
        new_Node.next = self.head
        self.head = new_Node

    def printList(self):
        tNode = self.head
        while tNode != None:
            print(tNode.data),
            tNode = tNode.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked list before calling swapNodes()")
    llist.printList()
    llist.swapNodes(4, 3)
    print("Linked list after calling swapNodes()")
    llist.printList()'''
