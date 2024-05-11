
def hash_combine(lhs, rhs):
  lhs ^= rhs + 0x9e3779b9 + (lhs << 6) + (lhs >> 2)
  return lhs
