# Day 08: Treetop Tree House

import os

def get_path():
  return os.path.join(os.path.dirname(__file__), 'data.txt')

def build_grid():
  grid = []
  with open(get_path()) as fp:
    for line in fp:
      grid.append(map(int, line.strip()))
  return grid

def get_column(grid, col_idx):
  return map(lambda row: row[col_idx], grid)

def is_visible(grid, row_idx, col_idx):
  # all edge trees are visible
  if row_idx == 0 or row_idx == len(grid) -1 \
    or col_idx == 0 or col_idx == len(grid[0]) - 1:
    return True
  cell = grid[row_idx][col_idx]
  # check the left side
  if all([item < cell for item in grid[row_idx][:col_idx]]):
    return True
  # check the right side
  if all([item < cell for item in grid[row_idx][col_idx+1:]]):
    return True
  # check the top
  if all([item < cell for item in get_column(grid, col_idx)[:row_idx]]):
    return True
  # check the bottom
  if all([item < cell for item in get_column(grid, col_idx)[row_idx+1:]]):
    return True
  return False

def score_row(height, row):
  score = 0
  for item in row:
    score += 1
    if item >= height:
      break
  return score

def get_score(grid, row_idx, col_idx):
  # all edge trees will have at least one size with a 0 score
  if row_idx == 0 or row_idx == len(grid) -1 \
    or col_idx == 0 or col_idx == len(grid[0]) - 1:
    return 0

  height = grid[row_idx][col_idx]
  left_score = score_row(height, grid[row_idx][:col_idx][::-1]) # [::-1] reverses a slice. who knew? 
  right_score = score_row(height, grid[row_idx][col_idx+1:])
  top_score = score_row(height, get_column(grid, col_idx)[:row_idx][::-1]) # reverse it because we are looking "backwards"
  bottom_score = score_row(height, get_column(grid, col_idx)[row_idx+1:])
  total_score = left_score * right_score * top_score * bottom_score
  # print ('grid[%d][%d] = %d, (%d, %d, %d, %d) = %d' % (row_idx, col_idx, height, left_score, right_score, top_score, bottom_score, total_score))
  return total_score

def solve_part1():
  total = 0

  grid = build_grid()
  # print('height %d, width %d' % (len(grid), len(grid[0])))
  for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[row_idx])):
      if is_visible(grid, row_idx, col_idx):
        total += 1

  print('Day 08: Part 1')
  print('GOAL: Count the number of trees that are visible from outside the grid when looking directly along a row or column.')
  print('ANSWER: How many trees are visible from outside the grid?')
  print('Total: %d' % (total))

def solve_part2():
  best_score = 0
  grid = build_grid()
  for row_idx in range(0, len(grid)):
    for col_idx in range(0, len(grid[row_idx])):
      score = get_score(grid, row_idx, col_idx)
      best_score = score if score > best_score else best_score

  print('Day 08: Part 2')  
  print('GOAL: Consider each tree on your map.')
  print('ANSWER: What is the highest scenic score possible for any tree?')
  print('Best Score: %d' % (best_score))

if __name__ == '__main__':
  solve_part1()
  solve_part2()