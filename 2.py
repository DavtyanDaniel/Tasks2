# 2. Input e arvum kamayak tiv. Petq e stugel ayd tiv@ 2-i astichan e te voch.

num = int(input("Enter the number"))

while num > 1:
    num = num / 2
    if num % 2 != 0 and num != 1:
        print('False')
        break
else:
    print('True')


