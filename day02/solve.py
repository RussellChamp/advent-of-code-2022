# Day 02: Rock Paper Scissors

import os

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

ROCK_INPUT = 'A'
PAPER_INPUT = 'B'
SCISSORS_INPUT = 'C'
ROCK_OUTPUT = 'X'
PAPER_OUTPUT = 'Y'
SCISSORS_OUTPUT = 'Z'
ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
scoreDict = { ROCK_OUTPUT: ROCK_SCORE, PAPER_OUTPUT: PAPER_SCORE, SCISSORS_OUTPUT: SCISSORS_SCORE }
LOSS_SCORE = 0
TIE_SCORE = 3
WIN_SCORE = 6

# calculate a score based on their choice and my choice
def get_score(theirs, mine):
  if [theirs, mine] == [ROCK_INPUT, ROCK_OUTPUT] \
    or [theirs, mine] == [PAPER_INPUT, PAPER_OUTPUT] \
    or [theirs, mine] == [SCISSORS_INPUT, SCISSORS_OUTPUT]: # Tie
    return TIE_SCORE + scoreDict[mine]
  elif [theirs, mine] == [ROCK_INPUT, PAPER_OUTPUT] \
    or [theirs, mine] == [PAPER_INPUT, SCISSORS_OUTPUT] \
    or [theirs, mine] == [SCISSORS_INPUT, ROCK_OUTPUT]: # Win
    return WIN_SCORE + scoreDict[mine]
  else: # Loss
    return LOSS_SCORE + scoreDict[mine]

LOSS_OUTCOME = 'X'
TIE_OUTCOME = 'Y'
WIN_OUTCOME = 'Z'
outcomeDict = { LOSS_OUTCOME: LOSS_SCORE, TIE_OUTCOME: TIE_SCORE, WIN_OUTCOME: WIN_SCORE }
# calculate a score based on their choice and the desired outcome
def get_score_beta(theirs, outcome):
  if [theirs, outcome] == [ROCK_INPUT, TIE_OUTCOME] \
    or [theirs, outcome] == [PAPER_INPUT, LOSS_OUTCOME] \
    or [theirs, outcome] == [SCISSORS_INPUT, WIN_OUTCOME]: # Rock play
    return ROCK_SCORE + outcomeDict[outcome]
  elif [theirs, outcome] == [PAPER_INPUT, TIE_OUTCOME] \
    or [theirs, outcome] == [SCISSORS_INPUT, LOSS_OUTCOME] \
    or [theirs, outcome] == [ROCK_INPUT, WIN_OUTCOME]: # Paper play
    return PAPER_SCORE + outcomeDict[outcome]
  else: # Scissors play
    return SCISSORS_SCORE + outcomeDict[outcome]

# Calculate the total score from the playbook
def solve_part1():
  total_score = 0

  with open(get_path()) as fp:
    for line in fp:
      choices = line.strip().split(' ')
      total_score += get_score(choices[0], choices[1])      

  print('total score: %s' % (total_score))

# Calculate the alternate total score from the playbook
def solve_part2():
    total_score = 0

    with open(get_path()) as fp:
      for line in fp:
        choices = line.strip().split(' ')
        total_score += get_score_beta(choices[0], choices[1])      

    print('total score: %s' % (total_score))

if __name__ == '__main__':
  print('Part 1:')
  solve_part1()

  print('Part 2:')
  solve_part2()