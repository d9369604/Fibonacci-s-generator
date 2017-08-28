import unittest
from fibonacci import fib


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        c = fib()
        result = [next(c) for _ in range(10)]
        expect = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertListEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
