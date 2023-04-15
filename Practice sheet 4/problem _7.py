'''Write a function called number_of_factors that takes an integer and returns how many factors the
number has and print all factors.'''
def number_of_factors(n):
   factors=[]
   for i in range(1,n+1):
       if n%i==0:
           factors.append(i)
   print('The factors of number are',factors,'number of factors are',len(factors))
a=int(input('Enter number : '))
number_of_factors(a)
   
