class Empty(Exception):
    pass




class QueueList:
    '''FIFO queue implementation with a Python list as the underlying infrastructure'''

    def __init__(self):
        '''create an empty queue'''
        self.data = []
        self._size = 0
        self._front = 0
    
    def __len__(self):
        '''return number of elements in queue'''
        return self._size
    def isEmpty(self):
        return self._size
    
    def first(self):
        '''return (but not remove) element at the front of queue'''
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''remove and return the first element in queue'''
        if self.isEmpty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # to help garbage collection (none elements get removed after sometime)
        self._front += 1
        self._size -= 1
        return answer
    
    def enqueue(self, elem):
        self._data.append(elem)
        self._size += 1

    









class LinkedQueue:
    '''Fifo queue implementation using a sll'''

    #---------> nest Node class------------
    class _Node:
        '''lightweight non-public class for storing sll'''
        __slots__ = '_element', '_next' #class attributes

        def __init__(self,element, next):
            '''create a Node'''
            self._element = element
            self._next = next
    #--------------------------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def first(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        
        return self._head._element
    
    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty(): # removed head had been tail
            self._tail = None
        return answer
    
    def enqueue(self):
        new_node = self._Node(elem, None)
        if self.isEmpty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
