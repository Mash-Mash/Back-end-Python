import unittest
from LRUCache import LRUCache


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cache = LRUCache(4)

    def test_set_get(self):
        self.cache.set('Jesse', 'James')
        self.assertTrue(self.cache.get('Jesse'), 'James')

    def test_delete(self):
        self.cache.set('Jesse', 'James')
        self.cache.get('Jesse')
        self.cache.delete('Walter')

    def test_out_of_memory(self):
        self.cache.set('Jesse', 'James')
        self.cache.set('Jim', 'Richard')
        self.cache.set('Smith', 'Alex')
        self.cache.set('Walter', 'White')

        self.cache.set('Jesse', 'John')  # ('Jesse', 'John') will be moved to the end of the list

        self.cache.set('Williams', 'Jack')  # ('Jim', 'Richard') will be deleted

        self.assertEqual(self.cache.get('Jim'), None)
        self.assertEqual(self.cache.get('Smith'), 'Alex')

        self.cache.set('Jim', 'Richard')  # ('Walter', 'White') will be deleted

        self.assertEqual(self.cache.get('Walter'), None)


if __name__ == '__main__':
    unittest.main()
