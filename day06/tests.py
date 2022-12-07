import unittest
import solve

class Day06TestMethods(unittest.TestCase):
  def setUp(self):
    pass

  def test_all_same(self):
    test_cases = [
      [False, []],
      [True, [111]],
      [True, [1,1,1,1]],
      [False, [1,2,3,4]],
      [True, ['a','a','a','a']],
      [False, ['z', 'd', 'z', 'z']],
    ]
    for [expected, arr] in test_cases:
      self.assertEqual(solve.all_same(arr), expected, 'expected %s to be %s' % (arr, expected))

  def test_all_different(self):
    test_cases = [
      [True, []],
      [True, [111]],
      [False, [1,2,3,1]],
      [False, [1,1,1,1]],
      [True, [1,2,3,4]],
      [False, ['a','a','a','a']],
      [False, ['p', 'q', 'f', 'f']],
      [False, ['z', 'd', 'z', 'z']],
      [True, ['a', 'z', 'd', 'f']]
    ]
    for [expected, arr] in test_cases:
      self.assertEqual(solve.all_different(arr), expected, 'expected %s to be %s' % (arr, expected))
  
if __name__ == '__main__':
  unittest.main()