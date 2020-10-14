import sys, os, traceback, types
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QProgressBar, QLineEdit, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from collections import deque 
import time
import threading
import math
import multiprocessing
import random
from datetime import datetime


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
    if arr_A[a_len-1] <= arr_B[0] :
        return

    last_A = arr_A.pop()            # Popup the last element in A and store that in last_A
    first_B = arr_B.pop(0)          # Popup the first element in B and store that in last_A

    # Add them to the other side of array
    arr_B.append(last_A)
    arr_A.append(first_B)

    # sort both of arrays with sort_Functions
    sort_func(arr_A)
    sort_func(arr_B)

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

        return sorted_arr

    merge_block_arrays(new_block, func_sort, rest_arr, merge_func)



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
		self.setGeometry(60,80,600,350)

		self.setWindowTitle('BUBBLE MERGE PARALLEL_BUBBLE PARALLEL_MERGE SORTING ALGORITHM')
		
		# Element Input Label
		self.elementCnt_Label = QLabel(self)
		self.elementCnt_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.elementCnt_Label.setGeometry(50, 40, 250, 30)
		self.elementCnt_Label.setText("Number of Elements : ")

		# Element Cnt Input
		self.elementCnt_Input = QLineEdit(self)
		self.elementCnt_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.elementCnt_Input.setGeometry(320, 40, 200, 35)


		# Sorting TYPE - Insertion Sorting
		self.InsertionSort_Btn = QPushButton('Insertion Sort', self)
		self.InsertionSort_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 19px; border-radius:5px;")
		self.InsertionSort_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.InsertionSort_Btn.setGeometry(40, 100, 160, 40)
		self.InsertionSort_Btn.clicked.connect(self.on_Insertion_SortBtnClick)

		# Sorting TYPE - Selection Sort
		self.SelectionSort_Btn = QPushButton('Selection Sort', self)
		self.SelectionSort_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.SelectionSort_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.SelectionSort_Btn.setGeometry(220, 100, 160, 40)
		self.SelectionSort_Btn.clicked.connect(self.on_Selection_SortBtnClick)


		# Sorting TYPE - Merge Sort
		self.MergeSort_Btn = QPushButton('Merge Sort', self)
		self.MergeSort_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.MergeSort_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.MergeSort_Btn.setGeometry(400, 100, 160, 40)
		self.MergeSort_Btn.clicked.connect(self.on_Merge_SortBtnClick)




		# Sorting TYPE - Parallel insertion sort
		self.Par_InsertionSort_Btn = QPushButton('Parallel Insertion', self)
		self.Par_InsertionSort_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 19px; border-radius:5px;")
		self.Par_InsertionSort_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.Par_InsertionSort_Btn.setGeometry(40, 160, 160, 40)
		self.Par_InsertionSort_Btn.clicked.connect(self.on_Par_Insertion_SortBtnClick)

		# Sorting TYPE - Parallel Selection sort
		self.Par_SelectionSort_Btn = QPushButton('Parallel Selection', self)
		self.Par_SelectionSort_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.Par_SelectionSort_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.Par_SelectionSort_Btn.setGeometry(220, 160, 160, 40)
		self.Par_SelectionSort_Btn.clicked.connect(self.on_Par_Selection_SortBtnClick)


		# Sorting TYPE - Parallel merge sort
		self.Par_MergeSort_Btn = QPushButton('Parallel Merge', self)
		self.Par_MergeSort_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.Par_MergeSort_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.Par_MergeSort_Btn.setGeometry(400, 160, 160, 40)
		self.Par_MergeSort_Btn.clicked.connect(self.on_Par_Merge_SortBtnClick)





		# Execution Time Label
		self.Execution_Time_Label = QLabel(self)
		self.Execution_Time_Label.setStyleSheet("color: black; font-size : 23px; border : ")
		self.Execution_Time_Label.setGeometry(50, 230, 200, 35)
		self.Execution_Time_Label.setText("Execution Time : ")

		# Execution Time output
		self.Execution_Time_output = QLabel(self)
		self.Execution_Time_output.setStyleSheet("color: black; font-size : 23px; border : 2px solid black;")
		self.Execution_Time_output.setGeometry(280, 230, 200, 35)
		self.Execution_Time_output.setText("UnKnown")


		# Execution Time Label
		self.Averge_Time_Label = QLabel(self)
		self.Averge_Time_Label.setStyleSheet("color: black; font-size : 23px; border : ")
		self.Averge_Time_Label.setGeometry(50, 280, 200, 35)
		self.Averge_Time_Label.setText("Averg Exec Time : ")

		# Execution Time output
		self.Averge_Time_output = QLabel(self)
		self.Averge_Time_output.setStyleSheet("color: black; font-size : 23px; border : 2px solid black;")
		self.Averge_Time_output.setGeometry(280, 280, 200, 35)
		self.Averge_Time_output.setText("UnKnown")

		
		self.show()


	def IsInt(self, value) :
		try : 
			int(value)
			return True
		except :
			return False

	def getCnt(self) :
		if self.IsInt(self.elementCnt_Input.text()) :
			return int(self.elementCnt_Input.text())
		else :
			return 0

	def messageBox(self) :
		msgBox = QMessageBox.question(self, 'Warning', "Please Input the Element Count!")

	def getFileStrData(self) :

		cnt = int(self.elementCnt_Input.text())
		# Using readlines() 
		while 1:
			try :
				with open('GutenbergWordsFile.txt', 'r') as file_read :
					lines = file_read.readlines()

				List = []
				for line in lines :
					cnt -= 1
					List.append(line.strip())
					if cnt == 0 :
						break
				return List
			except IOError as X :
				print  ("couldn't read this file on this spot")

	def log_Result(self, sorting_Type, execution_Time, averg_time) :
		while 1 :
			try :
				with open('log.txt', 'a', encoding = 'utf-8') as file_object :
					cnt = int(self.elementCnt_Input.text())
					now = datetime.now()
					current_time = now.strftime("%d/%m/%Y %H:%M:%S")
					str_cur_time = "Current Date Time :: " + current_time
					file_object.write(str_cur_time  +  sorting_Type + ":: Element Count :: " + str(cnt) + " :: Execution Time : " + execution_Time + " :: Average Time : " + averg_time + "\n")
				return
			except IOError as X :
				print  ("couldn't read this file on this spot")

	def assign_arr(self) :
		arr = []
		arr = [v for v in self.arr]
		return arr

	def on_Insertion_SortBtnClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		self.arr = self.getFileStrData()

		# Do insertion Sort Several times and get the average exe_time from there.
		sum_execution_time = 0
		for i in range(3):

			arr = self.assign_arr()

			start_time = time.perf_counter()
			insertion_Sort(arr)
			dur_time = time.perf_counter() - start_time
			sum_execution_time += dur_time

		exe_time = str(int((dur_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 3) * 1000000) / 1000) + "MS"
		self.Execution_Time_output.setText(exe_time)
		self.Averge_Time_output.setText(averg_time)

		self.log_Result("Insertion Sort", exe_time, averg_time)


	def on_Selection_SortBtnClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		self.arr = self.getFileStrData()

		# Do insertion Sort Several times and get the average exe_time from there.
		sum_execution_time = 0
		for i in range(3):

			arr = self.assign_arr()

			start_time = time.perf_counter()
			selection_Sort(arr)
			dur_time = time.perf_counter() - start_time
			sum_execution_time += dur_time

		exe_time = str(int((dur_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 3) * 1000000) / 1000) + "MS"
		self.Execution_Time_output.setText(exe_time)
		self.Averge_Time_output.setText(averg_time)

		self.log_Result("Selection Sort", exe_time, averg_time)


	def on_Merge_SortBtnClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		self.arr = self.getFileStrData()

		# Do insertion Sort Several times and get the average exe_time from there.
		sum_execution_time = 0
		for i in range(3):

			arr = self.assign_arr()

			start_time = time.perf_counter()
			merge_Sort(arr)
			dur_time = time.perf_counter() - start_time
			sum_execution_time += dur_time

		exe_time = str(int((dur_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 3) * 1000000) / 1000) + "MS"
		self.Execution_Time_output.setText(exe_time)
		self.Averge_Time_output.setText(averg_time)

		self.log_Result("Merge Sort", exe_time, averg_time)



	def on_Par_Insertion_SortBtnClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		self.arr = self.getFileStrData()

		# Do insertion Sort Several times and get the average exe_time from there.
		sum_execution_time = 0
		for i in range(3):

			arr = self.assign_arr()

			start_time = time.perf_counter()
			block_arr, rest_arr = divide_Array(arr)
			merge_block_arrays(block_arr, insertion_Sort, rest_arr, method_One_Merge)
			dur_time = time.perf_counter() - start_time
			sum_execution_time += dur_time

		exe_time = str(int((dur_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 3) * 1000000) / 1000) + "MS"
		self.Execution_Time_output.setText(exe_time)
		self.Averge_Time_output.setText(averg_time)

		self.log_Result("Parallel Insertion Sort", exe_time, averg_time)


	def on_Par_Selection_SortBtnClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		self.arr = self.getFileStrData()

		# Do insertion Sort Several times and get the average exe_time from there.
		sum_execution_time = 0
		for i in range(3):
			arr = self.assign_arr()

			start_time = time.perf_counter()
			block_arr, rest_arr = divide_Array(arr)
			merge_block_arrays(block_arr, selection_Sort, rest_arr, method_One_Merge)
			dur_time = time.perf_counter() - start_time
			sum_execution_time += dur_time

		exe_time = str(int((dur_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 3) * 1000000) / 1000) + "MS"
		self.Execution_Time_output.setText(exe_time)
		self.Averge_Time_output.setText(averg_time)

		self.log_Result("Parallel Selection Sort", exe_time, averg_time)


	def on_Par_Merge_SortBtnClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		self.arr = self.getFileStrData()

		# Do insertion Sort Several times and get the average exe_time from there.
		sum_execution_time = 0
		for i in range(3):

			arr = self.assign_arr()

			start_time = time.perf_counter()
			block_arr, rest_arr = divide_Array(arr)
			merge_block_arrays(block_arr, selection_Sort, rest_arr, method_Two_Merge)
			dur_time = time.perf_counter() - start_time
			sum_execution_time += dur_time

		exe_time = str(int((dur_time) * 1000000) / 1000) + "MS"
		averg_time = str(int((sum_execution_time / 3) * 1000000) / 1000) + "MS"
		self.Execution_Time_output.setText(exe_time)
		self.Averge_Time_output.setText(averg_time)

		self.log_Result("Parallel Merge Sort", exe_time, averg_time)




if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = MainWindow()
	screen.show()
	sys.exit(app.exec_())
