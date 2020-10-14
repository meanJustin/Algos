import sys, os, traceback, types
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QProgressBar, QLineEdit, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from collections import deque 
import time
import math
import random
from datetime import datetime

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

class MainWindow(QWidget):
	"""
	Simple dialog that consists of a Progress Bar and a Button.
	Clicking on the button results in the start of a timer and
	updates the progress bar.
	"""
	arr = []

	def __init__(self):
		QWidget.__init__(self)
		self.setStyleSheet("color: black; background-color: #e4e5e6;")
		self.setGeometry(60,80,700,550)

		self.setWindowTitle('LINEAR SEARCH ALGORITHMs')
		
		# Element Input Label
		self.elementPattern_Label = QLabel(self)
		self.elementPattern_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.elementPattern_Label.setGeometry(150, 40, 150, 40)
		self.elementPattern_Label.setText("Search Pattern : ")

		# Element Cnt Input
		self.elementPattern_Input = QLineEdit(self)
		self.elementPattern_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.elementPattern_Input.setGeometry(350, 40, 200, 40)


		# Sorting TYPE - Bubble Sorting
		self.linearSearch_Btn = QPushButton('Linear Search', self)
		self.linearSearch_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 19px; border-radius:5px;")
		self.linearSearch_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.linearSearch_Btn.setGeometry(30, 100, 200, 40)
		self.linearSearch_Btn.clicked.connect(self.on_linearSearch_BtnClick)

		# Sorting TYPE - Merge Sort
		self.binarySearch_Btn = QPushButton('Binary Search', self)
		self.binarySearch_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.binarySearch_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.binarySearch_Btn.setGeometry(250, 100, 200, 40)
		self.binarySearch_Btn.clicked.connect(self.on_binarySearch_BtnClick)


		# Sorting TYPE - Paralle Bubble Sort
		self.blockLinearSearch_Btn = QPushButton('Block Linear Search', self)
		self.blockLinearSearch_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.blockLinearSearch_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.blockLinearSearch_Btn.setGeometry(470, 100, 200, 40)
		self.blockLinearSearch_Btn.clicked.connect(self.on_blocklinearSearch_BtnClick)

		# Sorting TYPE - Paralle Merge Sort
		self.improvedBlockLinearSearch_Btn = QPushButton('Improved block Linear', self)
		self.improvedBlockLinearSearch_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.improvedBlockLinearSearch_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.improvedBlockLinearSearch_Btn.setGeometry(250, 155, 200, 40)
		self.improvedBlockLinearSearch_Btn.clicked.connect(self.on_improvedblocklinearSearch_BtnClick)



		# Search Type Label
		self.searchAlgoType_Label = QLabel(self)
		self.searchAlgoType_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.searchAlgoType_Label.setGeometry(150, 220, 150, 40)
		self.searchAlgoType_Label.setText("Search Type : ")

		# Search Type Input
		self.searchAlgoType_Input = QLineEdit(self)
		self.searchAlgoType_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.searchAlgoType_Input.setGeometry(350, 220, 200, 40)


		# Total Execution Time Label
		self.totalExecutionTime_Label = QLabel(self)
		self.totalExecutionTime_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.totalExecutionTime_Label.setGeometry(70, 280, 230, 40)
		self.totalExecutionTime_Label.setText("Total Execution Time : ")

		# Total Execution Time Input
		self.totalExecutionTime_Input = QLineEdit(self)
		self.totalExecutionTime_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.totalExecutionTime_Input.setGeometry(350, 280, 200, 40)


		# Averg Execution Time Label
		self.avergExecutionTime_Label = QLabel(self)
		self.avergExecutionTime_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.avergExecutionTime_Label.setGeometry(70, 340, 230, 40)
		self.avergExecutionTime_Label.setText("Averg Execution Time : ")

		# Averg Execution Time Input
		self.avergExecutionTime_Input = QLineEdit(self)
		self.avergExecutionTime_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.avergExecutionTime_Input.setGeometry(350, 340, 200, 40)


		# No. of Comparisons Label
		self.noOfComparisions_Label = QLabel(self)
		self.noOfComparisions_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.noOfComparisions_Label.setGeometry(70, 400, 230, 40)
		self.noOfComparisions_Label.setText("No. of Comparisons : ")

		# No. of Comparisons Input
		self.noOfComparisions_Input = QLineEdit(self)
		self.noOfComparisions_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.noOfComparisions_Input.setGeometry(350, 400, 200, 40)



		# Frequency of Word Label
		self.frequencyOfWord_Label = QLabel(self)
		self.frequencyOfWord_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.frequencyOfWord_Label.setGeometry(70, 460, 230, 40)
		self.frequencyOfWord_Label.setText("Frequency of Word : ")

		# Frequency of Word Input
		self.frequencyOfWord_Input = QLineEdit(self)
		self.frequencyOfWord_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.frequencyOfWord_Input.setGeometry(350, 460, 200, 40)

		self.getFileStrData()
		self.arr.sort()

		self.show()

	def isString(self, value) :
		try : 
			str(value)
			return True
		except :
			return False

	def getSearchPattern(self) :
		if len(str(self.elementPattern_Input.text())) :
			return str(self.elementPattern_Input.text())
		return None


	def messageBox(self) :
		msgBox = QMessageBox.question(self, 'Warning', "Please Input the Search Pattern!")

	def getFileStrData(self) :
		# Using readlines() 
		while 1:
			try :
				with open('GutenbergWordsFile.txt', 'r') as file_read :
					lines = file_read.readlines()

				self.arr = []
				for line in lines :
					self.arr.append(line.strip())
				return 
			except IOError as X :
				print  ("couldn't read this file on this spot")

	def log_Result(self, Searching_Type, execution_Time, average, noOfComparision, frequency) :
		while 1 :
			try :
				with open('log.txt', 'a', encoding = 'utf-8') as file_object :
					pattern = str(self.elementPattern_Input.text())
					now = datetime.now()
					current_time = now.strftime("%d/%m/%Y %H:%M:%S")
					str_cur_time = "    Current Date Time ::  " + current_time + ":::"
					file_object.write(str_cur_time + Searching_Type + ":: Searching Pattern :: " + pattern + " :: Execution Time : " + execution_Time + " :: Average Execution Time : " + average + " :: No.Comparisons : " + noOfComparision + " :: frequency : " + frequency + "\n")
				return
			except IOError as X :
				print  ("couldn't read this file on this spot")

	# Do linear search with the value and array
	def on_linearSearch_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return

		sum_execution_time = 0
		for i in range(10):
			start_time = time.perf_counter()
		    
			index = linear_search( self.arr, pattern)
			freq = frequency_Word( self.arr, index)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 10) * 1000000) / 1000) + "MS"
		self.searchAlgoType_Input.setText("Linear Search")
		self.totalExecutionTime_Input.setText(exe_time)
		self.avergExecutionTime_Input.setText(averg_time)
		self.noOfComparisions_Input.setText(str(index))
		self.frequencyOfWord_Input.setText(str(freq))

		self.log_Result("Linear Search", str(exe_time), str(averg_time), str(index), str(freq))


	# Do binary search with the value and array
	def on_binarySearch_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return

		sum_execution_time = 0
		for i in range(10):
			start_time = time.perf_counter()
		    
			index = binary_search( self.arr, 0, len(self.arr) - 1 , pattern)
			freq = frequency_Word( self.arr, index)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 10) * 1000000) / 1000) + "MS"
		self.searchAlgoType_Input.setText("Binary Search")
		self.totalExecutionTime_Input.setText(exe_time)
		self.avergExecutionTime_Input.setText(averg_time)
		self.noOfComparisions_Input.setText(str(index))
		self.frequencyOfWord_Input.setText(str(freq))

		self.log_Result("Linear Search", str(exe_time), str(averg_time), str(index), str(freq))


	# Do block linear search with the value and array
	def on_blocklinearSearch_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return

		sum_execution_time = 0
		for i in range(10):
			start_time = time.perf_counter()
		    
			ref_arr, par_len = get_Reference_array(len(self.arr))
			index = parallel_Linear_Search(self.arr, ref_arr, par_len, pattern)
			freq = frequency_Word( self.arr, index)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 10) * 1000000) / 1000) + "MS"
		self.searchAlgoType_Input.setText("Block Linear Search")
		self.totalExecutionTime_Input.setText(exe_time)
		self.avergExecutionTime_Input.setText(averg_time)
		self.noOfComparisions_Input.setText(str(index))
		self.frequencyOfWord_Input.setText(str(freq))

		self.log_Result("Linear Search", str(exe_time), str(averg_time), str(index), str(freq))

	# Do improved block linear search with the value and array
	def on_improvedblocklinearSearch_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return

		sum_execution_time = 0
		for i in range(5):
			start_time = time.perf_counter()
		    
			index = improve_Linear_Search( self.arr, pattern)
			freq = frequency_Word( self.arr, index)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 5) * 1000000) / 1000) + "MS"
		self.searchAlgoType_Input.setText("Improved Block Linear")
		self.totalExecutionTime_Input.setText(exe_time)
		self.avergExecutionTime_Input.setText(averg_time)
		self.noOfComparisions_Input.setText(str(index))
		self.frequencyOfWord_Input.setText(str(freq))

		self.log_Result("Linear Search", str(exe_time), str(averg_time), str(index), str(freq))





if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = MainWindow()
	screen.show()
	sys.exit(app.exec_())
