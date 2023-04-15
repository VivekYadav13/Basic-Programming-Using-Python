'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz''''
str1=input('Enter a word: ')
str2=input('Enter a word: ')
a=str1[0]+str1[1]
b=str2[0]+str2[1]
a,b=b,a
print(a+str1[2:]+b+str2[2:])
