from timeit import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Тестуємо випадковий масив з чисел в діапазоні від 1 до 1000
array_int = array_random = [random.randint(1, 1000) for _ in range(10000)]

tim_sort_time = timeit(lambda: array_int.sort(), number=1000)

print("Time execution of Timsort for integers array:", tim_sort_time)

insertion_sort_time = timeit(lambda: insertion_sort(array_int.copy()), number=1000)

print("Time execution of insertion sort for integers array:", insertion_sort_time)

merge_sort_time = timeit(lambda: merge_sort(array_int.copy()), number=1000)

print("Time execution of merge sort for integers array:", merge_sort_time)

# Тестуємо рядки різної довжини
array_strings = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10))) for _ in range(10000)]

tim_sort_time = timeit(lambda: array_strings.sort(), number=1000)

print("Time execution of Timsort for strings array:", tim_sort_time)

insertion_sort_time = timeit(lambda: insertion_sort(array_strings.copy()), number=1000)

print("Time execution of insertion sort for strings array:", insertion_sort_time)

merge_sort_time = timeit(lambda: merge_sort(array_strings.copy()), number=1000)

print("Time execution of merge sort for strings array:", merge_sort_time)

# Тестуємо випадковий масив та сортуємо його частково
array_partially_sorted = [random.randint(1, 10000) for _ in range(10000)]
array_partially_sorted[:5000] = sorted(array_partially_sorted[:5000])

tim_sort_time = timeit(lambda: array_partially_sorted.sort(), number=1000)

print("Time execution of Timsort for partially sorted array:", tim_sort_time)

insertion_sort_time = timeit(lambda: insertion_sort(array_partially_sorted.copy()), number=1000)

print("Time execution of insertion sort for partially sorted:", insertion_sort_time)

merge_sort_time = timeit(lambda: merge_sort(array_partially_sorted.copy()), number=1000)

print("Time execution of merge sort for partially sorted:", merge_sort_time)