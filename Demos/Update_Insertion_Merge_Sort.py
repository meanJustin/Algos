import random
import time
import math
import sys

# Insert sort function
def insertion_Sort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

# Selection Sort function
def selection_Sort(arr) :
    # Traverse through all array elements 
    for i in range(len(arr)): 
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
              
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Python program for implementation of  
# MergeSort (Alternative) 
def merge_Sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_Sort(L) # Sorting the first half 
        merge_Sort(R) # Sorting the second half 
  
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


# Merge two array with using method one
def method_One_Merge (arr_A, arr_B, sort_func) -> list:
    a_len = len(arr_A)              # Define a_len variable which reflects the length of Array_A
    b_len = len(arr_B)              # Define b_len variable which reflects the length of Array_B

    # If the last element in A is smaller than the first element in B then move
    # array A followed by array B to array M and return the Merged array
    if a_len == 0 or b_len == 0 :
        return
    if arr_A[a_len-1] <= arr_B[0] :
        return

    last_A = arr_A.pop()            # Popup the last element in A and store that in last_A
    first_B = arr_B.pop(0)          # Popup the first element in B and store that in last_A

    for i in range(b_len-1) :       # Insert the last element of A into Array B
        if arr_B[i] > last_A :      # Looping until meet the first greater value than last_A
            arr_B.insert(i, last_A)
            break
        if i == b_len - 1 :         # If not find then append the last_A in Array B
            arr_B.append(i, last_A)


    for i in range(a_len - 2, -1, -1) :     # Insert the first element of B into Array A
        if arr_A[i] < first_B :             # Looping until meet the first smaller value than first_B
            arr_A.insert(i + 1, first_B)
            break
        if i == 0:                          # If not find then insert the first_B into first in Array A
            arr_A.insert(0, first_B)

    # Add them to the other side of array
    # arr_B.append(last_A)
    # arr_A.append(first_B)

    # sort both of arrays with sort_Functions
    # sort_func(arr_A)
    # sort_func(arr_B)

    # Recall until merge has done
    method_One_Merge(arr_A, arr_B, sort_func)



# # Merge two array with using method two
def method_Two_Merge(arr_A, arr_B, merged_arr) :
    if len(arr_A) == 0:             # If arr_A is empty then merge the Arr_B into the merged array
        merged_arr += arr_B         # And return the merged array
        return merged_arr           

    if len(arr_B) == 0:             # If arr_B is empty then merge the Arr_A into the merged array
        merged_arr += arr_A         # And return the merged array
        return merged_arr

    # If the last element in A is smaller than first element in B then
    # copy all A to M followed by whole B and merging is complete
    if arr_A[-1] <= arr_B[0] :      
        merged_arr += arr_A + arr_B
        return merged_arr

    # if the B element is larger then move all the elements in A,
    # that are less than the first element in B into array M, as subarray block
    if arr_A[0] <= arr_B[0] :
        while len(arr_A) >= 1 and arr_A[0] <= arr_B[0] :
            merged_arr.append(arr_A.pop(0))

        merged_arr.append(arr_B.pop(0))

    # otherwise just copy the B element to M
    # If the next element at top of B is smaller than the last element in A then
    # repeat the previous process;
    else :
        while len(arr_B) >= 1 and arr_A[0] >= arr_B[0] :
            merged_arr.append(arr_B.pop(0))

    method_Two_Merge(arr_A, arr_B, merged_arr)

# Divide the main array into small ones
# Each of them has equal size
# And also has rest of them
# And sort each of them
def divide_Array(arr) :
    length = len(arr)                       # define the length variable which reflect the length of array

    par_len = (int)(math.sqrt(length))      # get the perferable equal_length
    print (par_len)

    block_arr = []                          # Define array of block arrays
    rest_arr = []                           # Define rest_array

    block_cnt = 0                           # Set the block_cnt = 0
    for i in range(length) :                # Looping and divide the main array into block arrays which has equal size
        if i % par_len == 0 :
            block_cnt += 1
            block_arr.append([])
        block_arr[block_cnt - 1].append(arr[i])

    rest_arr = block_arr.pop()              # Make a rest array and place in apart from main block array
    block_cnt -= 1
    if len(rest_arr) == par_len :
        block_arr.append(rest_arr)
        rest_arr = []
        block_cnt += 1

    for i in range(block_cnt) :             # Sort every block array(including rest array)
        block_arr[i].sort()
    rest_arr.sort()

    return [block_arr, rest_arr]


