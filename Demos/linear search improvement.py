import math
import multiprocessing
import random
import sys
import time

# Linear search function
def linear_search(arr, value): 
    for i in range(len(arr)): 
        if arr[i] == value: 
            return i 
    return -1

# Binary Search function
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1



# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  



# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
 


# Make parallel Array.
# Every array has sqrt(length of array) element
# Make another array for storing the first element of each parallel array
def sqrt_Parallel_Array (arr) :

    ref_arr = [0] # define reference array
    par_arr = [] # define parallel array
    temp_arr = [] # define temp array for making parallel array
    length = len(arr)   # total length of array
    par_len = int(math.sqrt(length)) # calculate of the sqrl(lengh) for divide into


    # Looping the whole array for buidling ref_arr & par_arr
    for i in range(length) :
        if i % par_len == 0 and i != 0:
            par_arr.append(temp_arr)
            temp_arr = []
            ref_arr.append(i)

        temp_arr.append(arr[i])

    # return the ref_arr and par_arr
    return {'ref_arr' : ref_arr, 'par_arr' : par_arr}

# Make reference array
def get_Reference_array (length) :
    par_len = int(math.sqrt(length)) # calculate of the sqrl(lengh) for divide into
    ref_arr = []    # define reference array
    i = 0   # define temp value for looping

    # making a reference array
    while i < length :
        ref_arr.append(i)
        i += par_len

    return ref_arr, par_len

# Do parallel linear search
# It has ref_arr, par_arr and arr as parameter and also value
# the value is what we have to find in this array

def parallel_Linear_Search(arr, ref_arr, par_len, value) :
    # if the value is greater then maximum value of array or less than the minimun value of the array then return false 
    if value < arr[0] and value > arr[len(arr) - 1]:
        return -1

    #1. Do linear search in the reference block if match found exit otherwise
    for i in range(len(ref_arr)) :

        # if there is the value in the reference array then return the True and Index value
        if arr[ref_arr[i]] == value :
            return ref_arr[i]

        # 2.Stop searching when an element in the reference block is larger than the input data, then break 
        if arr[ref_arr[i]] > value :
            break;


    #3. In the main array continue the linear search on the block referenced only. If match found or return not found and exit.
    
    ref_index = ref_arr[i - 1]  # From the break index, get the block of last element compared that was less than the input element.

    for i in range(ref_index, ref_index + par_len) :
        if arr[i] == value :
            return i

    # if there is not result then return false and null index
    return -1


# Improve Linear Search
def improve_Linear_Search(arr, value) :
    par_arr = {}
    length = len(arr)
    for i in range(length) :
        temp_len = len(arr[i])
        if not temp_len in par_arr :
            par_arr[temp_len] = []
        par_arr[temp_len].append({'value' : arr[i], 'index' : i})

    value_len = len(value)
    if value_len in par_arr :
        for i in range(len(par_arr[value_len])) :
            if value == par_arr[value_len][i]['value'] :
                print (value, par_arr[value_len][i]['index'])
                return par_arr[value_len][i]['index']
    return -1


# Get frequency of the value in the array
def frequency_Word(arr, index) :
    if index == -1 :
        return 0
    freq = 1
    i = index
    while arr[i] == arr[i + 1] :
        freq += 1
        i += 1

    return freq

if __name__ == "__main__":
    # Open specific file and read the whole data Using readlines() 
    file1 = open('myfile.txt', 'r') 
    Lines = file1.readlines() 

    # From the data, make an array
    arr = []
    for line in Lines: 
        arr.append(line.strip())

    # sort array
    quickSort(arr, 0, len(arr) - 1)

    # get input value from the console
    print ("Please input the value for searching : ")
    value = input()

    # Do Linear search
    start = time.perf_counter()
    index = linear_search(arr, value)
    end = time.perf_counter() - start
    print(index)
    print ('Linear Search Operation Time : ', end)

    # Do Binary search
    start = time.perf_counter()
    index = binary_search(arr, 0, len(arr) - 1, value)
    end = time.perf_counter() - start
    print(index)
    print ('Binary Search Operation Time : ', end)


    # Remember the start time for estimation the operating time
    start = time.perf_counter()
    #ref_arr, par_arr = sqrt_Parallel_Array(arr)
    ref_arr, par_len = get_Reference_array(len(arr))
    index = parallel_Linear_Search(arr, ref_arr, par_len, value)
    print(index)
    
    # Using the start_time, calculate the whole operating time
    end = time.perf_counter() - start
    print ('Parallel Linear Search Operation Time : ', end)


    # Remember the start time for estimation the operating time
    start = time.perf_counter()
    #ref_arr, par_arr = sqrt_Parallel_Array(arr)
    index = improve_Linear_Search(arr, value)
    print(index)
    # Using the start_time, calculate the whole operating time
    end = time.perf_counter() - start
    print ('Improve Linear Search Operation Time : ', end)

    print ("frequency_Word : ",frequency_Word(arr, index))
