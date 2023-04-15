'''Write a function called sum_digits that is given an integer num and returns the sum of the
digits of num.'''
def sum_digits(num):
    summ=0
    while num>0:
        summ=summ+num%10
        num=num//10
    return summ
no=int(input('Enter number : '))
print('Sum of digits is',sum_digits(no))
