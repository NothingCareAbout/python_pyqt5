from msilib.schema import ComboBox
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class Test(object):
    def __init__(self, *args):
        super(Test, self).__init__(*args)
        
        uifile="D:\Python\PyQt5\菜单栏创建\combox.ui"
        self.ui=uic.loadUi(uifile)
        self.ui.comboBox.textActivated[str].connect(self.onActivated)
        #下拉框文字被激活绑定信号
        
       
    def onActivated(self,text):
        
        if self.ui.comboBox.currentText()=="C35":
            self.ui.lineEdit.setText(str(16.7))
        elif self.ui.comboBox.currentText()=="C40":
            self.ui.lineEdit.setText(str(19.1))
            
    
    
def main():
    app=QApplication(sys.argv) 
    test=Test()      
    test.ui.show()
    app.exec_()  
        
if __name__ == '__main__':
    main()
    
        