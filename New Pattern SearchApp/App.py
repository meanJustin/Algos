import sys, os, traceback, types
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QFrame, QPlainTextEdit, QLineEdit, QMessageBox, QSplitter
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from collections import deque 
import time
import math
import random
from datetime import datetime

# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# Python program for KMP Algorithm 
def KMP_Search(pat, txt): 
	M = len(pat) 
	N = len(txt) 
	cnt = 0
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
			cnt += 1
			j = lps[j-1] 

	    # mismatch after j matches 
		elif i < N and pat[j] != txt[i]: 
			# Do not match lps[0..lps[j-1]] characters, 
			# they will match anyway 
			if j != 0 :
				j = lps[j-1] 
			else: 
				i += 1
	return cnt
  
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

    cnt = 0
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
        	cnt += 1

    return cnt

# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
 
# d is the number of characters in the input alphabet
# pat  -> pattern
# txt  -> text
# q    -> A prime number
 
def rabin_Karp_Search(pat, txt, q):
	cnt = 0
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
	        	cnt += 1

	    # Calculate hash value for next window of text: Remove
	    # leading digit, add trailing digit
	    if i < N-M:
	        t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

	        # We might get negative values of t, converting it to
	        # positive
	        if t < 0:
	            t = t+q
	return cnt
 
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

	cnt = 0
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
			cnt += 1
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

	return cnt

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
	return len(index_arr)	# return the requency of founds


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

