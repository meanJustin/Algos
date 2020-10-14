import sys, os, traceback, types
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QCursor

from collections import deque 
import time
import math
import random
from datetime import datetime

BEST_RESULT = 5		# Define best result as 5

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



# Do block linear search using reference block first
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



class MainWindow(QWidget):
	"""
	Simple dialog that consists of a Progress Bar and a Button.
	Clicking on the button results in the start of a timer and
	updates the progress bar.
	"""
	arr = []
	element_cnt = 1000

	def __init__(self):
		QWidget.__init__(self)
		self.setStyleSheet("color: black; background-color: #e4e5e6;")
		self.setGeometry(60,80,700,450)

		self.setWindowTitle('STRING LENGTH BASED ON SEARCHING ALGORITHMs')
		
		# Searching Pattern Label
		self.elementPattern_Label = QLabel(self)
		self.elementPattern_Label.setStyleSheet("color: black; font-size : 19px; ")
		self.elementPattern_Label.setGeometry(60, 40, 150, 40)
		self.elementPattern_Label.setText("Search Pattern : ")

		# Searching Pattern Input
		self.elementPattern_Input = QLineEdit(self)
		self.elementPattern_Input.setStyleSheet("color: black; font-size : 19px; border : 2px solid black")
		self.elementPattern_Input.setGeometry(250, 40, 250, 40)


		# Radio Buttons
		self.radioButton_1k = QtWidgets.QRadioButton(self) 
		self.radioButton_1k.setText("1K")
		self.radioButton_1k.setGeometry(QtCore.QRect(100, 100, 95, 40)) 
		self.radioButton_1k.setStyleSheet("font-size : 19px;")
		self.radioButton_1k.setChecked(True)
		# adding signal and slot  
		self.radioButton_1k.toggled.connect(self.selected_1k)


		# Radio Buttons
		self.radioButton_2k = QtWidgets.QRadioButton(self) 
		self.radioButton_2k.setText("2K")
		self.radioButton_2k.setGeometry(QtCore.QRect(200, 100, 95, 40)) 
		self.radioButton_2k.setStyleSheet("font-size : 19px;")
		# adding signal and slot  
		self.radioButton_2k.toggled.connect(self.selected_2k)



		# Radio Buttons
		self.radioButton_4k = QtWidgets.QRadioButton(self) 
		self.radioButton_4k.setText("4K")
		self.radioButton_4k.setGeometry(QtCore.QRect(300, 100, 95, 40)) 
		self.radioButton_4k.setStyleSheet("font-size : 19px;")
		# adding signal and slot  
		self.radioButton_4k.toggled.connect(self.selected_4k)


		# Radio Buttons
		self.radioButton_8k = QtWidgets.QRadioButton(self) 
		self.radioButton_8k.setText("8K")
		self.radioButton_8k.setGeometry(QtCore.QRect(400, 100, 95, 40)) 
		self.radioButton_8k.setStyleSheet("font-size : 19px;")
		# adding signal and slot  
		self.radioButton_8k.toggled.connect(self.selected_8k)



		# Radio Buttons
		self.radioButton_16k = QtWidgets.QRadioButton(self) 
		self.radioButton_16k.setText("16K")
		self.radioButton_16k.setGeometry(QtCore.QRect(500, 100, 95, 40)) 
		self.radioButton_16k.setStyleSheet("font-size : 19px;")
		# adding signal and slot  
		self.radioButton_16k.toggled.connect(self.selected_16k)



		# Searching Type : Regular Linear Search depends on string length
		self.blockLinearSearch_Btn = QPushButton('Regular Linear Search\n Depended on String Length', self)
		self.blockLinearSearch_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.blockLinearSearch_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.blockLinearSearch_Btn.setGeometry(60, 160, 250, 60)
		self.blockLinearSearch_Btn.clicked.connect(self.on_blockLinearSearch_Btn_BtnClick)

		# Execution Time Input
		self.firstStepTime_Input = QPlainTextEdit(self)
		self.firstStepTime_Input.setStyleSheet("color: black; font-size : 19px; border : 2px solid black")
		self.firstStepTime_Input.setGeometry(330, 160, 300, 60)
		self.firstStepTime_Input.appendPlainText("Execution Time : \nAverg Execution Time : ")



		# Searching Type : Regular Linear Search depends on string length
		self.blockLinearSearch_reference_Btn = QPushButton('Block Linear Search using\nreference block first', self)
		self.blockLinearSearch_reference_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.blockLinearSearch_reference_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.blockLinearSearch_reference_Btn.setGeometry(60, 240, 250, 60)
		self.blockLinearSearch_reference_Btn.clicked.connect(self.on_blockLinearSearch_reference_BtnClick)

		# Execution Time Input
		self.secondStepTime_Input = QPlainTextEdit(self)
		self.secondStepTime_Input.setStyleSheet("color: black; font-size : 19px; border : 2px solid black")
		self.secondStepTime_Input.setGeometry(330, 240, 300, 60)
		self.secondStepTime_Input.appendPlainText("Execution Time : \nAverg Execution Time : ")



		# Searching Type : Regular Linear Search depends on string length
		self.blockLinearSearch_length_Btn = QPushButton('Block Linear Search of length\nthen string comprarison', self)
		self.blockLinearSearch_length_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.blockLinearSearch_length_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.blockLinearSearch_length_Btn.setGeometry(60, 320, 250, 60)
		self.blockLinearSearch_length_Btn.clicked.connect(self.on_blockLinearSearch_length_BtnClick)

		# Execution Time Input
		self.thirdStepTime_Input = QPlainTextEdit(self)
		self.thirdStepTime_Input.setStyleSheet("color: black; font-size : 19px; border : 2px solid black")
		self.thirdStepTime_Input.setGeometry(330, 320, 300, 60)
		self.thirdStepTime_Input.appendPlainText("Execution Time : \nAverg Execution Time : ")


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
				down_cnt = self.element_cnt
				for line in lines :
					self.arr.append(line.strip())
					down_cnt -= 1
					if down_cnt == 0 :
						break
				return 
			except IOError as X :
				print  ("couldn't read this file on this spot")

	def log_Result(self, Searching_Type, execution_Time, average) :
		while 1 :
			try :
				with open('log.txt', 'a', encoding = 'utf-8') as file_object :
					pattern = str(self.elementPattern_Input.text())
					now = datetime.now()
					current_time = now.strftime("%d/%m/%Y %H:%M:%S")
					str_cur_time = "    Current Date Time ::  " + current_time + ":::"
					file_object.write(str_cur_time + Searching_Type + ":: Searching Pattern :: " + pattern + " :: Execution Time : " + execution_Time + " :: Average Execution Time : " + average + "\n")
				return
			except IOError as X :
				print  ("couldn't read this file on this spot")


	def selected_1k (self, selected) :
		if selected :
			self.element_cnt = 1000
			self.getFileStrData()

	def selected_2k (self, selected) :
		if selected :
			self.element_cnt = 2000
			self.getFileStrData()
	def selected_4k (self, selected) :
		if selected :
			self.element_cnt = 4000
			self.getFileStrData()
	def selected_8k (self, selected) :
		if selected :
			self.element_cnt = 8000
			self.getFileStrData()
	def selected_16k (self, selected) :
		if selected :
			self.element_cnt = 16000
			self.getFileStrData()

	# Do block linear search with the value and array
	def on_blockLinearSearch_Btn_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return

		sum_execution_time = 0
		for i in range(10):
			start_time = time.perf_counter()
		    
			search_On_Parallel_Array(build_3_12_Array(self.arr), pattern)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 10) * 1000000) / 1000) + "MS"
		self.firstStepTime_Input.setPlainText("Execution Time : " + exe_time + "\nAverg Execution Time : " + averg_time)

		self.log_Result("Regular Linear Search Depended on String Length", exe_time, averg_time)



	# Do block linear search reference
	def on_blockLinearSearch_reference_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return

		sum_execution_time = 0
		for i in range(10):
			start_time = time.perf_counter()

			ref_arr = get_Reference_array(self.arr, BEST_RESULT)
			Block_Linear_Search_Using_Reference_Block_First(self.arr, ref_arr, pattern)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 10) * 1000000) / 1000) + "MS"
		self.secondStepTime_Input.setPlainText("Execution Time : " + exe_time + "\nAverg Execution Time : " + averg_time)

		self.log_Result("Block Linear Search using reference block First", exe_time, averg_time)




	# Do block linear search length
	def on_blockLinearSearch_length_BtnClick(self):
		pattern = self.getSearchPattern()
		if pattern == None :
			self.messageBox()
			return
    	
		length_arr = parallel_Array(self.arr)

		sum_execution_time = 0
		for i in range(10):
			start_time = time.perf_counter()

			ref_arr = get_Reference_array(self.arr, BEST_RESULT)
			Block_Linear_Search_Of_Length_String(self.arr, ref_arr, pattern, length_arr)

			end_time = time.perf_counter()
			sum_execution_time += end_time - start_time


		exe_time = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 10) * 1000000) / 1000) + "MS"
		self.thirdStepTime_Input.setPlainText("Execution Time : " + exe_time + "\nAverg Execution Time : " + averg_time)

		self.log_Result("Block Linear Search of length then string comprarison", exe_time, averg_time)




if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = MainWindow()
	screen.show()
	sys.exit(app.exec_())
