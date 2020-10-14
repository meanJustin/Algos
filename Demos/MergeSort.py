# Python program for implementation of Selection 
# Sort 
import sys 
import time

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
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

mergeSort(arr) 

end_time = time.perf_counter()
  
#Driver code to test above 
print ("Sorted array") 
for i in range(length): 
    print(arr[i])

print ("time : Duration : Bubble Sort", end_time - start_time)