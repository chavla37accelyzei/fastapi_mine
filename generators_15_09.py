print("generator gives iterators:")
# genrator created with yeild keyword
def topten():
    n=1
    while n<=10:
        sq = n*n
        yield sq
        n =  n+1
values = topten()
for i in values:
    print(i)

# fibanoci series using generator
def fib():

    a,b =0,1
    while True:
        yield a
        a,b =b,a+b
fib_generator = fib()
for i in range(10):
    print(next(fib_generator))