# Python program for implementation of Selection 
# Sort 
import sys 
import time
from collections import deque 

# Using readlines() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 

List = []
# Strips the newline character 
for line in Lines: 
    List.append(line.strip())

length = len(List)

start_time = time.perf_counter()

stack1 = []
stack2 = []

# Traverse through all array elements 
for i in range(length - 1, 0, -1): 
    max_idx = i 
    for j in range(i - 1, 0, -1): 
        if List[max_idx] < List[j]: 
            max_idx = j 
            stack1.append(max_idx)
            stack2.append(List[max_idx])

    List[i], List[max_idx] = List[max_idx], List[i]
    if len(stack1) :
        stack1.pop()
        stack2.pop()

    while len(stack1) and i > 0:
        i -= 1
        location = stack1.pop()
        max_idx = location
        value = stack2.pop()
        swapped = False

        if i > 1 :
            for n in range(location - 1, 0, -1) :
                swapped = True
                if List[n] > value :
                    max_idx = n
                    stack1.append(max_idx)
                    value = List[max_idx]
                    stack2.append(value)
        if swapped :
            List[i], List[max_idx] = List[max_idx], List[i] 
            if len(stack1) :
                stack1.pop()
                stack2.pop()
        else :
            i += 1

end_time = time.perf_counter()
  
#Driver code to test above 
print ("Sorted array") 
for i in range(length): 
    print(List[i])

print ("time : Duration : SS", end_time - start_time)
