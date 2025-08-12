def TestArithmetic(a, b):
  x0 = a + b
  x1 = x0 * a
  x2 = x1 / b
  x3 = a % b
  x4 = -x2
  b0 = (x0 == 1)
  b1 = (x2 != x3)
  b2 = (x0 > x1)
  b3 = (x0 >= x1)
  b4 = (x0 < x1)
  b5 = (x0 <= x1)
  b6 = not b3
  return x0