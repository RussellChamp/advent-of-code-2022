# Day 04: Camp Cleanup

import os
import re

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

def fully_contains(a, b, c, d):
  # if the first item is contained in the second
  # or the second item is contained in the first
  return (a >= c and b <= d) or (c >= a and d <= b)

def any_overlap(a,b,c,d):
  # if the first item contains any overlap on the second item
  # if either the upper or lower of the first item exist within the second item
  # or the upper or lower of the second item exist within the first item
  return (a >= c and a <= d) or (b >= c and b <= d) \
    or (c >= a and c <= b) or (d >= a and d <= b)

def solve_part1():
  total = 0

  with open(get_path()) as fp:
    for line in fp:
      [first_lower, first_upper, second_lower, second_upper] = map(int, re.split(r',|-', line))
      if fully_contains(first_lower, first_upper, second_lower, second_upper):
        total += 1

  print('ANSWER: In how many assignment pairs does one range fully contain the other?')
  print('Total: %d' % (total))
def solve_part2():
  total = 0

  with open(get_path()) as fp:
    for line in fp:
      [first_lower, first_upper, second_lower, second_upper] = map(int, re.split(r',|-', line))
      if any_overlap(first_lower, first_upper, second_lower, second_upper):
        total += 1
  
  print('ANSWER: In how many assignment pairs do the ranges overlap?')
  print('Total: %d' % (total))

if __name__ == '__main__':
  solve_part1()
  solve_part2()