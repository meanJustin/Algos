import random
import time
import math
import sys

# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# Python program for KMP Algorithm 
def KMP_Search(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            print ("Found pattern at index " + str(i-j)) 
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1


# https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
# Python3 program for Naive Pattern 
# Searching algorithm 
def naive_Search(pat, txt): 
    M = len(pat) 
    N = len(txt) 

  
    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
        j = 0
          
        # For current index i, check  
        # for pattern match */ 
        while(j < M): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1
  
        if (j == M):  
            print("Pattern found at index ", i) 

# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
 
# d is the number of characters in the input alphabet
# pat  -> pattern
# txt  -> text
# q    -> A prime number
 
def rabin_Karp_Search(pat, txt, q):
    d = 256
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
 
    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q
 
    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
 
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else: j+=1
 
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print ("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
 
            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
 
# https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
# Python3 Program for Bad Character Heuristic 
# of Boyer Moore String Matching Algorithm  
  
  
def badCharHeuristic(string, size): 
    ''' 
    The preprocessing function for 
    Boyer Moore's bad character heuristic 
    '''
  
    # Initialize all occurrence as -1 
    NO_OF_CHARS = 256
    badChar = [-1]*NO_OF_CHARS 
  
    # Fill the actual value of last occurrence 
    for i in range(size): 
        badChar[ord(string[i])] = i; 
  
    # retun initialized list 
    return badChar 
  
def boyer_Moore_Search(pat, txt): 
    ''' 
    A pattern searching function that uses Bad Character 
    Heuristic of Boyer Moore Algorithm 
    '''
    m = len(pat) 
    n = len(txt) 
  
    # create the bad character list by calling  
    # the preprocessing function badCharHeuristic() 
    # for given pattern 
    badChar = badCharHeuristic(pat, m)  
  
    # s is shift of the pattern with respect to text 
    s = 0
    while(s <= n-m): 
        j = m-1
  
        # Keep reducing index j of pattern while  
        # characters of pattern and text are matching 
        # at this shift s 
        while j>=0 and pat[j] == txt[s+j]: 
            j -= 1
  
        # If the pattern is present at current shift,  
        # then index j will become -1 after the above loop 
        if j<0: 
            print("Pattern occur at shift = {}".format(s)) 
  
            '''     
                Shift the pattern so that the next character in text 
                      aligns with the last occurrence of it in pattern. 
                The condition s+m < n is necessary for the case when 
                   pattern occurs at the end of text 
               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1) 
        else: 
            ''' 
               Shift the pattern so that the bad character in text 
               aligns with the last occurrence of it in pattern. The 
               max function is used to make sure that we get a positive 
               shift. We may get a negative shift if the last occurrence 
               of bad character in pattern is on the right side of the 
               current character. 
            '''
            s += max(1, j-badChar[ord(txt[s+j])]) 



# This is the new pattern String search that we are gonna build

def new_Pattern_String_Search(pattern, str_arr) :
    pat_arr = []                        # Pattern ascii code array
    pat_len = len(pattern)              # Length of pattern

    # Initialize the pat_arr
    for i in range(pat_len) :
        pat_arr.append(ord(pattern[i]) - 96)

    space_cnt = len(str_arr[0])         # get the all count of space
    index_arr = []                      # Initalize the found index array

    # Looping all indexes
    for i in range(space_cnt) :

        # The word after space's length is different from pattern and skip this loop
        if i != space_cnt - 1 and str_arr[0][i + 1] - str_arr[0][i] != pat_len + 1:
            continue

        pat_index = 0                   # Set temp_index for looping
        temp = str_arr[0][i] + 1

        # Looping until next pattern value is exist on the array
        while temp in str_arr[pat_arr[pat_index]] :
            temp += 1
            pat_index += 1

            if pat_len == pat_index :
                index_arr.append(str_arr[0][i] + 1)
                break
    print(index_arr)


# Read the whole file and return the filedata as one string
def getStringFromFile() :
    # "Open the random 5000 words.txt and make the whole array
    file1 = open('Random 5000 words.txt', 'r') 
    Lines = file1.readlines() 

    # Initial the total string as ''
    total_Str = ''

    # Looping line by line and make the total_str
    for line in Lines :
        total_Str += line.strip()

    #Return the total_str
    return total_Str


    
# get Array from file
def getArrayFromFile(total_Str) :

    str_arr = []
    for i in range(27) :
        str_arr.append([])
    total_length = len(total_Str)

    for i in range(total_length) :
        if total_Str[i] == ' ' :
            str_arr[0].append(i)
        else :
            str_arr[ord(total_Str[i]) - ord('a') + 1].append(i)

    return str_arr



# get Array from file
def getPatternsFromFile() :

    str_arr = []
    file1 = open('stopwords.txt', 'r') 
    lines = file1.readlines() 

    # Looping line by line and make the total_str
    for line in lines :
        str_arr.append(line.strip())

    return str_arr


if __name__ == "__main__":
    
    # Do Regular Insertion sort
    total_Str = getStringFromFile()
    start_time = time.perf_counter()
    str_arr = getArrayFromFile(total_Str)
    new_Pattern_String_Search("has", str_arr)
    dur_time = time.perf_counter() - start_time
    print ("New Patter Search : ", dur_time)
    
    # As you can see this new pattern search is only seeking the exact word while the others are seeking the pattern
    print (total_Str[9182 : 9200])

    start_time = time.perf_counter()
    KMP_Search("has",total_Str)
    dur_time = time.perf_counter() - start_time
    print ("KMP search : ", dur_time)

    start_time = time.perf_counter()
    naive_Search("has",total_Str)
    dur_time = time.perf_counter() - start_time
    print ("Naive search : ", dur_time)


    start_time = time.perf_counter()
    rabin_Karp_Search("has",total_Str,101)
    dur_time = time.perf_counter() - start_time
    print ("Rabin Karp search : ", dur_time)


    start_time = time.perf_counter()
    boyer_Moore_Search("has",total_Str)
    dur_time = time.perf_counter() - start_time
    print ("Boyer Moore search : ", dur_time)
    # #Driver code to test above 


    print (getPatternsFromFile())