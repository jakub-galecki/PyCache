import unittest
from PyHashMap import Hash


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashMap = Hash(16)

    def test(self):
        self.assertTrue(self.hashMap.insert("case0", "some value 0"))
        self.assertTrue(self.hashMap.insert("case1", "some value 1"))
        self.assertTrue(self.hashMap.insert("case2", "some value 2"))
        self.assertEqual("some value 0", self.hashMap.get("case0"))
        self.assertEqual("some value 1", self.hashMap.get("case1"))
        self.assertEqual("some value 2", self.hashMap.get("case2"))
        self.assertTrue(self.hashMap.remove("case0"))
        self.assertTrue(self.hashMap.remove("case1"))
        self.assertTrue(self.hashMap.remove("case2"))
        self.assertFalse(self.hashMap.get("case0"))
        self.assertFalse(self.hashMap.get("case1"))
        self.assertFalse(self.hashMap.get("case2"))
