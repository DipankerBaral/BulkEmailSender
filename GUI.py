
import sys
from PyQt5.QtWidgets import *

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()


        #Line edit boxes
                
        self.lineEntry = QLineEdit(self)
        self.lineEntry.move(100,16)
        self.lineEntry.resize(200,40)

        self.qlabel = QLabel(self)
        self.qlabel.move(100,64)

        self.lineEntry1= QLineEdit(self)
        self.lineEntry1.move(100,100)
        self.lineEntry1.resize(200,40)

        self.qlabel1 = QLabel(self)
        self.qlabel1.move(100,150)

        #Text beside boxes

        self.textLabel= QLabel(self)

        self.textLabel.setText("Enter Email:")
        self.textLabel.move(10,16)

        self.textLabel1 = QLabel(self)
        self.textLabel1.setText("Enter Passowrd:")

        self.textLabel1.move(10,100)

        #Send Button

        self.button1 = QPushButton(self)
        self.button1.setText("Send Email")
        self.button1.move(150,200)


        self.lineEntry1.textChanged.connect(self.onChanged1)

        self.lineEntry.textChanged.connect(self.onChanged)
        
        self.setGeometry(50,50,400,400)
        self.setWindowTitle("Bulk Email Sender")
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        print(self.qlabel)
        self.qlabel.adjustSize()

    def onChanged1(self, text):
        self.qlabel1.setText(text)
        print(self.qlabel)
        self.qlabel1.adjustSize()





                            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
