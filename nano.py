def add(a, b):
    print("Adding values:", a, b)
    if a is None or b is None:
        raise ValueError("Inputs cannot be None")
    return a + b

