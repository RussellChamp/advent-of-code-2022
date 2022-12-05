# Day 03: Rucksack Reorganization

import os

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

def get_priority(item):
  iitem = ord(item)
  if iitem >= 65 and iitem <= 90: # between A-Z
    return iitem - 38 # range 27 and 52
  elif iitem >= 97 and iitem <= 122: # between a-z
    return iitem - 96 # range between 1 and 26
  else:
    return 0

def solve_part1():
  total = 0

  with open(get_path()) as fp:
    for line in fp:
      [first,second] = [line[:len(line)/2], line[len(line)/2:]]
      for c in first:
        if c in second:
          total += get_priority(c)
          break

  print('GOAL: Find the item type that appears in both compartments of each rucksack.')
  print('ANSWER: What is the sum of the priorities of those item types?')
  print('Total: %d' % (total))

def solve_part2():
  group = 0
  total = 0

  with open(get_path()) as fp:
    while True:
      [first, second, third] = [fp.readline(), fp.readline(), fp.readline()]
      if first == '':
        break
      group += 1
      for c in first:
        if c in second and c in third:
          total += get_priority(c)
          break

  print('GOAL: Find the item type that corresponds to the badges of each three-Elf group.')
  print('ANSWER: What is the sum of the priorities of those item types?')
  print('Total: %d' % (total))

if __name__ == '__main__':
  solve_part1()
  solve_part2()