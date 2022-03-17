
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from pandas import ExcelFile
'''QAction常用方法有:
setIcon():设置图标；
setText():设置要显示的文字；
setToolTip()： 设置提示文字；
setShortcut()： 设置快捷键；
setCheckable()： 设置成check选择模式；
setChecked()： 设置成选中/未选中(菜单前打勾或不打勾)。
QAction常用信号：
triggered：点击时发射信号，( 最常用)；
hovered： 鼠标悬浮上空时发射该信号；
toggled： 如果状态为选中，则checked为True，该参数会被发送；
changed： 只要QAction状态发生改变就会发送，如多了个图标，换了文字等。
'''
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(QApplication.instance().quit)
        #再来一个状态栏
        openfileAct = QAction(QIcon('exit.png'), '&OpenFile', self)#添加Action
        openfileAct.setShortcut('Ctrl+O')
        openfileAct.setStatusTip('OpenFile')
        openfileAct.triggered.connect(self.openFile)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        openMenu = menubar.addMenu('&Edit')
        fileMenu.addAction(exitAct)
        openMenu.addAction(openfileAct)

        self.resize(800,600)
        self.move(1200,800)
        #self.move(500,500)
        self.setWindowTitle('Simple menu')
        
        #添加一个plaintext试一下
        self.plainText=QPlainTextEdit(self)
        self.plainText.resize(300,600)
        self.plainText.move(300,100)
        
        self.show()
        
    ''' QFileDialog.getOpenFileName()    #获取一个打开文件的文件名
        QFileDialog.getOpenFileNames()   #获取多个打开文件的文件名
        QFileDialog.getOpenFileUrl()     #获取一个打开文件的统一资源定位符
        QFileDialog.getOpenFileUrls()    #获取多个打开文件的统一资源定位符
        QFileDialog.getSaveFileName()    #获取保存的文件名
        QFileDialog.getSaveFileUrl()     #获取保存的url
    '''   
    def openFile(self): #注意是不同文件之间是双分号
        dirpath=QFileDialog.getOpenFileName(self,"请选择文件",'',"txtFile(*.txt);;Excel files(*.xls xlxs)")
        #QFileDialog.getExistingDirectory(self,"请选择目录") #返回的是tuple
        filepath=dirpath[0]
        with open(filepath,'r',encoding='utf-8') as f:
            text=f.read()
            self.plainText.setPlainText(text)
            
            
            
        #print(type(dirpath[0]))

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
