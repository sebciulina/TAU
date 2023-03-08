def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    input_str = input("Enter array elements separated by a space: ")
    elements_list = input_str.split()
    sorted_list = quicksort(elements_list)
    print("The array before sorting: ", elements_list)
    print("The array after sorting: ", sorted_list)
