class Empty(Exception):
    pass

'''Priority Queue:

P.add(k,v): insert item with key k and value v into priority queue Priority
P.min(): return tuple (k,v) where v is min overall
P.removeMin(): remove and return tuple (k,v) with minimum priority
P.isEmpty(): return True if P is empty, False otherwise

Heaps(best underlying structure for P queues):
--> complete binary tree (filled binary tree)
--> each internal node has value smaller than its children 

--> array implementation
methods:
--> _parent(j): parent of j
--> left(j): left child of j (2*j+1)
--> right(j): right child of j (2*j+2)
--> hasLeft(j): true if j has a left child 
--> hasRight(j):true if j has a right child
--> swap(i,j): swap i and j(during heapification)
--> upheap(j): heapify toward the root from j (private)
--> downheap(j): heapify from j to a leaf
--> len(H): number of elements in heap h
--> add(k, v): add key value pair into the heap h
--> min(): min element value in h
--> removeMin(): remove min key in H(i.e. the root of heap) 
and return corresponding values(using upheap or downheap)'''



'''Example2: implement a queue based  on a circular array 
(do i need to pointers)
Example1: implement a queue based a fixed size array and then 
give the choice to extend the size (also taking a second argument 
desired size)
Example3: implement a queue based in a stack(2 stacks)
Example4: implement a double ended queue (from both ends you can 
dequeue and enqueue)

--> D.addFirst(e): add element e to the fornt of dequeue
--> D.addLast(e): add element e to the end of dequeue
--> D.deleteFirst(): remove and return first element of deleteFirst
--> D.deleteLast(): remove and return last element of deleteFirst
--> rest of similar methods'''


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
        new_node = self._Node(element, None)
        if self.isEmpty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
