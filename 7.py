
# 7. Trvac e my_list = [[55, 2, 18], [96, 45], [85, 86, 90], [4, 852, 444, 233], [785, 632, 56, 81, 53]].
#    Petq e gtnel amenamec tiv@ ev ay listi index@ vortex ayd tiv@ gtnvum e.
#    Tvyal depqum mer mot amenamec tiv@ 852-n e ev aynq gtnvum e 3 indexi tak gtnvox list-i mej.
#    print-i orinak:
#    852 3

my_list = [[55, 2, 18], [96, 45], [85, 86, 90], [4, 852, 444, 233], [785, 632, 56, 81, 53]]
greatest_number = [0, 0]


for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if my_list[i][j] > greatest_number[0]:
            greatest_number[0] = my_list[i][j]
            greatest_number[1] = i


print(greatest_number)

