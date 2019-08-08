# using annotations
def add(x:int, y:int) -> int:
    return x + y

# lambda expression
a = [4, 1, 2, 3]
b = lambda a: sorted(a)

# closures
def func1(fname, lname):
    name = fname + ' ' + lname
    def greeting(greeting):
        return greeting + ' ' + name
    # returning function
    return greeting



# function with callback
def apply_async(func, args, *, callback):
    # compute the result
    result = func(*args)

    # invoke the callback with the result
    r = callback(result)
    return r

# callback example
def multiply_by_10(num):
    return num * 10

res = apply_async(add, (1, 3), callback=multiply_by_10)
print(res)