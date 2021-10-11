# 3. Trvac e my_list = [4, 9, 4, 13, 9, 13, 10, 10, 13, 7, 9, 13, 12, 9, 4, 5, 9, 12, 11, 6, 8, 5, 6, 13, 5, 8, 6, 6, 8, 4].
#    Petq e hashvel qani angam e my_list-i mej handipum 9 tvanshan@. (count metod ogtagorcel@ chi tuylatrvum)

counter = 0
my_list = [4, 9, 4, 13, 9, 13, 10, 10, 13, 7, 9, 13, 12, 9, 4, 5, 9, 12, 11, 6, 8, 5, 6, 13, 5, 8, 6, 6, 8, 4]

for num in my_list:
    if num == 9:
        counter += 1

print(counter)
