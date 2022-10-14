import lab1
import unittest


class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

    def test_is_empty(self):
        q = lab1.Queue()
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(1)
        self.assertEqual(q.isEmpty(), False)

    def test_dequeue_empty(self):
        q = lab1.Queue()
        self.assertRaises(AttributeError, q.dequeue)

    def test_dequeue_once(self):
        q = lab1.Queue()
        q.enqueue(12)
        self.assertEqual(q.dequeue(), 12)

    def test_queue_series(self):
        q = lab1.Queue()
        q.enqueue(12)
        q.enqueue(34)
        q.enqueue(1)
        self.assertEqual(str(q), '[12, 34, 1]')
        self.assertEqual(q.dequeue(), 12)
        q.enqueue(32)
        self.assertEqual(str(q), '[34, 1, 32]')

    def test_print_empty(self):
        q = lab1.Queue()
        self.assertEqual(str(q), '[]')


class T1_TestingStack(unittest.TestCase):

    def test_print_empty(self):
        q = lab1.Stack()
        self.assertEqual(str(q), '[]')

    def test_is_empty(self):
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        s.pop()
        self.assertEqual(s.isEmpty(), True)
        print("\n")

    def test_pop_empty(self):
        s = lab1.Stack()
        print("Raise AttributeError on empty pop")
        self.assertRaises(AttributeError, s.pop)
        print('\n')

    def test_pop(self):
        s = lab1.Stack()
        s.push(10)
        print('pop returns the data')
        self.assertEqual(s.pop(), 10)

    def test_push_once(self):
        s = lab1.Stack()
        s.push(10)
        self.assertEqual(str(s), '[10]')

    def test_stack_series(self):
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(str(s), '[4, 3, 2, 1]')
        s.pop()
        s.pop()
        self.assertEqual(str(s), '[2, 1]')
        self.assertEqual(s.pop(), 2)


class T2_TestingPalindrome(unittest.TestCase):

    tests = {
        'Hello':        False,
        'ni t I n':     True,
        '&$(^^)$&':     False,
        'My gym':       True,
        '12TENET12':    False,
        '63488436':     True,
        '':             True
    }

    def test_basic_string(self):

        for test in self.tests:
            print("\n")
            string = test
            sol = self.tests[string]
            p = lab1.isPalindrome(string)
            print("The string being tested is -> ", string)
            self.assertEqual(p, sol)
            print('passed')
            print("\n")


class T3_TestingTwoStackQueue(unittest.TestCase):

    def test_print_empty(self):
        q = lab1.TwoStackQueue()
        self.assertEqual(str(q), '[]')

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.TwoStackQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

    def test_is_empty(self):
        q = lab1.TwoStackQueue()
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(1)
        self.assertEqual(q.isEmpty(), False)

    def test_dequeue_empty(self):
        q = lab1.TwoStackQueue()
        self.assertRaises(AttributeError, q.dequeue)

    def test_dequeue_once(self):
        q = lab1.TwoStackQueue()
        q.enqueue(12)
        self.assertEqual(q.dequeue(), 12)

    def test_queue_series(self):
        q = lab1.TwoStackQueue()
        q.enqueue(12)
        q.enqueue(34)
        q.enqueue(1)
        self.assertEqual(str(q), '[12, 34, 1]')
        self.assertEqual(q.dequeue(), 12)
        q.enqueue(32)
        self.assertEqual(str(q), '[34, 1, 32]')


class T4_TestingPalindromeEC(unittest.TestCase):

    tests = {
        'Hello':        False,
        'ni t I n':     True,
        '&$(^^)$&':     False,
        'My gym':       True,
        '12TENET12':    False,
        '63488436':     True,
        '':             True
    }

    def test_basic_string(self):

        for test in self.tests:
            print("\n")
            string = test
            sol = self.tests[string]
            p = lab1.isPalindromeEC(string)
            print("The string being tested is -> ", string)
            self.assertEqual(p, sol)
            print('passed')
            print("\n")


if __name__ == '__main__':
    unittest.main()
