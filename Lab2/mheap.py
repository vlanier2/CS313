"""
mheap.py
    Implements a binary max-heap for use in a priority queue implementation.
    Author: Vincent Lanier
    Class: CIS 313
"""

class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. The underlying 
    implementation uses a Python list instead. When initialized, 
    max_heap creates a new list of fixed size or uses an existing list.

    Attributes
    -----
    max_size    : int
    length      : int
    heap        : list

    Methods
    -----
    get_heap()
        returns the array storing the heap

    insert(data)
        Inserts the data in the heap. Maintains heap property.

    peek()
        Returns, but does not remove, the maximum value in the heap.

    extract_max()
        Returns and removes the maximum value in the heap.

    build_heap()
        builds a heap from the underlying array.
    """

    def __init__(self, size=20, data=None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size

    def get_heap(self):
        """Return the array storing the heap."""
        return self.heap

    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you
        #      : reach the root
        if self.length == self.max_size:
            raise IndexError('The heap is full')
        
        curr_index = self.length
        self.heap[curr_index] = data
        self.length += 1
        
        while self.heap[curr_index] > self.heap[self.__get_parent(curr_index)]:
            parent_index = self.__get_parent(curr_index)
            if parent_index < 0: return
            self.__swap(curr_index, parent_index)
            curr_index = parent_index

    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]
        
    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""

        if self.length == 0:
            raise KeyError('Heap is Empty')

        self.__swap(0, self.length-1)
        max_element = self.heap[self.length-1]
        self.heap[self.length-1] = None
        self.length -= 1
        self.__heapify(0)
        return max_element

    def __heapify(self, curr_index, list_length=None):
        """Sift down at curr_index until the heap property is satisfised"""
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)

        if left < self.length and right < self.length:
            largest = max(left, right, curr_index, key=lambda x : self.heap[x])
        elif left < self.length:
            largest = left if self.heap[left] > self.heap[curr_index] else curr_index
        elif right < self.length:
            largest = right if self.heap[right] > self.heap[curr_index] else curr_index
        else: # reached a leaf - heap property maintained
            return

        if largest == curr_index: # heap property maintained
            return

        self.__swap(curr_index, largest)
        self.__heapify(largest)

    def build_heap(self):
        """Build a max heap from the stored list"""
        for i in range((self.length-1) // 2, -1, -1):
            self.__heapify(i)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """Returns the given list in ascending order."""
    new_list = [None] * len(l)
    heap = max_heap(data=l)
    heap.build_heap()
    for i in range(len(l)-1, -1, -1):
        new_list[i] = heap.extract_max()
    return new_list