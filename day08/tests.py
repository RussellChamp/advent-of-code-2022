import unittest
import solve

class Day08TestMethods(unittest.TestCase):
  def setUp(self):
    pass

  def test_score_row(self):
    test_cases = [
      [1, 5, [3]],
      [1, 5, [5,2]],
      [2, 5, [1,2]],
      [2, 5, [3,5,3]],
      [2, 5, [3,3]]
    ]
    for [expected, height, row] in test_cases:
      self.assertEqual(solve.score_row(height, row), expected)
  
if __name__ == '__main__':
  unittest.main()