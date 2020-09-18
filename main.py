from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5 import QtWidgets
import guess

class Form:
    widget=None
    label=None
    numInput=None
    confirmButton=None
    resetButton=None
    congratulationLable=None
    currentTime=1
    result=None
    def __init__(self):
        self.initUI()
        self.initWidgetsPosition()
        self.initData()
    def initUI(self):
        self.widget=QtWidgets.QWidget()
        self.widget.setWindowTitle("猜数字游戏")
        #标签
        self.label=QtWidgets.QLabel(self.widget)
        self.label.setText('数字：')
        #数字输入框
        self.numInput=QtWidgets.QLineEdit(self.widget,placeholderText='请输入1个4位不重复的数字')
        #确认按钮
        self.confirmButton=QtWidgets.QPushButton(self.widget)
        self.confirmButton.setText('确认')
        self.confirmButton.clicked.connect(self.checkNum)
        #换个数字按钮
        self.resetButton=QtWidgets.QPushButton(self.widget)
        self.resetButton.setText('换个数字')
        self.resetButton.clicked.connect(self.resetNum)
        #提示信息
        self.congratulationLable=QtWidgets.QLabel(self.widget)
        self.congratulationLable.setText('等待您输入数字中。。。')

    def resetUi(self):
        self.numInput.setText('')
        self.confirmButton.setEnabled(True)
        self.congratulationLable.setText('等待您输入数字中。。。')

    def initWidgetsPosition(self):
        formWidth=300
        formHeigh=130
        rowHeight=30
        
        self.widget.setGeometry(0,0,formWidth,formHeigh)
        self.label.setGeometry(20,10,50,rowHeight)
        self.numInput.setGeometry(70,10,180,rowHeight)
        self.confirmButton.setGeometry(20,rowHeight*1+10*2,110,rowHeight)
        self.resetButton.setGeometry(140,rowHeight*1+10*2,110,rowHeight)
        self.congratulationLable.setGeometry(20,rowHeight*2+10*3,250,rowHeight)

    def initData(self):
        self.result=guess.ResultNum()
        self.currentTime=1
        print(self.result)
        
    def checkNum(self):
        guessNum=self.numInput.text()
        if(self.validateGuessNum(guessNum)!=True):
            return
        resultText=guess.checkNum(self.result,guessNum)
        if self.isGameOver(resultText)!=True:
            self.congratulationLable.setText('第'+str(self.currentTime)+'次：'+resultText)
        self.currentTime=self.currentTime+1

    def validateGuessNum(self,num):
        if(len(num)!=4):
            self.congratulationLable.setText('请输入1个4位不重复的数字')
            return False
        if(num.isdigit()!=True):
            self.congratulationLable.setText('请输入1个4位不重复的数字')
            return False
        #检查是否有重复数字
        if(len(list(set(num)))!=4):
            self.congratulationLable.setText('请输入1个4位不重复的数字')
            return False
        return True

    def resetNum(self):
        self.resetUi()
        self.initData()

    def isGameOver(self,result):
        if(result=='4A0B'):
            self.endGame('第'+str(self.currentTime)+'次：'+result+' 恭喜你，答案正确')
            return True
        if self.currentTime>7:
            self.endGame('第'+str(self.currentTime)+'次：很遗憾，没有猜到正确答案哦')
            return True
        return False

    def endGame(self,text):
        self.congratulationLable.setText(text)
        self.confirmButton.setEnabled(False)
    
    def show(self):
        self.widget.show()

if __name__=='__main__':
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    form=Form()
    form.show()
    app.exec_()