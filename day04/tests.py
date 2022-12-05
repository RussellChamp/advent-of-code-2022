import unittest
import solve

class Day04TestMethods(unittest.TestCase):
  def setUp(self):
    pass

  def test_fully_contains(self):
    test_cases = [
      [True, 1,2,1,2],
      [True, 1,100,5,50],
      [True, 5,50,1,100],
      [False, 1,2,3,4],
      [False, 1,100,50,500],
      [False, 2,4,6,8],
      [False, 2,3,4,5],
      [False, 5,7,7,9],
      [True, 2,8,3,7],
      [True, 6,6,4,6],
      [False, 2,6,4,8]
    ]
    for [expected, a, b, c, d] in test_cases:
      self.assertEqual(solve.fully_contains(a, b, c, d), expected)

  def test_any_overlap(self):
    test_cases = [
      [False, 2,4,6,8],
      [False, 2,3,4,5],
      [True, 5,7,7,9],
      [True, 2,8,3,7],
      [True, 6,6,4,6],
      [True, 2,6,4,8]
    ]
    for [expected, a, b, c, d] in test_cases:
      self.assertEqual(solve.any_overlap(a, b, c, d), expected, 'overlap of %d-%d and %d-%d should be %s' % (a, b, c, d, expected))
  
if __name__ == '__main__':
  unittest.main()