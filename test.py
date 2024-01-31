import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(None), "Hello, world!")

if __name__ == '__main__':
    unittest.main()