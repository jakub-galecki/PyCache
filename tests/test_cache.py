import unittest
from PyCache import Cache

class CacheTest(unittest.TestCase):

    def test_cache_hit(self):
        cache = Cache(5)
        cache.put("somekey", "somevalue")
        cache.put("somekey2", "somevalue2")
        cache.put("somekey3", "somevalue3")
        cache.put("somekey4", "somevalue4")
        self.assertEqual("somevalue", cache.get("somekey"))
        self.assertEqual("somevalue2", cache.get("somekey2"))
        self.assertEqual("somevalue3", cache.get("somekey3"))
        self.assertEqual("somevalue4", cache.get("somekey4"))

    def test_cache_miss(self):
        cache = Cache(5)
        cache.put("somekey", "somevalue")
        cache.put("somekey2", "somevalue2")
        cache.put("somekey3", "somevalue3")
        cache.put("somekey4", "somevalue4")
        self.assertEqual(-1, cache.get("somevalue"))
        self.assertEqual(-1, cache.get("somevalue21321"))
        self.assertEqual(-1, cache.get("somadwadaevalue"))
        
    def test_cache_LRU(self):
        cache = Cache(5)
        cache.put("somekey", "somevalue")
        cache.put("somekey2", "somevalue2")
        cache.put("somekey3", "somevalue3")
        cache.put("somekey4", "somevalue4")
        self.assertEqual("somevalue", cache.get("somekey")) 
        self.assertEqual("somevalue4", cache.get("somekey4")) 
        cache.put("somekey4", "somevalue5")
        self.assertEqual("somevalue5", cache.get("somekey4")) 
        cache.put("somekey4", "somevalue6")
        self.assertEqual("somevalue6", cache.get("somekey4")) 
        cache.put("somekey5", "somevalue7")
        self.assertEqual("somevalue7", cache.get("somekey5")) 
        cache.put("somekey6", "somevalue8")
        self.assertEqual("somevalue8", cache.get("somekey6")) 