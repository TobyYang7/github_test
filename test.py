from icecream import ic


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)


name = "GitHub Copilot"
age = 2
test_val = 'test'
is_copilot = True

ic(quick_sort([1, 3, 6, 2, 4]))
ic(name, age, is_copilot)
ic(test_val)
