def binary_search(arr, target):
    # n = len(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr =[2,4,6,8,14,18,20]
target = int(input("Enter a number to search: "))
result = binary_search(arr,target)
if result != -1:
    print(f"Element {target} present at index {result}")
else:
    print(f"Element Not Found")
