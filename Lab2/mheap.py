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
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap

        pass

    def __heapify(self, curr_index, list_length=None):
        """Sift down the node at curr_index until the heap property is satisfised"""
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        pass

    def build_heap(self):
        """Build a max heap from the stored list"""
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        pass

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
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
