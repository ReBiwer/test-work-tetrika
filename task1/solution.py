def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for i, (name, expected_type) in enumerate(annotations.items()):
            if name == 'return':
                continue
            if i < len(args):
                value = args[i]
            elif name in kwargs:
                value = kwargs[name]
            else:
                continue
            if not isinstance(value, expected_type):
                raise TypeError(f"Argument '{name}' must be {expected_type.__name__}, got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper 

@strict
def sum_two(a: int, b: int) -> int:
    return a + b
