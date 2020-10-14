import string
import random
import time
import math
import sys


# Build the parallel array which reflect the length of every element of the array
def parallel_Array(arr) :
    par_arr = []                    # Define parallel array
    length = len(arr)               # Define a length value which reflect the length of array
    for i in range(length) :        # Doing loop and make the parallel array
        par_arr.append(len(arr[i]))

    return par_arr                  # Return the made parallel array



# Build ten arrays which place in 3-12 length strings
# Each of them could has 256(maximum) string on the array
def build_3_12_Array(arr) :
    
    par_arr = {}            # define parallel array
    length = len(arr)       # define the value which reflect the length of the array

    # iteration of the whole array to build the parallel array
    for i in range(length) :

        temp_len = len(arr[i])              #Length of current string
        if temp_len < 3 or temp_len > 12 :  # If the length is out of 3-12 then skip this one
            continue
        if not temp_len in par_arr :        # If this length array is not define in par_arr then create one
            par_arr[temp_len] = []
        if len(par_arr[temp_len]) >= 256 :  # If this length array has more than 256 then skip one
            continue
        par_arr[temp_len].append({'value' : arr[i], 'index' : i})   # Add this string add onto the array

    return par_arr              # return the par_arr that we create



# Search on Parallel Array we create above
# recognize the length of input value and search on this length array
def search_On_Parallel_Array(par_arr, pattern) :
    
    pattern_len = len(pattern)              # Define the pattern_len which reflect the length of pattern

    # if the length of pattern is out of 3-12 then return -1
    if pattern_len < 3 or pattern_len > 12 :
        return -1

    # Looping the array of Par_arr for seeking the pattern
    for i in range(len(par_arr[pattern_len])) :
        # If find something equal then return the index value of that
        if pattern == par_arr[pattern_len][i]['value'] :
            return par_arr[pattern_len][i]['index']

    return -1                               # If not then return -1


# Generate the random string
def generate_RandomString() :
    # Generate the length in random
    ran_length = random.randint(3,12)
    letters = string.ascii_lowercase

    # Generate the string in random
    ran_str = ''.join(random.choice(letters) for i in range(ran_length))
    return ran_str


# Search 256 times for getting the best result 
def search_256(par_arr_3_12) :

    exe_time = []               # define execution time array
    for i in range(3,13) :
        exe_time.append({'sum' : 0, 'count' : 0})

    # Generate the random str 256 times and searching on this par_arr and log them all.
    for i in range(256) :
        # Generate random string
        ran_str = generate_RandomString()
        print ("Generated String : ", ran_str)

        # Start the searching
        start = time.perf_counter()
        print (search_On_Parallel_Array (par_arr_3_12, ran_str))
        dur_time = time.perf_counter() - start

        # save the execution time
        exe_time[len(ran_str) - 3]['sum'] += dur_time
        exe_time[len(ran_str) - 3]['count'] += 1


    # get average execution time from all of those
    for i in range(3,13) :
        exe_time[i-3] = exe_time[i-3]['sum'] / exe_time[i-3]['count']
        print (exe_time[i - 3])

    best_length = exe_time.index(min(exe_time)) + 3
    print ("The best length is :   ", best_length)
    return best_length


# Make reference array
def get_Reference_array (arr, best_length) :
    ref_arr = [0]           # define reference array
    length = len(arr)       # define the value which reflect the length of array
    i = 1                   # define temp value for looping

    # making a reference array
    while i < length :
        if len(arr[i]) == best_length :
            ref_arr.append(i)
        i += 1

    return ref_arr




# Do parallel linear search
# It has ref_arr, par_arr and arr as parameter and also value
# the value is what we have to find in this array

def Block_Linear_Search_Using_Reference_Block_First(arr, ref_arr, pattern) :
    # if the pattern is greater then maximum pattern of array or 
    # less than the minimun pattern of the array then return false 
    if pattern < arr[0] and pattern > arr[len(arr) - 1]:
        return -1

    #1. Do linear search in the reference block if match found exit otherwise
    for i in range(len(ref_arr)) :

        # if there is the pattern in the reference array
        # then return the True and Index value
        if arr[ref_arr[i]] == pattern :
            return ref_arr[i]

        # Stop searching when an element in the reference block is larger
        # than the input data, then break 
        if arr[ref_arr[i]] > pattern :
            break;


    # In the main array continue the linear search on the block referenced only. 
    # If match found or return not found and exit.

    # From the break index, get the block of last element compared
    # that was less than the input element.    
    ref_index = ref_arr[i - 1]
    length = len(arr)

    for i in range(ref_index, length) :
        if arr[i] == pattern :
            return i

    # if there is not result then return false and null index
    return -1


# Block Linear Search Of Length String
def Block_Linear_Search_Of_Length_String(arr, ref_arr, pattern, par_arr) :
    # if the pattern is greater then maximum pattern of array or 
    # less than the minimun pattern of the array then return false 
    if pattern < arr[0] and pattern > arr[len(arr) - 1]:
        return -1

    len_pattern = len(pattern)      # define a valuable which reflects the length of string

    # Do linear search in the reference block if match found exit otherwise
    for i in range(len(ref_arr)) :
        # if there is the pattern in the reference array
        # then return the True and Index value
        if len_pattern == len(arr[ref_arr[i]]) and arr[ref_arr[i]] == pattern :
            return ref_arr[i]

        # 2.Stop searching when an element in the reference block is larger
        # than the input data, then break 
        if arr[ref_arr[i]] > pattern :
            break;

    # In the main array continue the linear search on the block referenced only. 
    # If match found or return not found and exit.

    # From the break index, get the block of last element compared
    # that was less than the input element.    
    ref_index = ref_arr[i - 1]
    length = len(arr)

    for i in range(ref_index, length) :
        if len_pattern == par_arr[i] and arr[i] == pattern :
            return i

    # if there is not result then return false and null index
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
    arr.sort()

    # get length array from the original array
    length_arr = parallel_Array(arr)


    # Building the Parallel Array of 3-12
    par_arr_3_12 = build_3_12_Array (arr)
    for i in par_arr_3_12 :
        print ("===============================", i)
        print (par_arr_3_12[i])


    # Search 256 times
    best_length = search_256(par_arr_3_12)



    # get input value from the console
    print ("Please input the pattern for searching : ")
    pattern = input()

    # Do Block Linear Search using reference block first
    start = time.perf_counter()

    ref_arr = get_Reference_array(arr, best_length)
    index = Block_Linear_Search_Using_Reference_Block_First(arr, ref_arr, pattern)
    end = time.perf_counter() - start
    print(index, arr[index])
    print ('Linear Search Operation Time : ', end)


    # Do Block Linear Search using reference block first
    start = time.perf_counter()

    ref_arr = get_Reference_array(arr, best_length)
    index = Block_Linear_Search_Of_Length_String(arr, ref_arr, pattern, length_arr)
    end = time.perf_counter() - start
    print(index, arr[index])
    print ('Linear Search Operation Time : ', end)
    