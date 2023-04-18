'''Find largest and smallest number in a list'''
a=list(input('Enter numbers : '))
a.sort()
print(a)
print('the largest number in the list is',a[len(a)-1])
print('the smallest number in the list is',a[0])
