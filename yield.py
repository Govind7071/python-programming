# write a generator function that yields even number up to a specific limit


"""In Python, yield is used inside a function to turn it into a generator.
Instead of returning a single value and finishing, a generator yields 
values one-by-one, pausing after each value and resuming later."""






def even_generator(limit) :

    for i in range(2,limit+1,2):
        yield i


for num in even_generator(10):
    print(num)


