# Python program for implementation of Selection 
# Sort 
import sys 
import time

# Using readlines() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 

List = []
# Strips the newline character 
for line in Lines: 
    List.append(line.strip())

length = len(List)

print ("count :", length)
  
start_time = time.perf_counter()

# Traverse through all array elements 
for i in range(length): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, length): 
        if List[min_idx] > List[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    List[i], List[min_idx] = List[min_idx], List[i] 

end_time = time.perf_counter()

ss_time = end_time - start_time
# Driver code to test above 
print ("Sorted array") 
for i in range(length): 
    print(List[i])

print ("time : Duration : SS", ss_time)
