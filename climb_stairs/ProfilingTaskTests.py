import unittest
from Profiling import ProfilingTask


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.var = ProfilingTask()

    def test_climb_stairs(self):
        self.assertEqual(self.var.climb_stairs(-2), 0)
        self.assertEqual(self.var.climb_stairs(2), 2)
        self.assertEqual(self.var.climb_stairs(5), 8)
        self.assertEqual(self.var.climb_stairs(10), 89)

    def test_climb_stairs_cache(self):
        self.assertEqual(self.var.climb_stairs_cache(-2), 0)
        self.assertEqual(self.var.climb_stairs_cache(2), 2)
        self.assertEqual(self.var.climb_stairs_cache(5), 8)
        self.assertEqual(self.var.climb_stairs_cache(10), 89)
        self.assertEqual(self.var.climb_stairs_cache(45), 1836311903)


if __name__ == '__main__':
    unittest.main()
