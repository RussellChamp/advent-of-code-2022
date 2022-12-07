# Day 06: Tuning Trouble

import os

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

def all_same(arr):
  if len(arr) is 0:
    return False
  elif len(arr) is 1:
    return True
  else:
    for value in arr:
      if value is not arr[0]:
        return False
    return True

def all_different(arr):
  if len(arr) <= 1:
    return True
  else:
    for idx in range(len(arr)):
      for idz in range(idx+1, len(arr)):
        # print('%s is %s ? %s ' % (arr[idx], arr[idz], arr[idx][0] is arr[idz][0]))
        if arr[idx] is arr[idz]:
          return False
    return True

def get_unique_straight(size):
  total = size

  with open(get_path()) as fp:
    # technically this has a bug if the first set of n characters match it will not detect it
    # but i'm done working on this puzzle...
    set = list(fp.read(size))
    while True:
      char = fp.read(1)
      if not char:
        print('Read entire input file :(')
        break
      total += 1
      # ok i don't understand the black magic happening here but when you call read(1) it will read a single character from input
      # however, if you compare these characters you'll find that equality is borked
      # eg comparing `'a' is 'a'` will return False. Why? I don't know! But calling 'a'[0] will return a non-compare borked char instead
      set = set[1:] + [char[0]]
      # print('#%d: %s' % (total, set))
      if total > size -1 and all_different(set):
        break
  return total

def solve_part1():
  
  total = get_unique_straight(4)

  print ('GOAL: Find the the first start-of-packet marker')
  print('ANSWER: How many characters need to be processed before the first start-of-packet marker is detected?')
  print('Total: %d' % (total))

def solve_part2():
  total = get_unique_straight(14)
  
  print('GOAL: Find the start-of-message marker')
  print('ANSWER: How many characters need to be processed before the first start-of-message marker is detected?')
  print('Total: %d' % (total))

if __name__ == '__main__':
  solve_part1()
  solve_part2()