import unittest
from DoublyLinkedList import DLList


class DLLTest(unittest.TestCase):
    def test_traverse(self):
        dll = DLList()
        dll.push_front(1)
        dll.push_back(2)
        dll.push_back(3)
        dll.push_back(4)
        dll.push_back(5)
        self.assertEqual([1, 2, 3, 4, 5], dll.traverse())

    def test_push(self):
        dll = DLList()
        self.assertIsNotNone(dll.push_front(1))
        self.assertIsNotNone(dll.push_back(2))
        self.assertIsNotNone(dll.push_back(3))
        self.assertIsNotNone(dll.push_back(4))
        self.assertIsNotNone(dll.push_back(5))
        self.assertEqual([1, 2, 3, 4, 5], dll.traverse())


    def test_pop(self):
        dll = DLList()
        dll.push_front(1)
        dll.push_back(2)
        tmp = dll.push_back(3)
        dll.push_back(4)
        dll.push_back(5)
        self.assertEqual([1, 2, 3, 4, 5], dll.traverse())
        self.assertEqual(1, dll.pop_front())
        self.assertIsNone(dll.pop_node(tmp))
        self.assertEqual(5, dll.pop_back())
        self.assertEqual([2, 4], dll.traverse())

