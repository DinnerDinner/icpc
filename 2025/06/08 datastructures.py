
#Array, in an array, all elements are stored contiguously so when you pop(0), it has to shift all the other elements/
#to maintain the indexes, and as the slots are numbered(indexs), its faster at searching through
print("\nlist/array")

lst = [1,2,3,4]
lst.append(5)
print(lst)
print(lst.pop())



#Stack (LIFO)
print("\nstack")

stack = []
stack.append(5)
stack.append(10)
print(stack)
print(stack.pop())


def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

print(is_balanced("(()())"))  # YES
print(is_balanced("(())"))   # NO





# Queue (FIFO), in here, there are no slots, it just removes elements and leaves the rest where it is, there are no indexes, hence it has to
#count when you are trying to access a certain value's position in the queue taking o(n), but the popleft or appendleft only take o(1)
from collections import deque
print("\nqueue")
que = deque()
que.append(-1)
que.append(0)
que+=[1,2,3,4]
print(que.popleft())
print(list(que))

from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueues:", list(queue))  # ['A', 'B', 'C']

first = queue.popleft()
print("Dequeued element:", first)             # 'A'
print("Queue after dequeue:", list(queue))    # ['B', 'C']

# Peek at the front element without removing
front = queue[0]
print("Front element:", front)                 # 'B'


#Arrays (list) are great at jumping (indexing) but bad at shuffling (popping front). Linked structures (deque) are bad at jumping but great at sliding.

#Linked list short short
## A chain of boxes. Each box holds: A piece of data (like a number), A link to the next box. Elements are not side by side in memory
# singly linked list view:  [10] → [20] → [30] → None


#----------------

# Hash Table - **LITERALLY JUST A Python Dictionary! It's just the technical term for it.
'''
    it gets hashed into a long number, you % it by its length, and take the resulting index as its position in a hidden array, 
    in that array, the element at that index is a tuple with (key, value) formatting, and from there whenever you call the key, 

    it finds its hash, does the %, takes the resulting remainder as index, and searches the list for said number in the hidden array, 
    and returns the second value from the tuple (the value part), hence in a list since finding the element at certain index is o(1), 
    hash tables look-ups have a time complexity of o(1)
'''


#exemple; Prompt: Return the first character that appears only once in the string. If none exist, return '_'.
def first(lst):
    dct = {}

    for i in lst:
        dct[i] = dct.get(i, 0) + 1

    for key in dct:
        if dct[key] == 1:
            return key
    return "_"

print(first("leetcode"))
print(first("aabbccc"))




# Heaps: special binary tree-based data structure