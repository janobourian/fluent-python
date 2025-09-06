import unittest
from test_assesments.lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    
    def test_get_empty_cache(self):
        lru = LRUCache(5)
        self.assertEqual(lru.get(1), -1)
    
    def test_put_and_get(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
    
    def test_capacity_eviction(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(3, 3)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)
    
    def test_update_existing_key(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(1, 10)
        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(2), 2)
    
    def test_access_order(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.get(1)
        lru.put(3, 3)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)

    def test_eviction_order(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(3, 3)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)
    
    def test_key_as_string(self):
        lru = LRUCache(2)
        lru.put("one", 1)
        lru.put("two", 2)
        self.assertEqual(lru.get("one"), 1)
        self.assertEqual(lru.get("two"), 2)
        lru.put("three", 3)
        self.assertEqual(lru.get("one"), -1)
        self.assertEqual(lru.get("two"), 2)
        self.assertEqual(lru.get("three"), 3)

if __name__ == '__main__':
    unittest.main()