import sys, os, traceback, types
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QProgressBar, QLineEdit, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from collections import deque 
import time
import threading
from datetime import datetime


# SS's thread
def ss_thread(List) :
    # # Traverse through all array elements 
	for i in range(len(List)): 
	      
	    # Find the minimum element in remaining  
	    # unsorted array 
	    min_idx = i 
	    for j in range(i+1, len(List)): 
	        if List[min_idx] > List[j]: 
	            min_idx = j 
	              
	    # Swap the found minimum element with  
	    # the first element         
	    List[i], List[min_idx] = List[min_idx], List[i] 

# DSS's thread
def dss_thread(List) :

	stack1 = []
	stack2 = []
	length = len(List)
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

# PDSS's small element thread
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

# PDSS's large element thread
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

		self.setWindowTitle('THREE TYPES OF SELECTION SORTING AlGORITHM')
		
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
		self.sortingType_Label.setGeometry(20, 100, 200, 40)
		self.sortingType_Label.setText("Algorithm Type : ")


		# Sorting TYPE - Selection Sorting
		self.ss_Btn = QPushButton('SS', self)
		self.ss_Btn.setStyleSheet("color: #fff; background: #1a73e8; border: 1px solid transparent; font-size : 23px; border-radius:5px;")
		self.ss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.ss_Btn.setGeometry(250, 100, 80, 40)
		self.ss_Btn.clicked.connect(self.on_SS_ButtonClick)

		# Sorting TYPE - Dynamic Selection Sort
		self.dss_Btn = QPushButton('DSS', self)
		self.dss_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 23px;  border-radius:5px")
		self.dss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.dss_Btn.setGeometry(360, 100, 80, 40)
		self.dss_Btn.clicked.connect(self.on_DSS_ButtonClick)


		# Sorting TYPE - Paralle Dynamic Selection Sort
		self.pdss_Btn = QPushButton('PDSS', self)
		self.pdss_Btn.setStyleSheet("color: #fff; background: #1a73e8;border: 1px solid transparent; font-size : 23px;  border-radius:5px")
		self.pdss_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.pdss_Btn.setGeometry(470, 100, 80, 40)
		self.pdss_Btn.clicked.connect(self.on_PDSS_ButtonClick)


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

	def on_SS_ButtonClick(self):

		if self.getCnt() == 0 :
			self.messageBox()
			return
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
				break
			except IOError as X :
				print  ("couldn't read this file on this spot")

		start_time = time.perf_counter()
		try:
		    threading.Thread(ss_thread( List ))
		except:
		    print ("Error: unable to start thread")
		end_time = time.perf_counter()


		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)
		self.log_Result("                 Selection Sort", res_str)


	def on_DSS_ButtonClick(self):

		if self.getCnt() == 0 :
			self.messageBox()
			return
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
				break
			except IOError as X :
				print  ("couldn't read this file on this spot")
		
		start_time = time.perf_counter()
		try:
		    threading.Thread(dss_thread( List ))
		except:
		    print ("Error: unable to start thread")
		end_time = time.perf_counter()

		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)
		self.log_Result("         Dynamic Selection Sort", res_str)

	def on_PDSS_ButtonClick(self):

		if self.getCnt() == 0 :
			self.messageBox()
			return
		cnt = int(self.elementCnt_Input.text())
		# Using readlines() 
		while 1:
			try :
				with open('GutenbergWordsFile.txt', 'r') as file_read :
					lines = file_read.readlines()

				list_small = []

				for line in lines :
					cnt -= 1
					list_small.append(line.strip())
					if cnt == 0 :
						break
				break
			except IOError as X :
				print  ("couldn't read this file on this spot")

		start_time = time.perf_counter()
		try:
		    threading.Thread(smallElementThread( list_small ))
		    threading.Thread(largeElementThread( list_small ))
		except:
		    print ("Error: unable to start thread")
		end_time = time.perf_counter()

		res_str = str(int((end_time - start_time) * 1000000) / 1000) + "MS"
		self.Time_output.setText(res_str)
		self.log_Result("Parallel Dynamic Selection Sort", res_str)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = MainWindow()
	screen.show()
	sys.exit(app.exec_())