class MainWindow(QWidget):
	"""
	Simple dialog that consists of a Progress Bar and a Button.
	Clicking on the button results in the start of a timer and
	updates the progress bar.
	"""
	total_Str = ''
	pat_arr = []

	def __init__(self):
		QWidget.__init__(self)

		self.setStyleSheet("color: black; background-color: #e4e5e6;")
		self.setGeometry(60,80,770,550)

		self.setWindowTitle('LINEAR SEARCH ALGORITHMs')
		

		# Top title Label
		self.top_25_Label = QLabel(self)
		self.top_25_Label.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.top_25_Label.setGeometry(-2, -2, 400, 40)
		self.top_25_Label.setText("Search all 25 noise words at once : ")

		# Search Pattern Label
		self.elementPattern_Label = QLabel(self)
		self.elementPattern_Label.setStyleSheet("color: black; font-size : 19px; ")
		self.elementPattern_Label.setGeometry(450, 40, 300, 30)
		self.elementPattern_Label.setText("Search Patterns from StopWords.txt ")

		# Searching TYPE - Naive Search Algorithm
		self.naiveSearch_25_Btn = QPushButton('Naive Search', self)
		self.naiveSearch_25_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.naiveSearch_25_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.naiveSearch_25_Btn.setGeometry(10, 100, 180, 40)
		self.naiveSearch_25_Btn.clicked.connect(self.on_naiveSearch_25_BtnClick)


		# Searching TYPE - Rabin Karp Search
		self.rabinKarp_25_Btn = QPushButton('Rabin Karp Search', self)
		self.rabinKarp_25_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.rabinKarp_25_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.rabinKarp_25_Btn.setGeometry(200, 100, 180, 40)
		self.rabinKarp_25_Btn.clicked.connect(self.on_rabinKarp_25_BtnClick)



		# Searching TYPE - Boyer moore Search
		self.boyerMoore_25_Btn = QPushButton('Boyer Moore Search', self)
		self.boyerMoore_25_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.boyerMoore_25_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.boyerMoore_25_Btn.setGeometry(390, 100, 180, 40)
		self.boyerMoore_25_Btn.clicked.connect(self.on_boyerMoore_25_BtnClick)


		# Searching TYPE - KMP Search
		self.kmp_25_Btn = QPushButton('KMP Search', self)
		self.kmp_25_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.kmp_25_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.kmp_25_Btn.setGeometry(580, 100, 180, 40)
		self.kmp_25_Btn.clicked.connect(self.on_kmp_25_BtnClick)


		# Searching TYPE - New Pattern Search aglo
		self.newPattern_25_Btn = QPushButton('New Pattern Search Alogrithm', self)
		self.newPattern_25_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.newPattern_25_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.newPattern_25_Btn.setGeometry(280, 150, 250, 40)
		self.newPattern_25_Btn.clicked.connect(self.on_newPattern_25_BtnClick)

		
		# Execution Time Label
		self.ExecutionTime_25_Label = QLabel(self)
		self.ExecutionTime_25_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.ExecutionTime_25_Label.setGeometry(150, 210, 200, 40)
		self.ExecutionTime_25_Label.setText("Execution Time : ")


		# Execution Time Input
		self.ExecutionTime_25_Input = QLineEdit(self)
		self.ExecutionTime_25_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.ExecutionTime_25_Input.setGeometry(370, 210, 200, 40)



		# Search Pattern Input
		self.spliteLabel = QLabel(self)
		self.spliteLabel.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.spliteLabel.setGeometry(-2, 270, 800, 5)



		# Beginning of second part

		# Top title Label
		self.top_1_Label = QLabel(self)
		self.top_1_Label.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.top_1_Label.setGeometry(-2, 273, 400, 40)
		self.top_1_Label.setText("Search for a certain noise word : ")

		# Search Pattern Label
		self.elementPattern_Label = QLabel(self)
		self.elementPattern_Label.setStyleSheet("color: black; font-size : 19px; ")
		self.elementPattern_Label.setGeometry(450, 300, 150, 30)
		self.elementPattern_Label.setText("Search Pattern : ")

		# Search Pattern Input
		self.elementPattern_Input = QLineEdit(self)
		self.elementPattern_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.elementPattern_Input.setGeometry(600, 300, 150, 30)


		# Searching TYPE - Naive Search Algorithm
		self.naiveSearch_Btn = QPushButton('Naive Search', self)
		self.naiveSearch_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.naiveSearch_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.naiveSearch_Btn.setGeometry(10, 360, 180, 40)
		self.naiveSearch_Btn.clicked.connect(self.naiveSearch_BtnClick)


		# Searching TYPE - Rabin Karp Search
		self.rabinKarp_Btn = QPushButton('Rabin Karp Search', self)
		self.rabinKarp_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.rabinKarp_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.rabinKarp_Btn.setGeometry(200, 360, 180, 40)
		self.rabinKarp_Btn.clicked.connect(self.rabinKarp_BtnClick)



		# Searching TYPE - Boyer moore Search
		self.boyerMoore_Btn = QPushButton('Boyer Moore Search', self)
		self.boyerMoore_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.boyerMoore_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.boyerMoore_Btn.setGeometry(390, 360, 180, 40)
		self.boyerMoore_Btn.clicked.connect(self.boyerMoore_BtnClick)


		# Searching TYPE - KMP Search
		self.kmp_Btn = QPushButton('KMP Search', self)
		self.kmp_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.kmp_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.kmp_Btn.setGeometry(580, 360, 180, 40)
		self.kmp_Btn.clicked.connect(self.kmp_BtnClick)


		# Searching TYPE - New Pattern Search aglo
		self.newPattern_Btn = QPushButton('New Pattern Search Alogrithm', self)
		self.newPattern_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 17px; border-radius:5px;")
		self.newPattern_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.newPattern_Btn.setGeometry(280, 410, 250, 40)
		self.newPattern_Btn.clicked.connect(self.newPattern_BtnClick)

		
		# Execution Time Label
		self.demo_ExecutionTime_Label = QLabel(self)
		self.demo_ExecutionTime_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.demo_ExecutionTime_Label.setGeometry(50, 470, 200, 40)
		self.demo_ExecutionTime_Label.setText("Execution Time : ")


		# Execution Time Input
		self.demo_ExecutionTime_Input = QLineEdit(self)
		self.demo_ExecutionTime_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.demo_ExecutionTime_Input.setGeometry(250, 470, 200, 40)


		# Execution Time Label
		self.demo_frequencyOfWord_Label = QLabel(self)
		self.demo_frequencyOfWord_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.demo_frequencyOfWord_Label.setGeometry(500, 470, 120, 40)
		self.demo_frequencyOfWord_Label.setText("Frequency : ")


		# Execution Time Input
		self.demo_frequencyOfWord_Input = QLineEdit(self)
		self.demo_frequencyOfWord_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.demo_frequencyOfWord_Input.setGeometry(650, 470, 80, 40)

		self.getFileStrData()
		self.getPatternsFromFile()
		self.show()

	def isString(self, value) :
		try : 
			str(value)
			return True
		except :
			return False

	def getSearchPattern(self) :
		pattern = self.elementPattern_Input.text()
		length = len(pattern)
		for i in range(length) :
			if pattern[i] <= 'a' or pattern[i] >= 'z':
				return None
		if len(str(self.elementPattern_Input.text())) :
			return str(self.elementPattern_Input.text())
		return None


	def messageBox(self) :
		msgBox = QMessageBox.question(self, 'Warning', "Please Input the Search Pattern!")


	# get Pattern Array from file
	def getPatternsFromFile(self) :

		self.pat_arr = []
		file1 = open('stopwords.txt', 'r') 
		lines = file1.readlines() 

		# Looping line by line and make the total_str
		for line in lines :
			self.pat_arr.append(line.strip())
			if len(self.pat_arr) == 25 :
				return


	def getFileStrData(self) :
		# Using readlines() 
		while 1:
			try :
				with open('Random 5000 words.txt', 'r') as file_read :
					Lines = file_read.readlines()
				
				# Initial the total string as ''
				self.total_Str = ''

				# Looping line by line and make the total_str
				for line in Lines :
				    self.total_Str += line.strip()
				return
			except IOError as X :
				print  ("couldn't read this file on this spot")



	def log_Result(self, Searching_Type, execution_Time, freq, is_pattern) :
		while 1 :
			try :
				with open('log.txt', 'a', encoding = 'utf-8') as file_object :
					if is_pattern :
						pattern = str(self.elementPattern_Input.text()) + "   :: Frequency ::  " + str(freq)
					else :
						pattern = "Stopwords.txt"
					now = datetime.now()
					current_time = now.strftime("%d/%m/%Y %H:%M:%S")
					str_cur_time = "    Current Date Time ::  " + current_time + ":::"
					file_object.write(str_cur_time + Searching_Type + ":: Searching Pattern :: " + pattern + " :: Execution Time : ")
				return
			except IOError as X :
				print  ("couldn't read this file on this spot")

	# Do block linear search length
	def naiveSearch_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return
		
		start_time = time.perf_counter()
		cnt = naive_Search(pattern, self.total_Str)
		end_time = time.perf_counter()
		sum_execution_time = end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.demo_ExecutionTime_Input.setText(exe_time)
		self.demo_frequencyOfWord_Input.setText(str(cnt))
		self.log_Result("Naive Search Algorithm", exe_time, cnt,True)

	# Do Rabin Karp search length
	def rabinKarp_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return
		
		start_time = time.perf_counter()
		cnt = rabin_Karp_Search(pattern, self.total_Str, 101)
		end_time = time.perf_counter()
		sum_execution_time = end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.demo_ExecutionTime_Input.setText(exe_time)
		self.demo_frequencyOfWord_Input.setText(str(cnt))
		self.log_Result("Rabin Karp Search Algorithm", exe_time, cnt,True)

	# Do Boyer Moore search length
	def boyerMoore_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return
		
		start_time = time.perf_counter()
		cnt = boyer_Moore_Search(pattern, self.total_Str)
		end_time = time.perf_counter()
		sum_execution_time = end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.demo_ExecutionTime_Input.setText(exe_time)
		self.demo_frequencyOfWord_Input.setText(str(cnt))
		self.log_Result("BoyerMoore Search Algorithm", exe_time, cnt,True)

	# Do KMP search length
	def kmp_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return
		
		start_time = time.perf_counter()
		cnt = KMP_Search(pattern, self.total_Str)
		end_time = time.perf_counter()
		sum_execution_time = end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.demo_ExecutionTime_Input.setText(exe_time)
		self.demo_frequencyOfWord_Input.setText(str(cnt))
		self.log_Result("KMP Search Algorithm", exe_time, cnt,True)

	# Do New pattern Btn search length
	def newPattern_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return
		
		start_time = time.perf_counter()
		str_arr = getArrayFromFile(self.total_Str)
		cnt = new_Pattern_String_Search(pattern, str_arr)
		end_time = time.perf_counter()

		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.demo_ExecutionTime_Input.setText(exe_time)
		self.demo_frequencyOfWord_Input.setText(str(cnt))
		self.log_Result("New Pattern Search Search Algorithm", exe_time, cnt,True)


	# Do 25 times naive Search
	def on_naiveSearch_25_BtnClick(self):
		start_time = time.perf_counter()
		for i in range(25) :
			cnt = naive_Search(self.pat_arr[i], self.total_Str)
		end_time = time.perf_counter()


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.ExecutionTime_25_Input.setText(exe_time)
		self.log_Result("25 - Naive Search Algorithm", exe_time, cnt,False)

	# Do 25 times naive Search
	def on_rabinKarp_25_BtnClick(self):
		start_time = time.perf_counter() 
		for i in range(25) :
			cnt = rabin_Karp_Search(self.pat_arr[i], self.total_Str, 101)
		end_time = time.perf_counter()


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.ExecutionTime_25_Input.setText(exe_time)
		self.log_Result("25 - Rabin Karp Search Algorithm", exe_time, cnt,False)

	# Do 25 times naive Search
	def on_boyerMoore_25_BtnClick(self):
		start_time = time.perf_counter()
		for i in range(25) :
			cnt = boyer_Moore_Search(self.pat_arr[i], self.total_Str)
		end_time = time.perf_counter()


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.ExecutionTime_25_Input.setText(exe_time)
		self.log_Result("25 - Boyer Moore Search Algorithm", exe_time, cnt,False)

	# Do 25 times naive Search
	def on_kmp_25_BtnClick(self):
		start_time = time.perf_counter()
		for i in range(25) :
			cnt = KMP_Search(self.pat_arr[i], self.total_Str)
		end_time = time.perf_counter()


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.ExecutionTime_25_Input.setText(exe_time)
		self.log_Result("25 - KMP Search Algorithm", exe_time, cnt,False)

	# Do 25 times naive Search
	def on_newPattern_25_BtnClick(self):
		start_time = time.perf_counter()
		str_arr = getArrayFromFile(self.total_Str)
		for i in range(25) :
			cnt = new_Pattern_String_Search(self.pat_arr[i], str_arr)
		end_time = time.perf_counter()


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.ExecutionTime_25_Input.setText(exe_time)
		self.log_Result("25 - New Pattern Search Algorithm", exe_time, cnt,False)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = MainWindow()
	screen.show()
	sys.exit(app.exec_())
