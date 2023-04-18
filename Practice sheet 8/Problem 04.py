''' Write a Python function that takes two lists and returns True if they have at least
one common member.'''
def func_1(a,b):
    for i in a:
        for j in b:
            if i==j:
                return True
            return False
l1=list(input('Enter elements of list : '))
l2=list(input('Enter elements of list : '))
print(func_1(l1,l2))
