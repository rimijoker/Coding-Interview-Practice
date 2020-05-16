class MaxStack:
  def __init__(self):
    # Fill this in.

  def push(self, val):
    # Fill this in.

  def pop(self):
    # Fill this in.

  def max(self):
    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
"""
class MaxStack:
  def __init__(self):
    self.stack = []
    self.maxes = []

  def push(self, val):
    self.stack.append(val)
    if self.maxes:
      self.maxes.append(max(val, self.maxes[-1]))
    else:
      self.maxes.append(val)

  def pop(self):
    if self.maxes:
      self.maxes.pop()
    return self.stack.pop()

  def max(self):
    return self.maxes[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
"""