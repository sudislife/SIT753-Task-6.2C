import unittest
import say_hello

class MyTestCase(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello.say_hello(), 'Hello World!')

if __name__ == '__main__':
    unittest.main()