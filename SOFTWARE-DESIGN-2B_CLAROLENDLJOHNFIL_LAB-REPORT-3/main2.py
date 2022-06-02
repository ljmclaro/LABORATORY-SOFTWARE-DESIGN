#7.44
'''from tkinter import *

app = Tk()

def shift_cursor1(event=None):
    position = entry_label.index(INSERT)
    entry_label.icursor(position - 1)

def shift_cursor2(event=None):
    position = entry_label.index(INSERT)
    entry_label.icursor(position + 1)

button1 = Button(app, text="Shift cursor left", command=shift_cursor1)
button1.grid(row=1, column=1, padx=10, pady=10)

button2 = Button(app, text="Shift cursor right", command=shift_cursor2)
button2.grid(row=1, column=0, padx=10, pady=10)

entry_label = Entry(app)
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry_label.focus()
app.mainloop()'''

#7.45
'''class SparseArray:
    def __init__(self, A):
        self._orig = A
        self._storage = {}
        for idx, elem in enumerate(A):
            if elem != None:
                self._storage[idx] = elem

    def __len__(self):
        return len(self._storage)

    def __getitem__(j):
        return self._storage[j]

    def __setitem__(j, e):
        self._storage[j] = e

sparse = [None] * 1000 + [1] + [None] * 1000 + [2]

new_sparse = SparseArray(sparse)
print(len(new_sparse))'''

#7.26
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while (iternode != None):
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return

MyStack = Stack()
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)
MyStack.display()

print("\nTop element is ", MyStack.peek())

MyStack.pop()
MyStack.pop()
MyStack.display()

print("\nTop element is ", MyStack.peek())'''