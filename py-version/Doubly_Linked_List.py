class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print(f'\nlength of the structure: {self.length}')

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while(temp.next):
            prev = temp
            temp = temp.next
        self.tail = prev
        temp.prev = None
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        self.length-=1
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index-1)
        temp = self.get(index)
        prev.next = new_node
        new_node.prev = prev
        new_node.next = temp
        temp.prev = new_node
        self.length += 1
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = self.get(index)
        prev.next = temp.next
        prev = temp.next
        prev.prev = temp.prev
        temp.prev = None
        temp.next = None
        self.length-= 1

    
    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after