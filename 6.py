# 6. Trvac e students_points = {"John": [42, 55, 81], "Raja": [90, 64, 39], "Rodriges": [85, 80, 20], "Michael": [10, 90, 40]}.
#    Petq e gtnel ayn usanoxin um gumarayin gnahatakanner@ amenabardzrn en.
#    Verjum piti tpeq usanoxi anun@ ev ira gnahatakanneri gumar@.

students_points = {"John": [42, 55, 81],
                   "Raja": [90, 64, 39],
                   "Rodriges": [85, 80, 20],
                   "Michael": [10, 90, 40]}

sum1 = [0, '']

for i, j in students_points.items():
    if sum(j) > sum1[0]:
        sum1[0] = sum(j)
        sum1[1] = i

print(sum1)


