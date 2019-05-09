import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("sliderDialTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        """
        QAbstractSlider Singal
        - sliderMoved()
        - valueChanged()
        - rangeChanged()

        QAbstractSlider Description
        - Value : The bounded interger that QAbstractSlider maintains.
        - minumum : The lowest possible value
        - maximum : THe highest possible value.
        - singleStep : The smaller of two natural steps that typically corresponds to the user pressing an arrow key
        - pageStep : The larger of two natural steps thah typically coreesponds to the user pressing PageUp/Down and MousePress

        QAbstractSlider Function & Slot

        - maximum()
        - minimum()
        - pageStep()
        - singleStep()
        Function Above returns int Value

        - setMaximum()
        - setMinimum()
        - setPageStep()
        - setSingleStep()

        - setRange(min,max)
        - setValue()
        """

        #Vertical Slider에 기능 연결
        self.slider_vertical.valueChanged.connect(self.showVerticalSliderValue)
        self.slider_vertical.rangeChanged.connect(self.printRangeChanged)

        #Horizontal Slider에 기능 연결
        self.slider_horizontal.valueChanged.connect(self.showHorizontalSliderValue)
        self.slider_horizontal.rangeChanged.connect(self.printRangeChanged)

        #Dial에 기능 연결
        self.dial_Test.valueChanged.connect(self.showDialValue)
        self.dial_Test.rangeChanged.connect(self.printRangeChanged)

        #버튼에 기능 연결
        self.btn_vInfo.clicked.connect(self.getVerticalInfo)
        self.btn_vValue.clicked.connect(self.setVertical)
        self.btn_hInfo.clicked.connect(self.getHorizontalInfo)
        self.btn_hValue.clicked.connect(self.setHorizontal)
        self.btn_dInfo.clicked.connect(self.getDialInfo)
        self.btn_dValue.clicked.connect(self.setDial)


    def printRangeChanged(self) :
        print("Range Changed")

    #Vertical Slider에 관련된 함수들
    def showVerticalSliderValue(self) :
        self.lbl_vertical.setText(str(self.slider_vertical.value()))

    def getVerticalInfo(self) :
        print("Maximum : " + str(self.slider_vertical.maximum()))
        print("Minimum : " + str(self.slider_vertical.minimum()))
        print("PageStep : " + str(self.slider_vertical.pageStep()))
        print("SingleStep : " + str(self.slider_vertical.singleStep()))

    def setVertical(self) :
        self.slider_vertical.setMaximum(500)
        self.slider_vertical.setMinimum(-500)
        self.slider_vertical.setPageStep(100)
        self.slider_vertical.setSingleStep(20)

    #Horizontal Slider에 관련된 함수들
    def showHorizontalSliderValue(self) :
        self.lbl_horizontal.setText(str(self.slider_horizontal.value()))

    def getHorizontalInfo(self) :
        print("Maximum : " + str(self.slider_horizontal.maximum()))
        print("Minimum : " + str(self.slider_horizontal.minimum()))
        print("PageStep : " + str(self.slider_horizontal.pageStep()))
        print("SingleStep : " + str(self.slider_horizontal.singleStep()))

    def setHorizontal(self) :
        self.slider_horizontal.setMaximum(500)
        self.slider_horizontal.setMinimum(-500)
        self.slider_horizontal.setPageStep(100)
        self.slider_horizontal.setSingleStep(20)

    #Dial에 관련된 함수들
    def showDialValue(self) :
        self.lbl_dial.setText(str(self.dial_Test.value()))

    def getDialInfo(self) :
        print("Maximum : " + str(self.dial_Test.maximum()))
        print("Minimum : " + str(self.dial_Test.minimum()))
        print("PageStep : " + str(self.dial_Test.pageStep()))
        print("SingleStep : " + str(self.dial_Test.singleStep()))

    def setDial(self) :
        self.dial_Test.setMaximum(500)
        self.dial_Test.setMinimum(-500)
        self.dial_Test.setPageStep(100)
        self.dial_Test.setSingleStep(20)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 