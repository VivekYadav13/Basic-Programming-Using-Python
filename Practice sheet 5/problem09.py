''' Write a Python program to find the list of words that are longer than n from a given list of words.'''
a=[]
for i in range(5):
    st=input('Enter word in list : ')
    a.append(st)
n=int(input('Enter length : '))
for j in a:
    if len(j)>n:
        print(j)
    
        
