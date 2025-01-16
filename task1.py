import timeit
import random
# Сортування вставками (Insertion sort)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Сортування злиттям (Merge sort)
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





# Стоворення масивів
test_array_short = [random.randrange(1, 100) for _ in range(10)]
test_array_medium = [random.randrange(1, 100) for _ in range(100)]
test_array_long = [random.randrange(1, 100) for _ in range(300)]



# Test Вимірювання часу Python Sort  
# Часова складність O(n)
print(50 * '-')
t_timsort_sort_short = timeit.timeit(lambda: test_array_short.copy().sort(), number=10000)
t_timsort_sort_medium = timeit.timeit(lambda: test_array_medium.copy().sort(), number=10000)
t_timsort_sort_long = timeit.timeit(lambda: test_array_long.copy().sort(), number=10000)

print(f'Час сортування масиву з < {len(test_array_short)} > ел. методом Python sort {t_timsort_sort_short}')
print(f'Час сортування масиву з < {len(test_array_medium)} > ел. методом Python sort {t_timsort_sort_medium}')
print(f'Час сортування масиву з < {len(test_array_long)} > ел. методом Python sort {t_timsort_sort_long}')



# Тест Вимірювання часу Insertion sort
# Часова складність O(n2)

t_insertion_sort_short = timeit.timeit(lambda: insertion_sort(test_array_short.copy()),number=10000)
t_insertion_sort_medium = timeit.timeit(lambda: insertion_sort(test_array_medium.copy()),number=10000)
t_insertion_sort_long = timeit.timeit(lambda: insertion_sort(test_array_long.copy()),number=10000)
print(50 * '-')
print(f'Час сортування масиву з < {len(test_array_short)} > ел. методом Insertion sort {t_insertion_sort_short}')
print(f'Час сортування масиву з < {len(test_array_medium)} > ел. методом Insertion sort {t_insertion_sort_medium}')
print(f'Час сортування масиву з < {len(test_array_long)} > ел. методом Insertion sort {t_insertion_sort_long}')

# Тест Вимірювання часу Merge sort
# Часова складність O(n log n)

print(50 * '-')
t_merge_sort_short = timeit.timeit(lambda: merge_sort(test_array_short.copy()),number=10000)
t_merge_sort_medium = timeit.timeit(lambda: merge_sort(test_array_medium.copy()),number=10000)
t_merge_sort_long = timeit.timeit(lambda: merge_sort(test_array_long.copy()),number=10000)

print(f'Час сортування масиву з < {len(test_array_short)} > ел. методом Merge sort {t_merge_sort_short}')
print(f'Час сортування масиву з < {len(test_array_medium)} > ел. методом Merge sort {t_merge_sort_medium}')
print(f'Час сортування масиву з < {len(test_array_long)} > ел. методом Merge sort {t_merge_sort_long}')

# Висновки

# Merge Sort демонструє стабільну продуктивність на великих масивах.
# Insertion Sort працює швидше на малих або вже відсортованих даних, на великих даних він не є ефективним.
# Timsort значно швидший завдяки комбінуванню двох алгоритмів, особливо для "майже відсортованих" даних.
# Використання Timsort у Python обґрунтоване його універсальністю та ефективністю.