Write a Python program to get a string made of the first 2 and the last 2
chars from a given string. If the string length is less than 2, return
instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
str=input('Enter a string:')
l=len(str)
if l>=2:
        print('New string is ', str[0]+str[1]+str[-2]+str[-1])
else:
    print('Empty String')
