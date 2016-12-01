#Query the user for n(The maximum number in the range)
n = input('Insert the maximum value in the range:')

#According to value n inserted by the user, find the prime numbers in that range and print them out
def prime(number):
    for x in range(2,n+1):
        count = 0
    for y in range(2,x):
        if x%y != 0:
            count += 1
    if count == x-2:
        print x,