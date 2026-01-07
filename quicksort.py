# 3-Way Quick Sort (List-based / Functional Quick Sort)
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
# return quicksort(left) + middle + quicksort(right) 

# if __name__ == "__main__":
#     sample_array = [64, 34, 25, 12, 22, 11, 90]
#     sorted_array = quicksort(sample_array)
# print("Sorted array is:", sorted_array)

# Lomuto Partition mrthod (In-place Quick Sort)

# def lomuto_partition(arr,low,high):
#     pivot = arr[high]
#     i = low-1
#     for j in range(low,high);
#     arr[j <= arr[high]:
#     i = i + 1
#     arr[i],arr[j] = arr[j],arr[i]]
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i +1

#     def quicksort(arr,low,high):
#         if low < high:
#             pi = lomuto_partition(arr,low,high)
#             quicksort(arr,low,pi-1)
#             quicksort(arr,pi+1,high)
#             return arr

#     if __name__ == "__main__":
#         sample_array = [64, 34, 25, 12, 22, 11, 90]
#         sorted_array = quicksort(sample_array,0,len(sample_array)-1)
#         print("Sorted array is:", sorted_array)

# Hoare partition method (In-place Quick Sort)
# def hoare_partition(arr,low,high):
#     pivot = arr[low]
#     i = low-1
#     j = high + 1
#     while True:
#     i += 1
#     while arr[i] < pivot:
#         i += 1
#     j -= 1
#     while arr[j] > pivot:
#         j -= 1
#         if i >= j:
#             return j
#             arr[i],arr[j] = arr[j],arr[i]

#     def quicksort(arr,low,high):
#         if low < high:
#             pi + hoare_partition(arr,low,high)
#             quicksort(arr,low,pi)
#             quicksort(arr,pi+1,high)
#             return arr

#     if __name__ == "__main__":
#         sample_array = [64, 34, 25, 12, 22, 11, 90]
#         sorted_array = quicksort(sample_array,0,len(sample_array)-1)
#         print("Sorted array is:", sorted_array)


