"""
lab1.py
Solutiion for lab1 CS313 - 
    - implements stack and queue using singly linked list
    - Extra credit TwoStackQueue implemented
    - Data structures used for palindrome checking fuction
Author: Vincent Lanier
"""


class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Initializes a Node containing the given data and 
        pointing to the given Node

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node


class Queue(object):
    """
    Initializes a standard FIFO Queue
    
    ...

    Attributes
    ------
    ask question??
    
    Methods
    -----
    enqueue(newData : int or float):
        add a node containing newData to the end of the queue
    dequeue():
        removes the front node from the queue and returns the stored data
    isEmpty():
        returns True of the queue is empty, otherwise returns False 
    """
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        pass

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        pass

    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        pass

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        pass


class Stack(object):
    """
    Initializes a standard LIFO Stack
    
    ...

    Attributes
    ------
    top : object of class Node
        pointer to the node at the top of the stack
    
    Methods
    -----
    push(newData : int or float):
        push a node containing newData onto the stack
    pop():
        remove the top node from the stack and return the stored data
    isEmpty():
        returns True of the stack is empty, otherwise returns False 
    """

    def __init__(self):
        '''Initializes an empty stack'''
        self.head = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        curr_node = self.head
        string_rep = str()        
        while curr_node:
            string_rep += f' {curr_node.getData()}'
            curr_node = curr_node.getNext()
        return string_rep

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        newNode = Node(newData, self.head)
        self.head = newNode

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        
        head_node = self.head
        self.head = head_node.getNext()
        return head_node.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        pass


def isPalindrome(s):
    '''Returns True if string s is a palidrome, otherwise returns False'''
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value
    return


def isPalindromeEC(s):
    '''Returns True if string s is a palindrome, otherwise returns False'''

    # Return appropriate value
    return
