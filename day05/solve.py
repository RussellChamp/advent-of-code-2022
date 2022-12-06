# Day 05: Supply Stacks

import os
import re

# The moves part of the input data have been put into a separate file
def get_moves_path():
  return os.path.join(os.path.dirname(__file__), 'moves.txt')

# The stacks part of the input data have been transformed into rows instead of columns and put into a separate file
# Each row represents a stack with the bottom crate starting in the first index. letter are separated by spaces
def get_stacks_path():
  return os.path.join(os.path.dirname(__file__), 'stacks.txt')

def get_last(arr):
  return arr[-1]

def solve_part1():
  stacks = map(str.split, open(get_stacks_path()).readlines())
  # print(stacks)

  with open(get_moves_path()) as moves:
    for move in moves:
      [count, source, dest] = map(int, re.match('move (\d+) from (\d+) to (\d+)', move).groups())
      for _ in range(count):
        stacks[dest - 1].append(stacks[source - 1].pop())
      # print('Moved %d from stack %d to stack %d' % (count, source, dest))

  print('GOAL: Which crate will end up on top of each stack?')
  print('ANSWER: After the rearrangement procedure completes, what crate ends up on top of each stack?')
  tops = ''.join(map(get_last, stacks))
  print('Tops: %s' % (tops))

def solve_part2():
  stacks = map(str.split, open(get_stacks_path()).readlines())
  # print(stacks)

  with open(get_moves_path()) as moves:
    for move in moves:
      [count, source, dest] = map(int, re.match('move (\d+) from (\d+) to (\d+)', move).groups())
      # print('moving %d items from %s to %s' % (count, stacks[source-1], stacks[dest-1]))
      moved_items = stacks[source-1][-count:]
      del stacks[source-1][-count:]
      stacks[dest-1] += moved_items
  
  print('ANSWER: After the rearrangement procedure completes, what crate ends up on top of each stack?')
  tops = ''.join(map(get_last, stacks))
  print('Tops: %s' % (tops))

if __name__ == '__main__':
  solve_part1()
  solve_part2()