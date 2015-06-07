import unittest


class HelloWorld(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 2)

    def test_two(self):
        self.assertEqual(1, 1)
