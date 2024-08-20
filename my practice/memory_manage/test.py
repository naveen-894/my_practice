from memory_profiler import profile
def my_generator():
    for i in range(1000):
        yield i

for value in my_generator():
    print(value)


import gc

@profile
def my_function():
    a = [1] * 1000000
    b = [2] * 1000000
    del b
    gc.collect()  # Force garbage collection
    return a

if __name__ == "__main__":
    my_function()
