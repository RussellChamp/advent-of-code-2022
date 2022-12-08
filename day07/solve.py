# Day 07: No Space Left On Device

import os
from PathNode import PathNode

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

def get_dir_tree():
  ptr = PathNode('/')

  with open(get_path()) as fp:
    for cmd in fp:
      cmd = cmd.strip()
      # print(cmd)
      if cmd[0] == '$':
        # commands
        if cmd[2:4] == 'ls':
          pass # basically a noop
        elif cmd[2:4] == 'cd':
          if cmd[5:] == '/':
            ptr = ptr.go_to_root()
          elif cmd[5:] == '..':
            ptr = ptr.go_up_one_level()
          else:
            ptr = ptr.go_to_child(cmd[5:])
        pass
      elif cmd[:3] == 'dir':
        # list a directory
        ptr.add_child(cmd[4:])
      else:
        # listing a file
        [size, name] = cmd.split()
        ptr.add_child(name, int(size))

  return ptr.go_to_root()


def solve_part1():
  root = get_dir_tree()
  # ptr.print_self()
  dirs = root.get_directories_le(100000)
  total_size = sum(map(lambda item: item[1], dirs))

  print('Day 07: Part 1')
  print('GOAL: Find all of the directories with a total size of at most 100000.')
  print('ANSWER: What is the sum of the total sizes of those directories?')
  print('Total size: %d' % (total_size))

def solve_part2():
  total_size     = 70000000
  required_space = 30000000

  root = get_dir_tree()
  delete_size = required_space - (total_size - root.size)
  # print('Current usage is %d / %d [additional %d needed to get to %d / %d]' % \
  #   (root.size, total_size, delete_size, total_size - required_space, total_size))
  smallest = root.find_smallest_at_least(delete_size)

  print('Day 07: Part 2')
  print('GOAL: Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.')
  print('ANSWER: What is the total size of that directory?')
  print('Need to free up %d' % delete_size)
  print('Smallest directory: %s - %d' % (smallest[0], smallest[1]))

if __name__ == '__main__':
  solve_part1()
  solve_part2()