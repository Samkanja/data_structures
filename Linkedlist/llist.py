class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    
    def print(self):
        if self.head is None:
            print('llist is  empty')
            return
        lst = []
        itr = self.head
        while itr:
            lst.append(itr.val)
            itr = itr.next
        print(lst)

    
    def add_begin(self, e):
        node = Node(e)
        node.next = self.head
        self.head = node

    def add_at_end(self,e):
        node = Node(e)
        if self.head is None:
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node

    def add_after(self, x, e):
        node = Node(e)
        if self.head is None:
            print('llist is empty')
            return
        itr = self.head
        while itr.next:
            if itr.val == x:
                break
            itr = itr.next
        if itr is None:
            print('itr is absent')
        else:
            node.next = itr.next
            itr.next = node
        
    def add_before(self, x, e):
        node = Node(e)
        if self.head is None:
            print('llist is empty')
            return
        if self.head.val == x:
            node.next = self.head
            self.head = node
            return
        itr = self.head
        while itr.next:
            if itr.next.val == x:
                break
            itr = itr.next
        if itr is None:
            print('llist is empty')
        else:
            node.next = itr.next
            itr.next = node

    def add_by_position(self,e, n):
        node = Node(e)
        if n == 0:
            node.next = self.head
            self.head = node
            return
        itr = self.head
        count = 1
        while itr.next and count < n:
            itr = itr.next
            count +=1
        node.next = itr.next
        itr.next = node


    def remove_first(self):
        if self.head is None:
            print('llist is empty')
            return
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            print('llist is empty')
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next  = None

    def remove_by_value(self, x):
        if self.head is None:
            print('llist is empty')
            return
       
        if self.head.val == x:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.val == x:
                break
            itr = itr.next
        if itr.next is None:
            print('node.is absent')
        else:
            itr.next = itr.next.next

    def remove_by_position(self, n):
        if n == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 1
        while itr.next and count < n:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

ll = Linkedlist()
ll.add_begin(45)
# ll.add_begin(100)
# ll.add_at_end(10)
# ll.add_at_end(50)
# ll.add_after(45, 24)
# ll.add_before(24, 100)
# ll.add_by_position(30, 0)
# ll.remove_first()
# ll.remove_by_value(100)
# ll.remove_by_position(0)
ll.remove_by_value(45)
ll.print()