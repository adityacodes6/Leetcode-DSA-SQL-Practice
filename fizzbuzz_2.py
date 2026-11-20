# WAP that print the numbers from 1 to 50
# for multiple of 3 print 'Fizz'
# for the multiplicative of 5 print 'Buzz'
# for the numbers multiple of both print FizzBuzz

for i in range(1, 51):
    if i % 3==0 and i % 5==0:
        print('FizzBuzz')
        continue
    elif i % 3==0:
        print('Fizz')
        continue
    elif i % 5==0:
        print('Buzz')
        continue
    else:
        print(i)