list_1 = input('Введите последовательность чисел через пробел: ').split()
list_1 = [int(list_1[i]) for i in range(len(list_1))]

n = int(input())


def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return(array)


sort(list_1)
print(list_1)


def binary_search(array, element, left, right):
    if element not in array:  # если левая граница превысила правую
        return 'False'  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        if middle - 1 < 0:
            return "Введенное число является минимальным"
        return middle - 1  # возвращаем индекс меньший на 1
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print('Позиция элемента, которая меньше введенного числа - ', binary_search(list_1, n, 0, len(list_1)))