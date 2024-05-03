grades = ['53354', '2223', '4552', '443', '55545']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
students_abc = sorted(students)
stud = tuple(students_abc)
a = len(grades[0])
b = len(grades[1])
c = len(grades[2])
d = len(grades[3])
e = len(grades[4])
aa = sum(map(int, grades[0]))
bb = sum(map(int, grades[1]))
cc = sum(map(int, grades[2]))
dd = sum(map(int, grades[3]))
ee = sum(map(int, grades[4]))
A = aa / a
B = bb / b
C = cc / c
D = dd / d
E = ee / e
list_students = {stud[0]: A,
                 stud[1]: B,
                 stud[2]: C,
                 stud[3]: D,
                 stud[4]: E}
print(list_students)
