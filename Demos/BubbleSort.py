# Python program for implementation of Selection 
# Sort 
import sys 
import time


def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
  

# Using readlines() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 

arr = []
# Strips the newline character 
for line in Lines: 
    arr.append(line.strip())

length = len(arr)

print ("count :", length)
  
start_time = time.perf_counter()

bubbleSort(arr) 

end_time = time.perf_counter()
  
#Driver code to test above 
print ("Sorted array") 
for i in range(length): 
    print(arr[i])

print ("time : Duration : Bubble Sort", end_time - start_time)