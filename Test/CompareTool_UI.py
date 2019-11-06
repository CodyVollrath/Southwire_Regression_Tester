'''
@Author Cody Vollrath
@Version 1.00
@Company Southwire Company
'''
#TODO: Create two find methods and widgits that will allow user to find text they need
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit
from tkinter import *
from tkinter import filedialog
import sys
import hashlib
import detect_delimiter

class Ui_MainWindow(object):
	
	def setupUi(self, MainWindow):
		#Window Config
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1414, 867)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		#UI Components
		self.titleLabel()
		self.ignoreEnvelopesCheckBox()
		self.browseButtons()
		self.fileLabelsMethod()
		self.textBrowserMethod()
		self.saveOptions()
		self.compareButtonMethod()
		self.wrapOptions()
		
		#Main Window Options
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1414, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def titleLabel(self):
		self.Title = QtWidgets.QLabel(self.centralwidget)
		self.Title.setGeometry(QtCore.QRect(10, 10, 231, 16))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.Title.setFont(font)
		self.Title.setObjectName("Title")

	def ignoreEnvelopesCheckBox(self):
		self.ignoreEnvelopeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.ignoreEnvelopeCheckBox.setGeometry(QtCore.QRect(540, 0, 111, 17))
		self.ignoreEnvelopeCheckBox.setObjectName("ignoreEnvelopeCheckBox")

	def browseButtons(self):
		self.browseButton = QtWidgets.QPushButton(self.centralwidget)
		self.browseButton.setGeometry(QtCore.QRect(10, 90, 75, 23))
		self.browseButton.setObjectName("browseButton")

		self.browseButton.clicked.connect(self.fileDialogBrowse)

		self.browseButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.browseButton_2.setGeometry(QtCore.QRect(610, 90, 75, 23))
		self.browseButton_2.setObjectName("browseButton_2")
		self.browseButton_2.clicked.connect(self.fileDialogBrowse2)

	def wrapOptions(self):
		self.wrapEntry = QtWidgets.QLineEdit(self.centralwidget)
		self.wrapEntry.setGeometry(QtCore.QRect(540, 30, 113, 20))
		self.wrapEntry.setObjectName("wrapEntry")
		self.replaceEntry = QtWidgets.QLineEdit(self.centralwidget)
		self.replaceEntry.setGeometry(QtCore.QRect(540, 50, 113, 20))
		self.replaceEntry.setObjectName("replaceEntry")
		self.wrapLabel = QtWidgets.QLabel(self.centralwidget)
		self.wrapLabel.setGeometry(QtCore.QRect(460, 30, 61, 21))
		self.wrapLabel.setObjectName("wrapLabel")
		self.replaceLabel = QtWidgets.QLabel(self.centralwidget)
		self.replaceLabel.setGeometry(QtCore.QRect(460, 50, 71, 21))
		self.replaceLabel.setObjectName("replaceLabel")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(670, 40, 75, 23))
		self.pushButton_3.setObjectName("pushButton_3")

		#Button Commands
		self.pushButton_3.clicked.connect(self.wrap)

	def saveOptions(self):
		self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
		self.SaveButton.setGeometry(QtCore.QRect(1220, 140, 75, 23))
		self.SaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.SaveButton.setStatusTip("")
		self.SaveButton.setObjectName("SaveButton")

		self.SaveButton2 = QtWidgets.QPushButton(self.centralwidget)
		self.SaveButton2.setGeometry(QtCore.QRect(1220, 170, 75, 23))
		self.SaveButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.SaveButton2.setStatusTip("")
		self.SaveButton2.setObjectName("SaveButton2")

		#Button commands
		self.SaveButton.clicked.connect(lambda:self.overWriteSave1or2(True))
		self.SaveButton2.clicked.connect(lambda:self.overWriteSave1or2(False))

	
	def fileLabelsMethod(self):
		self.fileLabel = QtWidgets.QLabel(self.centralwidget)
		self.fileLabel.setGeometry(QtCore.QRect(10, 120, 571, 16))
		self.fileLabel.setFrameShape(QtWidgets.QFrame.Box)
		self.fileLabel.setObjectName("fileLabel")
		self.fileLabel2 = QtWidgets.QLabel(self.centralwidget)
		self.fileLabel2.setGeometry(QtCore.QRect(610, 120, 581, 16))
		self.fileLabel2.setFrameShape(QtWidgets.QFrame.Box)
		self.fileLabel2.setObjectName("fileLabel2")

	def textBrowserMethod(self):
		self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
		self.scrollArea.setGeometry(QtCore.QRect(9, 140, 581, 581))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 579, 579))
		self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

		self.textBrowser_1 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
		self.textBrowser_1.setGeometry(QtCore.QRect(0, 0, 581, 581))
		self.textBrowser_1.setReadOnly(False)
		self.textBrowser_1.setUndoRedoEnabled(True)
		self.textBrowser_1.setObjectName("textBrowser_1")

		self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
		self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
		self.scrollArea_2.setGeometry(QtCore.QRect(609, 140, 581, 581))
		self.scrollArea_2.setWidgetResizable(True)
		self.scrollArea_2.setObjectName("scrollArea_2")
		self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 579, 579))
		self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")

		self.textBrowser_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
		self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 581, 581))
		self.textBrowser_2.setReadOnly(False)
		self.textBrowser_2.setUndoRedoEnabled(True)
		self.textBrowser_2.setObjectName("textBrowser_2")
		self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
	
	def compareButtonMethod(self):
		self.compareButton = QtWidgets.QPushButton(self.centralwidget)
		self.compareButton.setGeometry(QtCore.QRect(570, 730, 75, 23))
		self.compareButton.setObjectName("compareButton")

		self.compareButton.clicked.connect(self.breakUpLines)

	#Disable the button based on the stae of button - If enabled -> Disable && If Disabled -> enable
	def disableOrEnableButton(self,buttonObject):
		if buttonObject.isEnabled():
			buttonObject.setDisabled(True)
		else:
			buttonObject.setDisabled(False)
	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "EDI Compare Tool"))
		self.SaveButton.setText(_translate("MainWindow", "Save File 1"))
		self.SaveButton2.setText(_translate("MainWindow", "Save File 2"))
		self.fileLabel.setText(_translate("MainWindow", "File 1:"))
		self.fileLabel2.setText(_translate("MainWindow", "File 2:"))
		self.Title.setText(_translate("MainWindow", "Compare Tool"))
		self.ignoreEnvelopeCheckBox.setText(_translate("MainWindow", "Ignore Envelopes"))
		self.browseButton.setText(_translate("MainWindow", "Browse File 1"))
		self.browseButton_2.setText(_translate("MainWindow", "Browse File 2"))
		
		self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
		"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
		"p, li { white-space: pre-wrap; }\n"
		"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
		"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		
		self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
		"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
		"p, li { white-space: pre-wrap; }\n"
		"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
		"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		
		self.wrapLabel.setText(_translate("MainWindow", "Wrap At:"))
		self.replaceLabel.setText(_translate("MainWindow", "Replace With:"))
		self.pushButton_3.setText(_translate("MainWindow", "Wrap"))
		self.compareButton.setText(_translate("MainWindow", "Compare"))


	#Functional Methods
	def getTextAreaData(self,textArea):
		copiedText = textArea.toPlainText()
		return copiedText
	def getHashOfTextBrowserObject(self,textArea):
		priorData = self.getTextAreaData(textArea)
		hashObj = hashlib.sha256(priorData.encode('UTF-8'))
		hexDig = hashObj.hexdigest()
		return hexDig
	def fileDialogBrowse(self):
		Tk().withdraw()
		self.disableOrEnableButton(self.browseButton)
		try:
			self.fileName = filedialog.askopenfilename(initialdir = "Documents/", title = "Select File 1", filetype = (("EDI", "*.edi"), ("IDOC", ".idoc"), ("TEXT",'.txt')))
			self.fileLabel.setText("File 1: " + self.fileName)
			textData = self.readFile(self.fileName)
			self.textBrowser_1.setText(textData)
			self.priorHashValue1 = self.getHashOfTextBrowserObject(self.textBrowser_1)
		except:
			pass
		self.disableOrEnableButton(self.browseButton)

	def fileDialogBrowse2(self):
		Tk().withdraw()
		self.disableOrEnableButton(self.browseButton_2)
		try:
			self.fileName2 = filedialog.askopenfilename(initialdir = "Documents/", title = "Select File 2", filetype = (("EDI", "*.edi"), ("IDOC", ".idoc"), ("TEXT",'.txt')))
			self.fileLabel2.setText("File 2: " + self.fileName2)
			textData = self.readFile(self.fileName2)
			self.textBrowser_2.setText(textData)
			self.priorHashValue2 = self.getHashOfTextBrowserObject(self.textBrowser_2)
		except:
			pass
		self.disableOrEnableButton(self.browseButton_2)

	#PRECONDITION: isSave1 Represents a boolean value, if true is entered into the parameter then overWriteSave will activate, otherwise overWriteSave2 will activate
	def overWriteSave1or2(self,isSave1):
		#TODO: Detect change in textArea and ask user to save only if change is found
		
		try:
			if isSave1:
				self.changedValue = self.getHashOfTextBrowserObject(self.textBrowser_1)
				if self.changedValue != self.priorHashValue1:
					if self.isMessageBoxApproved(self.fileName):
						newData = self.textBrowser_1.toPlainText()
						self.writeFile(self.fileName,newData)
				else:
					newData = self.textBrowser_1.toPlainText()
					self.writeFile(self.fileName,newData)
				self.priorHashValue1 = self.getHashOfTextBrowserObject(self.textBrowser_1)
			else:
				self.changedValue2 = self.getHashOfTextBrowserObject(self.textBrowser_2)
				if self.changedValue2 != self.priorHashValue2:
					if self.isMessageBoxApproved(self.fileName2):
						newData = self.textBrowser_2.toPlainText()
						self.writeFile(self.fileName2,newData)
				else:
					newData = self.textBrowser_2.toPlainText()
					self.writeFile(self.fileName2,newData)
				self.priorHashValue2 = self.getHashOfTextBrowserObject(self.textBrowser_2)
		except:
			pass
	def isMessageBoxApproved(self,filename):
		askQuestion = QMessageBox()
		answer = askQuestion.question(askQuestion,'Overwrite Save Confirmation','Are you sure you want to overwrite ' + str(filename) + '?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
		if answer == askQuestion.Yes:
			return True
		else:
			return False
	
	def readFile(self, filename):
		with open(filename) as f:
			return f.read()
	def writeFile(self,filename,dataToWrite):
		with open(filename,'w+') as f:
			f.write(dataToWrite)
	
	def wrap(self):
		wrapAt = self.wrapEntry.text()
		replaceText = self.replaceEntry.text()
		browser1 = self.textBrowser_1.toPlainText()
		browser2 = self.textBrowser_2.toPlainText()
		if len(wrapAt) != 0 and len(replaceText) != 0:
			self.lines = browser1.replace(wrapAt,replaceText)
			self.lines2 = browser2.replace(wrapAt,replaceText)
		else:
			self.lines = browser1.replace(wrapAt,wrapAt + '\n')
			self.lines2 = browser2.replace(wrapAt,wrapAt + '\n')
		self.textBrowser_1.setText(self.lines)
		self.textBrowser_2.setText(self.lines2)
	
	def breakUpLines(self):
		self.countMismatches = 0
		dataArray = []
		data1 = self.textBrowser_1.toPlainText()
		data2 = self.textBrowser_2.toPlainText()
		lineItems = data1.split('\n')
		lineItems2 = data2.split('\n')
		if len(lineItems) == len(lineItems2):
			line2 = lineItems2
			i = 0
			for line in lineItems:
				if self.isIgnoreHeaderEnabled():
					if 'ISA' in line or 'GS' in line or 'ST' in line or 'SE' in line or 'GE' in line or 'IEA' in line:
						i +=1
					else:
						if 'SCH' in line:
							delimiter = self.determineDelimiter(line)
							sch = line.split(delimiter)
							sch_2 = line2[i].split(delimiter)
							 
							if len(self.extractNumbers(sch[6])) > 0 and len(self.extractNumbers(sch_2[6]))>0:
								i +=1
							else:
								if len(sch[6]) == 0 and len(sch_2[6]) == 0:
									i+=1
								else:
									dataArray.append(self.compareTwoLines(line,str(line2[i])))
									i+=1
						else:
							dataArray.append(self.compareTwoLines(line,str(line2[i])))
						i+=1
				else:
					dataArray.append(self.compareTwoLines(line,str(line2[i])))
					i+=1
			if self.countMismatches == 0:
				self.promptMatchConfirmation()
			else:
				self.saveFileData(dataArray)
		else:
			self.fileLinesDontAddUpPrompt()
	
	#Determines the delimiter by userinput
	def extractNumbers(self,data):
		data = data[:-1]
		return data
	def determineDelimiter(self,lineData):
		return detect_delimiter.detect(lineData)
	def compareTwoLines(self,line1,line2):
		if not line1 == line2:
			self.countMismatches += 1
			data = "Mismatch Found:\nText Area 1: ['" + line1 + "']\nText Area 2: ['" + line2 + "']\n\n"
			return data
		return ''
	
	def fileLinesDontAddUpPrompt(self):
		prompt = QMessageBox()
		prompt.setIcon(QMessageBox.Information)
		try:
			prompt.question(prompt,"Number of Lines Unequal!","Files out of Sync: " + self.fileName + " | " + self.fileName2,QMessageBox.Ok|QMessageBox.Close,QMessageBox.Close)
		except:
			prompt.question(prompt,"Number of Lines Unequal!","Out of Sync",QMessageBox.Ok|QMessageBox.Close,QMessageBox.Close)

	
	def promptMatchConfirmation(self):
		allMatchConfirmation = QMessageBox()
		allMatchConfirmation.setIcon(QMessageBox.Information)
		try:
			allMatchConfirmation.question(allMatchConfirmation,"Everything Matched!","Both files match: " + self.fileName + " | " + self.fileName2,QMessageBox.Ok|QMessageBox.Close,QMessageBox.Close)
		except:
			allMatchConfirmation.question(allMatchConfirmation,"Everything Matched!","Both textboxes match",QMessageBox.Ok|QMessageBox.Close,QMessageBox.Close)

	def saveFileData(self,dataArray):
		Tk().withdraw()
		self.disableOrEnableButton(self.compareButton)
		try:
			errorLog = filedialog.asksaveasfile(initialdir = "Documents/", title = "Save Output File", filetype = (("text", "*.txt"), ("All Files", "*")))
			for each in dataArray:
				self.appendDataToFile(errorLog.name,each)
		except:
			pass
		self.onlyMatches = False
		self.disableOrEnableButton(self.compareButton)

	def appendDataToFile(self,filename,data):
		outputFile = open(filename,"a")
		outputFile.write(data)
		outputFile.close()
	def isIgnoreHeaderEnabled(self):
		if self.ignoreEnvelopeCheckBox.isChecked():
			return True
		else:
			return False
def main():
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())
main()