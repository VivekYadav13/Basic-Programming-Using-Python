'''Write a program that asks the user to enter a string s and then converts s to lowercase, removes
all the periods and commas from s, and prints the resulting string. '''
stri=input('Enter a string : ')
a=''
b=''
a=stri.lower()
b=a.replace(',','')
print(b)
