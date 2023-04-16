'''Determine the maximum and minimum frequency character in a given string. (If multiple characters
have maximum and minimum frequency print them all)'''
a=input('Enter string : ')
dicti={}
for i in a:
    if i in dicti:
        dicti[i]+=1
    else:
        dicti[i]=1
c=max(dicti.values())
for j in dicti:
    if dicti[j]==c:
        print(j)
print(c)
