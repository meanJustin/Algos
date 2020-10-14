# Python program for implementation of Selection 
# Sort 
import sys 
import time
from collections import deque 
import threading


def smallElementThread(List) :
    Min = 0
    location = 0
    value = 0
    length = len(List)
    mid = int(length / 2)

    stack1 = deque()
    stack2 = deque()

    for i in range(mid) :
        Min = i
        for j in range(i + 1, length) :
            if List[j] < List[Min] :
                Min = j
                stack1.append(Min)
                value = List[Min]
                stack2.append(value)

        List[i], List[Min] = List[Min], List[i]
        if len(stack1) :
            stack1.pop()
            stack2.pop()

        while len(stack1) != 0 and i <= mid:
            i += 1
            location = stack1.pop()
            Min = location
            value = stack2.pop()
            swapped = False

            temp = 0
            if i != 1 :
                temp = i - 1
            for n in range(location, temp) :
                swapped = True
                if List[n] < value :
                    Min = n
                    stack1.append(Min)
                    value = List[Min]
                    stack2.append(value)

            if swapped :
                List[i], List[Min] = List[Min], List[i]
                if len(stack1) :
                    stack1.pop()
                    stack2.pop()
            else :
                i -= 1

def largeElementThread(List) :
    length = len(List)
    mid = int(length / 2)

    stack1 = deque()
    stack2 = deque()

    for i in range(mid, length) :
        Max = i
        for j in range(i + 1, length) :
            if List[j] < List[Max] :
                Max = j
                stack1.append(Max)
                value = List[Max]
                stack2.append(value)

        List[i], List[Max] = List[Max], List[i]

        if len(stack1) :
            stack1.pop()
            stack2.pop()

        while len(stack1) != 0 and i >= mid:
            i -= 1
            location = stack1.pop()
            Max = location
            value = stack2.pop()
            swapped = False

            temp = 0
            if i != 1 :
                temp = i - 1
            for n in range(location, temp) :
                swapped = True
                if List[n] < value :
                    Max = n
                    stack1.append(Max)
                    value = List[Max]
                    stack2.append(value)
            if swapped :
                List[i], List[Max] = List[Max], List[i]
                if len(stack1) :
                    stack1.pop()
                    stack2.pop()
            else :
                i += 1
    
while 1:
    try :
        with open('myfile.txt', 'r') as file_read :
            lines = file_read.readlines()
        list_small = []
        for line in lines :
            list_small.append(line.strip())
        break
    except IOError as X :
        print  ("couldn't read this file on this spot")

print ("Count of Array is : ", len(list_small))

# Create two threads as follows
start_time = time.perf_counter()

try:
    threading.Thread(smallElementThread( list_small ))
    threading.Thread(largeElementThread( list_small ))
except:
    print ("Error: unable to start thread")

end_time = time.perf_counter()
  
# Driver code to test above 
cnt = len(list_small)

for i in range(cnt) :
    print (list_small[i])

print ("time : Duration : SS", end_time-start_time)

