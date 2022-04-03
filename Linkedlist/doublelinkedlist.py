from xml.dom import NotFoundErr


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Doublelinkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('doublelist is empty')
            return
        itr = self.head
        lst = []
        while itr:
            lst.append(itr.val)
            itr = itr.next
        print(lst)

    def reveredPrint(self):
        if self.head is None:
            print('doublelinkedlist is empty')
            return
        itr = self.head
        lst = []
        while itr.next:
            itr = itr.next
        while itr:
            lst.append(itr.val)
            itr = itr.prev
        print(lst)

    def add_begin(self, e):
        node = Node(e)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def add_at_end(self, e):
        node = Node(e)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node.next = itr.next
        node.prev = itr
        itr.next = node

    def add_after(self, e, x):
        node = Node(e)
        if self.head is None:
            print('dlist is empty')
            return
        itr = self.head
        while itr:
            if itr.val == x:
                break
            itr = itr.next
        if itr is None:
            print('node is absent')
        else:
            node.next = itr.next
            node.prev = itr
            if itr.next:
                itr.next.prev = node
            itr.next = node


    def add_before(self, x, e):
        node = Node(e)
        if self.head is None:
            print('dlist is empty')
            return
        itr = self.head
        while itr:
            if itr.val == x:
                break
            itr = itr.next
        if itr is None:
            print('dlist is empty')
        else:
            node.prev = itr.prev
            node.next = itr
            if itr.prev:
                itr.prev.next = node
            else:
                self.head =node
            itr.prev = node

    def add_by_position(self, n, e):
        node = Node(e)
        if n == 0:
            self.head = node
            return
        itr = self.head
        count = 1
        while itr and count < n:
            itr = itr.next
            count +=1
        node.next = itr.next
        node.prev = itr
        if itr.next:
            itr.next.prev = node
        itr.next = node

    def remove_first(self):
        if self.head is None:
            print('dlist is empty')
            return
        self.head = self.head.next
        self.head.prev = None


    def remove_last(self):
        if self.head is None:
            print('dlist is empty')
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    
    def remove_by_value(self, x):
        if self.head is None:
            print('dlist is empty')
            return
        if self.head.next is None:
            if self.head.val == x:
                self.head = None
                return
        if self.head.val == x:
            self.head = self.head.next
            self.head.prev = None

        itr  = self.head
        while itr:
            if itr.val == x:
                break
            itr = itr.next
        if itr.next:
            itr.next.prev = itr.prev
            itr.prev.next = itr.next
        else:
            if itr.val == x:
                itr.prev.next = None
            else:
                print('node is absent')




dl = Doublelinkedlist()
# dl.add_begin(10)
dl.add_at_end(90)
dl.add_after(45, 90)
dl.add_before(90, 100)
dl.add_by_position(2, 200)
dl.remove_first()
dl.remove_last()
dl.print()
dl.reveredPrint()