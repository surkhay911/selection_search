from random import randint


def find_min_index(arr): # ищем индекс минимального значения
    min_value = arr[0]
    min_index = 0
    for i in range(1,len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    return min_index


def selection_search(arr): #алгоритм сортировки выбором
    newarr = []
    for i in range(1,len(arr)):
        min_index = find_min_index(arr) #используем функцию поиска минимального значения
        newarr.append(arr.pop(min_index))
    return newarr

x = []
for i in range(10):#рандомим числа в массиве
    x.append(randint(1,1000))
print(x)

print(selection_search(x))
