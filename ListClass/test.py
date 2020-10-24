import unittest
from ListClass import ListClass


class ListClassTests(unittest.TestCase):
    def setUp(self):
        self.a = ListClass()
        self.b = ListClass([1, 2, 3, 4])
        self.c = ListClass([10])
        self.d = ListClass([1, 8])
        self.e = [1, 2, 3, 0]

    def test_add(self):
        self.assertEqual(tuple(self.a + self.b), (1, 2, 3, 4))
        self.assertEqual(tuple(self.a + self.b), (1, 2, 3, 4))
        self.assertEqual(tuple(self.b + self.c), (11, 2, 3, 4))
        self.assertEqual(tuple(self.d + self.e), (2, 10, 3, 0))

    def test_sub(self):
        self.assertEqual(tuple(self.a - self.b), (-1, -2, -3, -4))
        self.assertEqual(tuple(self.b - self.c), (-9, 2, 3, 4))
        self.assertEqual(tuple(self.d - self.e), (0, 6, -3, 0))

    def test_lt(self):
        self.assertTrue(self.a < self.b)
        self.assertFalse(self.b < self.a)

        self.assertFalse(self.b < self.c)
        self.assertFalse(self.c < self.b)

        self.assertFalse(self.c < self.d)
        self.assertTrue(self.d < self.c)

        self.assertFalse(self.b < self.d)
        self.assertTrue(self.d < self.b)

        self.assertTrue(self.a < self.d)
        self.assertFalse(self.d < self.a)

        self.assertTrue(self.e < self.d)
        self.assertFalse(self.d < self.e)

    def test_eq(self):
        self.assertFalse(self.a == self.b)
        self.assertTrue(self.b == self.c)
        self.assertFalse(self.c == self.d)
        self.assertFalse(self.a == self.d)
        self.assertFalse(self.d == self.e)

    def test_ne(self):
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.b != self.c)
        self.assertTrue(self.c != self.d)
        self.assertTrue(self.a != self.d)
        self.assertTrue(self.d != self.e)

    def test_le(self):
        self.assertTrue(self.a <= self.b)
        self.assertFalse(self.b <= self.a)

        self.assertTrue(self.b <= self.c)
        self.assertTrue(self.c <= self.b)

        self.assertFalse(self.c <= self.d)
        self.assertTrue(self.d <= self.c)

        self.assertFalse(self.b <= self.d)
        self.assertTrue(self.d <= self.b)

        self.assertTrue(self.a <= self.d)
        self.assertFalse(self.d <= self.a)

        self.assertTrue(self.e <= self.d)
        self.assertFalse(self.d <= self.e)

    def test_gt(self):
        self.assertFalse(self.a > self.b)
        self.assertTrue(self.b > self.a)

        self.assertFalse(self.b > self.c)
        self.assertFalse(self.c > self.b)

        self.assertTrue(self.c > self.d)
        self.assertFalse(self.d > self.c)

        self.assertTrue(self.b > self.d)
        self.assertFalse(self.d > self.b)

        self.assertFalse(self.a > self.d)
        self.assertTrue(self.d > self.a)

        self.assertFalse(self.e > self.d)
        self.assertTrue(self.d > self.e)

    def test_ge(self):
        self.assertFalse(self.a >= self.b)
        self.assertTrue(self.b >= self.a)

        self.assertTrue(self.b >= self.c)
        self.assertTrue(self.c >= self.b)

        self.assertTrue(self.c >= self.d)
        self.assertFalse(self.d >= self.c)

        self.assertTrue(self.b >= self.d)
        self.assertFalse(self.d >= self.b)

        self.assertFalse(self.a >= self.d)
        self.assertTrue(self.d >= self.a)

        self.assertFalse(self.e >= self.d)
        self.assertTrue(self.d >= self.e)


if __name__ == '__main__':
    unittest.main()
