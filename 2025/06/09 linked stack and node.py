'''Singly linked list:

Doubly Linked Lists:

--> Need a nested Node class 
--> constructor: set elem, 

Example: implement a deque using a doubly linked list


'''


class Empty(Exception):
    pass





class StackLinkedList:
    
    #---------> nest Node class------------
    class _Node:
        '''lightweight non-public class for storing sll'''
        __slots__ = '_element', '_next' #class attributes

        def __init__(self,element, next):
            '''create a Node'''
            self._element = element
            self._next = next
    #--------------------------------------

    def push(self, elem):
        self._head = self._Node(elem, self._head)
        self._size += 1

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        








class DLL:
    class _Node:
        __slots__ = '_element', '_prev', '_next' #size fixed

        def __init__(self, elem, prev, next):
            self._element = elem
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        pass

    def isEmpty(self):
        pass
    def insertBetween(self, elem, predecessor, successor):
        pass
    def deleteNode(self, node):
        pass