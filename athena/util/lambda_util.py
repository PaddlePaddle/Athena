def const(value):
    return lambda f: value


def join_map(values, sep=", "):
    def func(f, value):
        return value(f) if callable(value) else f(value)

    return lambda f: sep.join(func(f, value) for value in values)
