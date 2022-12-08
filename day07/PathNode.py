class PathNode:
  def __init__(self, name, size = 0):
    self.name = name
    self.size = size
    self.parent = None
    self.children = {}

  def has_parent(self):
    # print('%s has a parent? %s' % (self.name, self.parent is not None))
    return self.parent is not None

  def set_parent(self, parent):
    self.parent = parent

  def has_child(self, name):
    # print('%s has child %s? %s' % (self.name, name, self.children.has_key(name)))
    return self.children.has_key(name)
  
  def add_child(self, name, size = 0):
    # print('+ adding %s to %s' % (name, self.name))
    self.children[name] = PathNode(name, size)
    self.children[name].set_parent(self)
    self.size += size

    ptr = self
    while ptr.has_parent():
      ptr = ptr.parent
      ptr.size += size
  
  def is_directory(self):
    return len(self.children) > 0

  def print_self(self, indentation = 0):
    size = '(%d)' % (self.size) + (' [%d items]' % (len(self.children)) if self.is_directory() else '')
    print('%s%s %s' % (' ' * indentation, self.name, size))
    for key in self.children:
      self.children[key].print_self(indentation+1)
  
  def go_up_one_level(self):
    if self.has_parent():
      # print('-> moved up one level from %s to %s' % (self.name, self.parent.name))
      return self.parent
    return self

  def go_to_root(self):
    if self.has_parent():
      # print('-> going to root from %s' % (self.name))
      return self.parent.go_to_root()
    return self

  def go_to_child(self, name):
    if self.has_child(name):
      # print('-> going to %s from %s' % (name, self.name))
      return self.children[name]
    return self

  def get_directories_le(self, size):
    dirs = []
    for key in filter(lambda c: self.children[c].is_directory(), self.children):
      if self.children[key].size <= size:
        dirs.append([self.children[key].name, self.children[key].size])
      dirs += self.children[key].get_directories_le(size)
    return dirs

  def iterate_all_directories(self):
    dirs = [[self.name, self.size]]
    for key in self.children:
      dirs += self.children[key].iterate_all_directories()
    return dirs

  def find_smallest_at_least(self, required_size):
    all_dirs = self.iterate_all_directories()
    adequate_size_dirst = filter(lambda item: item[1] >= required_size, all_dirs)
    smallest_dir = min(adequate_size_dirst, key=lambda item: item[1])
    return smallest_dir
