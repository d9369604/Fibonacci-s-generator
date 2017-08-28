import unittest
from fibonacci import fib


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.c = fib()
        self.expect = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    def test_fibonacci(self):
        result = [next(self.c) for _ in range(10)]
        self.assertListEqual(self.expect, result)

    def test_fibonacci2(self):
        for i in range(10):
            self.assertEqual(self.expect[i], next(self.c))


if __name__ == '__main__':
    unittest.main()
