#Query the user for n(The maximum number in the range)
n = input('Insert the maximum value in the range:')

#According to value n inserted by the user, find and print out a list of fibbonacci numbers from 0 to the value n
def Fibonacci():
    x,y = 0,1
    yield x
    yield y
    while True:
        x, y = y, x + y
        yield y
        
def Sub_Fibonacci(minNumber, maxNumber):
    for cur in Fibonacci():
        if cur > maxNumber: return
        if cur >= minNumber:
            yield cur
            
for i in Sub_Fibonacci(0, n):
    print i