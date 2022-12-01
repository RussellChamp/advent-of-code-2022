import os

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

# Get the sum of the largest group
def solve_part1():
  [idx, value] = [0, 0]
  [max_idx, max_value] = [0, 0]

  with open(get_path()) as fp:
    for line in fp:
      if line == '\n':
        if value >= max_value:
          [max_idx, max_value] = [idx, value]
        [idx, value] = [idx+1, 0]
      else:
        value += int(line)

  print('largest sum #%s: %s' % (max_idx, max_value))

# Get the sum of the 3 largest groups
def solve_part2():
  largest = [0]
  value = 0

  with open(get_path()) as fp:
    for line in fp:
      if line == '\n':
        largest.append(value)
        largest.sort(reverse=True)
        largest = largest[:3]
        value = 0
      else:
        value += int(line)
    
  print('largest 3 sums: %s, %s, %s' % (largest[0], largest[1], largest[2]))
  print('total sum: %s' % sum(largest))

if __name__ == '__main__':
  print('Part 1:')
  solve_part1()

  print('Part 2:')
  solve_part2()