# Merge the blocks with divided array
def merge_block_arrays(block_arr, func_sort, rest_arr, merge_func):
    cnt = len(block_arr)            # Get the how many blocks remains

    new_block = []                  # Generate new block
    for i in range(0, cnt, 2) :     # Make pair of them to make new merged block
        if i == cnt - 1 :
            break

        if merge_func == method_One_Merge :
            merge_func(block_arr[i], block_arr[i+1], func_sort)
            new_block.append(block_arr[i] + block_arr[i+1])
        else :
            merged_arr = []
            merge_func(block_arr[i], block_arr[i+1], merged_arr)
            new_block.append(merged_arr)

    if cnt % 2 == 1 :               # If the count is odd then left the rest one and add the new block arrays
        new_block.append(block_arr.pop())

    if len(new_block) == 1 :        # If the length of block is only one then merge with rest array and return
        sorted_arr = []

        if merge_func == method_One_Merge :
            merge_func(new_block[0], rest_arr, func_sort)
            sorted_arr = new_block[0] + rest_arr
        else :
            sorted_arr = []
            merge_func(new_block[0], rest_arr, sorted_arr)

        print (sorted_arr)
        return sorted_arr

    merge_block_arrays(new_block, func_sort, rest_arr, merge_func)



# get Array from file
def getArrayFromFile() :
    # Using readlines() 
    file1 = open('myfile.txt', 'r') 
    Lines = file1.readlines() 

    arr = []
    # Strips the newline character 
    for line in Lines: 
        arr.append(line.strip())

    return arr


if __name__ == "__main__":
    
    # Do Regular Insertion sort
    arr = getArrayFromFile()

    start_time = time.perf_counter()
    insertion_Sort(arr) 
    print (arr)
    dur_time = time.perf_counter() - start_time
    print ("Regular Insertion Sort : ", dur_time)


    # Do Regular Seletion sort
    arr = getArrayFromFile()
    start_time = time.perf_counter()
    selection_Sort(arr) 
    print (arr)
    dur_time = time.perf_counter() - start_time
    print ("Regular Seletion Sort : ", dur_time)


    # Do Regular Merge sort
    arr = getArrayFromFile()
    start_time = time.perf_counter()
    merge_Sort(arr) 
    print (arr)
    dur_time = time.perf_counter() - start_time
    print ("Regular Merge Sort : ", dur_time)


    # Do Parallel insertion sort
    arr = getArrayFromFile()

    start_time = time.perf_counter()
    block_arr, rest_arr = divide_Array(arr)
    merge_block_arrays(block_arr, insertion_Sort, rest_arr, method_One_Merge)
    dur_time = time.perf_counter() - start_time
    print ("Parallel insertion sort : ", dur_time)




    # Do Parallel selection sort
    arr = getArrayFromFile()

    start_time = time.perf_counter()
    block_arr, rest_arr = divide_Array(arr)
    merge_block_arrays(block_arr, selection_Sort, rest_arr, method_One_Merge)
    dur_time = time.perf_counter() - start_time
    print ("Parallel selection sort : ", dur_time)



    # Do Parallel selection sort
    arr = getArrayFromFile()

    start_time = time.perf_counter()
    block_arr, rest_arr = divide_Array(arr)
    merge_block_arrays(block_arr, selection_Sort, rest_arr, method_Two_Merge)
    dur_time = time.perf_counter() - start_time
    print ("Parallel merge sort : ", dur_time)


    arr_A = [1,3,5,7,9]
    arr_B = [2,4,6,8,10]

    merged = []

    method_One_Merge(arr_A, arr_B, merged)
    print ("+===============================")
    print(arr_A + arr_B)

    # arr_A = [1,3,5,7,9]
    # arr_B = [2,4,6,8,10]

    # merged = []

    # method_Two_Merge(arr_A, arr_B, merged)
    # print ("+===============================")
    # print(merged)
	
# #Driver code to test above 


