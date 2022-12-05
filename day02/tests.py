import unittest
import solve

class Day02TestMethods(unittest.TestCase):
  def setUp(self):
    pass

  def test_get_score(self):
    get_score_input = [
      [ solve.ROCK_INPUT, solve.ROCK_OUTPUT, solve.TIE_SCORE + solve.ROCK_SCORE ],
      [ solve.ROCK_INPUT, solve.PAPER_OUTPUT, solve.WIN_SCORE + solve.PAPER_SCORE ],
      [ solve.ROCK_INPUT, solve.SCISSORS_OUTPUT, solve.LOSS_SCORE + solve.SCISSORS_SCORE ],
      [ solve.PAPER_INPUT, solve.ROCK_OUTPUT, solve.LOSS_SCORE + solve.ROCK_SCORE ],
      [ solve.PAPER_INPUT, solve.PAPER_OUTPUT, solve.TIE_SCORE + solve.PAPER_SCORE],
      [ solve.PAPER_INPUT, solve.SCISSORS_OUTPUT, solve.WIN_SCORE + solve.SCISSORS_SCORE ],
      [ solve.SCISSORS_INPUT, solve.ROCK_OUTPUT, solve.WIN_SCORE + solve.ROCK_SCORE],
      [ solve.SCISSORS_INPUT, solve.PAPER_OUTPUT, solve.LOSS_SCORE + solve.PAPER_SCORE ],
      [ solve.SCISSORS_INPUT, solve.SCISSORS_OUTPUT, solve.TIE_SCORE + solve.SCISSORS_SCORE],
    ];

    for case in get_score_input:
      [theirs, mine, expectedScore] = case
      self.assertEqual(solve.get_score(theirs, mine), expectedScore, '%s vs %s should get %d points' % (theirs, mine, expectedScore))

  def test_get_score_beta(self):
    get_score_input = [
      [ solve.ROCK_INPUT, solve.TIE_OUTCOME, solve.TIE_SCORE + solve.ROCK_SCORE ],
      [ solve.ROCK_INPUT, solve.LOSS_OUTCOME, solve.LOSS_SCORE + solve.SCISSORS_SCORE ],
      [ solve.ROCK_INPUT, solve.WIN_OUTCOME, solve.WIN_SCORE + solve.PAPER_SCORE ],
      [ solve.PAPER_INPUT, solve.TIE_OUTCOME, solve.TIE_SCORE + solve.PAPER_SCORE],
      [ solve.PAPER_INPUT, solve.LOSS_OUTCOME, solve.LOSS_SCORE + solve.ROCK_SCORE ],
      [ solve.PAPER_INPUT, solve.WIN_OUTCOME, solve.WIN_SCORE + solve.SCISSORS_SCORE ],
      [ solve.SCISSORS_INPUT, solve.TIE_OUTCOME, solve.TIE_SCORE + solve.SCISSORS_SCORE ],
      [ solve.SCISSORS_INPUT, solve.LOSS_OUTCOME, solve.LOSS_SCORE + solve.PAPER_SCORE],
      [ solve.SCISSORS_INPUT, solve.WIN_OUTCOME, solve.WIN_SCORE + solve.ROCK_SCORE],
    ];

    for case in get_score_input:
      [theirs, outcome, expectedScore] = case
      self.assertEqual(solve.get_score_beta(theirs, outcome), expectedScore, '%s and %s should get %d points' % (theirs, outcome, expectedScore))
  
if __name__ == '__main__':
  unittest.main()