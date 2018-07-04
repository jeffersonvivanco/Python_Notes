from time import perf_counter

start = perf_counter()
print(start)
print('Something to print to waste time')
end = perf_counter()
print(str(round((end - start) * 1000, 1)))
