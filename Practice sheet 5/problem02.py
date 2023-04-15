'''Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.'''
word=input('Enter word : ')
vow=['a','e','i','o','u']
for i in word:
    if i in vow:
        print(set(i),end=',')
