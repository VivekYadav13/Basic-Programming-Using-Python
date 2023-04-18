''' A certain CS professor gives 100-point exams that are graded on the scale
90- 100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts
an exam score as input and prints out the corresponding grade.'''
marks=int(input('Enter marks of student : '))
if 100>=marks>=90:
    print('A')
elif 89>=marks>=80:
    print('B')
elif 79>=marks>=70:
    print('C')
elif 69>=marks>=60:
    print('D')
else:
    print('F')
