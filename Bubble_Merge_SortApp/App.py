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

# Bubble sort algorithm
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubbleSort_Par(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Merge sort algorithm
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
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




def BubbleSort_Parallel(data):
    # Creates a pool of worker processes, one per CPU core.
    # We then split the initial data into partitions, sized
    # equally per worker, and perform a regular merge sort
    # across each partition.
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(data)) / processes))
    data = [data[i * size:(i + 1) * size] for i in range(processes)]
    data = pool.map(bubbleSort_Par, data)
    # Each partition is now sorted - we now just merge pairs of these
    # together using the worker pool, until the partitions are reduced
    # down to a single sorted result.
    while len(data) > 1:
        # If the number of partitions remaining is odd, we pop off the
        # last one and append it back after one iteration of this loop,
        # since we're only interested in pairs of partitions to merge.
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]


# merge function
def merge(*args):
    # Support explicit left/right args, as well as a two-item
    # tuple which works more cleanly with multiprocessing.
    left, right = args[0] if len(args) == 1 else args
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index == left_length:
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:])
    return merged

# merge sort funtcion
def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    middle = int(length / 2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)

# parallel merge sort algorithm
def merge_sort_parallel(data):
    # Creates a pool of worker processes, one per CPU core.
    # We then split the initial data into partitions, sized
    # equally per worker, and perform a regular merge sort
    # across each partition.
    processes = multiprocessing.cpu_count()

    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(data)) / processes))
    data = [data[i * size:(i + 1) * size] for i in range(processes)]
    data = pool.map(merge_sort, data)
    # Each partition is now sorted - we now just merge pairs of these
    # together using the worker pool, until the partitions are reduced
    # down to a single sorted result.
    while len(data) > 1:
        # If the number of partitions remaining is odd, we pop off the
        # last one and append it back after one iteration of this loop,
        # since we're only interested in pairs of partitions to merge.
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]
    #When the Estimate Button is clicked


class MainWindow(QWidget):
	"""
	Simple dialog that consists of a Progress Bar and a Button.
	Clicking on the button results in the start of a timer and
	updates the progress bar.
	"""
	def __init__(self):
		QWidget.__init__(self)
		self.setStyleSheet("color: black; background-color: #e4e5e6;")
		self.setGeometry(60,80,600,300)

		self.setWindowTitle('BUBBLE MERGE PARALLEL_BUBBLE PARALLEL_MERGE SORTING ALGORITHM')
		
		# Element Input Label
		self.elementCnt_Label = QLabel(self)
		self.elementCnt_Label.setStyleSheet("color: black; font-size : 23px; ")
		self.elementCnt_Label.setGeometry(20, 40, 300, 40)
		self.elementCnt_Label.setText("Number of Elements : ")

		# Element Cnt Input
		self.elementCnt_Input = QLineEdit(self)
		self.elementCnt_Input.setStyleSheet("color: black; font-size : 23px; border : 2px solid black")
		self.elementCnt_Input.setGeometry(350, 40, 200, 40)


		# Element Input Label
		self.sortingType_Label = QLabel(self)
		self.sortingType_Label.setStyleSheet("color: black; font-size : 23px; border : ")
		self.sortingType_Label.setGeometry(20, 100, 150, 40)
		self.sortingType_Label.setText("Sorting Type : ")


		# Sorting TYPE - Bubble Sorting
		self.ss_Btn = QPushButton('BUBBLE', self)
		self.ss_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 19px; border-radius:5px;")
		self.ss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.ss_Btn.setGeometry(200, 100, 80, 40)
		self.ss_Btn.clicked.connect(self.on_Bubble_ButtonClick)

		# Sorting TYPE - Merge Sort
		self.dss_Btn = QPushButton('MERGE', self)
		self.dss_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.dss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.dss_Btn.setGeometry(290, 100, 80, 40)
		self.dss_Btn.clicked.connect(self.on_Merge_ButtonClick)


		# Sorting TYPE - Paralle Bubble Sort
		self.pdss_Btn = QPushButton('PA_BUB', self)
		self.pdss_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.pdss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.pdss_Btn.setGeometry(380, 100, 80, 40)
		self.pdss_Btn.clicked.connect(self.on_PAR_BUBBLE_ButtonClick)

		# Sorting TYPE - Paralle Merge Sort
		self.pdss_Btn = QPushButton('PA_MER', self)
		self.pdss_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 19px;  border-radius:5px")
		self.pdss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.pdss_Btn.setGeometry(470, 100, 80, 40)
		self.pdss_Btn.clicked.connect(self.on_PAR_Merge_ButtonClick)


		# Element Output Label
		self.OutPut_Label = QLabel(self)
		self.OutPut_Label.setStyleSheet("color: black; font-size : 23px; border : ")
		self.OutPut_Label.setGeometry(100, 200, 150, 40)
		self.OutPut_Label.setText("Time : ")

		# Element Output Time Label
		self.Time_output = QLabel(self)
		self.Time_output.setStyleSheet("color: black; font-size : 23px; border : 2px solid black;")
		self.Time_output.setGeometry(250, 200, 200, 40)
		self.Time_output.setText("UnKnown")

		multiprocessing.freeze_support()
		
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

	def log_Result(self, sorting_Type, execution_Time) :
		while 1 :
			try :
				with open('log.txt', 'a', encoding = 'utf-8') as file_object :
					cnt = int(self.elementCnt_Input.text())
					now = datetime.now()
					current_time = now.strftime("%d/%m/%Y %H:%M:%S")
					str_cur_time = "    Current Date Time ::  " + current_time
					file_object.write(sorting_Type + ":: Element Count :: " + str(cnt) +   " :: Execution Time : " + execution_Time + str_cur_time + "\n")
				return
			except IOError as X :
				print  ("couldn't read this file on this spot")


	def on_Bubble_ButtonClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		List = self.getFileStrData()

		start_time = time.perf_counter()
		try:
		    threading.Thread(bubbleSort( List ))
		except:
		    print ("Error: unable to start thread")
		end_time = time.perf_counter()

		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)

		self.log_Result("         Bubble Sort", res_str)


	def on_Merge_ButtonClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		List = self.getFileStrData()

		start_time = time.perf_counter()
		try:
		    threading.Thread(mergeSort( List ))
		except:
		    print ("Error: unable to start thread")
		end_time = time.perf_counter()

		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)
		self.log_Result("          Merge Sort", res_str)

	def on_PAR_BUBBLE_ButtonClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		List = self.getFileStrData()

		start_time = time.perf_counter()
		try:
		    data_sorted = BubbleSort_Parallel(List)
		except:
		    print ("Error: unable to start thread")
		end_time = time.perf_counter()
		
		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)
		self.log_Result("Parallel Bubble Sort", res_str)

	def on_PAR_Merge_ButtonClick(self):
		if self.getCnt() == 0 :
			self.messageBox()
			return

		List = self.getFileStrData()

		start_time = time.perf_counter()
		try:
		    data_sorted = merge_sort_parallel(List)
		except:
		    print ("Error: unable to start thread")

		end_time = time.perf_counter()
		
		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)
		self.log_Result(" Parallel Merge Sort", res_str)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = MainWindow()
	screen.show()
	sys.exit(app.exec_())
