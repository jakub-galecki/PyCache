import unittest
from DoublyLinkedList import DLList


class DLLTest(unittest.TestCase):
    def test_traverse(self):
        dll = DLList()
        dll.push_front(0,1)
        dll.push_back(0,2)
        dll.push_back(0,3)
        dll.push_back(0,4)
        dll.push_back(0,5)
        self.assertEqual([1, 2, 3, 4, 5], dll.traverse())

    def test_push(self):
        dll = DLList()
        self.assertIsNotNone(dll.push_front(0,1))
        self.assertIsNotNone(dll.push_back(0,2))
        self.assertIsNotNone(dll.push_back(0,3))
        self.assertIsNotNone(dll.push_back(0,4))
        self.assertIsNotNone(dll.push_back(0,5))
        self.assertEqual([1, 2, 3, 4, 5], dll.traverse())


    def test_pop(self):
        dll = DLList()
        dll.push_front(0,1)
        dll.push_back(0,2)
        tmp = dll.push_back(0,3)
        dll.push_back(0,4)
        dll.push_back(0,5)
        self.assertEqual([1, 2, 3, 4, 5], dll.traverse())
        self.assertEqual(1, dll.pop_front().value)
        self.assertIsNone(dll.pop_node(tmp))
        self.assertEqual(5, dll.pop_back().value)
        self.assertEqual([2, 4], dll.traverse())

