import random
def quicksort(arr, start , stop):
    if(start < stop):
          
        pivotindex = partitionrand(arr,\
                             start, stop)
          
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
  
def partitionrand(arr , start, stop):
  
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
  
def partition(arr,start,stop):
    pivot = start 
    i = start + 1 
      
    for j in range(start + 1, stop + 1):
          
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
def partition2(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
def quickSort2(array, low, high):
    if low < high:

        pi = partition(array, low, high)
 
        quickSort2(array, low, pi - 1)
 
        quickSort2(array, pi + 1, high)

ch = "1"
while(ch!="0"):
  print("1. Deterministic")
  print("2. Randomized")
  ch = input("0. Exit\n")
  if(ch=="0"):
    break
  elif ch=="1":
    num = int(input("Enter number of elements : "))
    arr = []
    for i in range(0,num):
      temp = int(input("Enter element : "))
      arr.append(temp)
    quickSort2(arr, 0, len(arr) - 1)
    print("Sorted array : ",arr)
  elif ch=="2":
    num = int(input("Enter number of elements : "))
    arr = []
    for i in range(0,num):
      temp = int(input("Enter element : "))
      arr.append(temp)
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array : ",arr)



