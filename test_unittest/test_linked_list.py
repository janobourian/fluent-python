import unittest
from linked_list.overview import DoublyLinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list = DoublyLinkedList()
    
    def test_append(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(list(self.list), [10, 20])
    
    def test_append_left(self):
        self.list.append_left(10)
        self.list.append_left(20)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(list(self.list), [20, 10])
    
    def test_mix_operations(self):
        self.list.append(10)
        self.list.append_left(20)
        self.list.append(30)
        self.assertEqual(len(self.list), 3)
        self.assertEqual(list(self.list), [20, 10, 30])
    
    def tearDown(self):
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()