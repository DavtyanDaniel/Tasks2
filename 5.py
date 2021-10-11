# buuble sort

def bubble_sort(lst: list) -> list:
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                k = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = k
    return lst

ls = [1, 5, 4, 2, 1, 500, 250, 100, 50, 20]

print(bubble_sort(ls))