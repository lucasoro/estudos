def foo(num, div):
    if num <= 2:
        return (div)
    return foo(num / div, div) if not (num % div) else foo(num, div + 1)


print(foo(517, 2))