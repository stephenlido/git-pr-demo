def add(a, b):
    if a is None or b is None:
        raise ValueError("Inputs cannot be None")
    return int(a) + int(b)

