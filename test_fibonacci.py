import unittest
from fibonacci import *

class TestValid(unittest.TestCase):
  def test_fibonacci(self):
    self.assertEqual(fibonacci(1), 0)
    self.assertEqual(fibonacci(3), 1)
    self.assertEqual(fibonacci(4), 5) # fail, == 2
    self.assertEqual(fibonacci(10), 34)

def test_answer():
    assert fibonacci(3) == 1
    assert fibonacci(4) == 5 # fail, == 2

if(__name__ == '__main__'):
  unittest.main(verbosity=2)