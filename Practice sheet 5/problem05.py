'''Write a function called closest that takes a list of numbers L and a number n and returns
the largest element in L that is not larger than n. For instance, if L=[1,6,3,9,11] and n=8,
then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than
8. Return “No Match” if all of the things in L are greater than n.'''
b=[]
for i in range(5):
    a=input('enter the numbers : ')
    b.append(a)
print(b)
n=input('Enter the reference number : ')
b.sort()
ind=b.index(n)
print(b[ind-1],'is the closest number to the entered number')

