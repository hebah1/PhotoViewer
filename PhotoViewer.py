import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PhotoViewer(QWidget):
   def __init__(self, parent = None):
      super(PhotoViewer, self).__init__(parent)

      #Create Layout
      layout = QGridLayout()

      #Create buttons,label, & text
      self.openbtn = QPushButton("Open")
      self.imgname = QLabel("Image: ")
      self.label = QLabel()
      self.text = QLineEdit()
      self.text.setReadOnly(True)
      self.text.setMinimumWidth(400)

      #Adding buttons and label to layout
      self.openbtn.clicked.connect(self.getfile)
      layout.addWidget(self.imgname,0,0,1,1)
      layout.addWidget(self.text,0,1,1,1)
      layout.addWidget(self.openbtn,0,3)
      layout.addWidget(self.label,2,0,2,2)
      layout.setColumnStretch(1,5)                    #adding setColumnStretch for scaling/sizing
      self.setGeometry(10,10,600,600)
      self.setLayout(layout)
      self.setWindowTitle("Photoviewer")

   def getfile(self):
       fname, _ = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.gif *.png)")
       self.text.setText(fname)
       pixmap = QPixmap(fname)
       self.label.setPixmap(pixmap.scaled(550,400,Qt.KeepAspectRatio))

def main():
   app = QApplication(sys.argv)
   ex = PhotoViewer()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
