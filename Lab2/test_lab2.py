import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):

    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5, 4, 2, 1, 3])
        print("\n")


class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")


class T9_pqueue_series_of_operations(unittest.TestCase):
    
    def test_series_of_operations(self):
        queue = pqueue.pqueue(size=7)
        queue.insert(14)
        queue.insert(33)
        queue.insert(42)
        queue.insert(44)
        queue.insert(35)
        queue.insert(16)
        self.assertEqual(queue.get_pqueue(), [44,42,33,14,35,16])
        queue.extract_max()
        self.assertEqual(queue.get_pqueue(), [42,35,33,14,16])
        queue.extract_max()
        self.assertEqual(queue.get_pqueue(), [35,15,33,14])
        queue.insert(12)
        queue.insert(100)
        self.assertEqual(queue.get_pqueue(), [100,16,35,14,12,33])


class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10, 24, 3, 57, 4, 67, 37, 87, 7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")


class T6_heap_build_heap(unittest.TestCase):

    def test_heap_build_standard(self):
        heap = mheap.max_heap(data=[35, 33, 42, 10, 14, 19, 27, 44, 26, 31])
        heap.build_heap()
        self.assertEqual(heap.get_heap(), [
                         44, 42, 35, 33, 31, 19, 27, 10, 26, 14])

    def test_heap_build_empty(self):
        heap = mheap.max_heap(data=[])
        heap.build_heap()
        self.assertEqual(heap.get_heap(), [])

    def test_heap_build_one(self):
        heap = mheap.max_heap(data=[1])
        heap.build_heap()
        self.assertEqual(heap.get_heap(), [1])


class T7_heap_insert(unittest.TestCase):

    def test_insert_smallest(self):
        heap = mheap.max_heap(data=[44, 35, 42, 33, 14, 19, 27])
        heap.heap = [*heap.heap, None]
        heap.max_size += 1
        heap.insert(10)
        self.assertEqual(heap.get_heap(), [44, 35, 42, 33, 14, 19, 27, 10])

    def test_insert_largest(self):
        heap = mheap.max_heap(data=[44, 35, 42, 33, 14, 19, 27])
        heap.heap = [*heap.heap, None]
        heap.max_size += 1
        heap.insert(100)
        self.assertEqual(heap.get_heap(), [
                         100, 44, 42, 35, 14, 19, 27, 33])

    def test_insert_middle(self):
        heap = mheap.max_heap(data=[44, 35, 42, 33, 14, 19, 27, 10])
        heap.heap = [*heap.heap, None]
        heap.max_size += 1
        heap.insert(37)
        self.assertEqual(heap.get_heap(), [44,37,42,35,14,19,27,10,33])

    def test_insert_empty(self):
        heap = mheap.max_heap(size=20)
        heap.insert(100)
        self.assertEqual(heap.get_heap(), [100]+([None]*19))

    def test_insert_full(self):
        heap = mheap.max_heap(data=[44, 35, 42, 33, 14, 19, 27, 10])
        with self.assertRaises(IndexError):
            heap.insert('4')


class T8_heap_extract_max(unittest.TestCase):

    aheap = mheap.max_heap(data=[44, 35, 42, 33, 14, 19, 27, 10])

    def test_extract_max_once(self):
        self.aheap.extract_max()
        self.assertEqual(self.aheap.get_heap(), [42,35,27,33,14,19,10])

    def test_extract_max_twice(self):
        self.aheap.extract_max()
        self.aheap.extract_max()
        self.assertEqual(self.aheap.get_heap(), [33,19,27,10,14])

    def test_extract_max_empty(self):
        heap = mheap.max_heap(data=[])
        with self.assertRaises(KeyError):
            heap.extract_max()


if __name__ == '__main__':
    unittest.main()
