import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

class Form(object):  #动态加载UI文件
    def __init__(self):
        super().__init__()
        uiFile="cal.ui"
        self.ui=uic.loadUi(uiFile)
        #self.ui.pt1.textChanged.connect(self.onchange)
        pt=QPlainTextEdit()
        self.ui.bt1.clicked.connect(self.calc)
        self.ui.bt2.clicked.connect(self.clear)
        
        
        
    def calc(self):
        info1=self.ui.pt1.toPlainText()
        try:
            
           if info1=="":
                self.ui.pt1.setPlainText("请输入计算式:")
           else:
            text=eval(info1)
            self.ui.pt2.setPlainText(str(text))
            
        except:
            self.ui.pt1.setPlainText("语法错误")
            pass
        
        
    def clear(self):
        self.ui.pt1.clear()
        self.ui.pt2.clear()
        
    
    
              
app=QApplication(sys.argv)
uniform=Form()
uniform.ui.show()
app.exec_()
        