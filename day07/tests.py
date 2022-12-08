import unittest

class Day07TestMethods(unittest.TestCase):
  def setUp(self):
    pass

  # Does a thing
  def test_true(self):
    self.assertEqual(True, False)
  
if __name__ == '__main__':
  unittest.main()