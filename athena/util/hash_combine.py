def hash_combine(lhs, rhs):
    lhs ^= rhs + 0x9E3779B9 + (lhs << 6) + (lhs >> 2)
    return lhs
