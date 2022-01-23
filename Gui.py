from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QLabel
from PySide6.QtGui import QCloseEvent, QIcon
from Tyson_Converter import DecConverter, HexConverter, BinConverter
import sys

'''
Please note that the file "Tyson_Converter.py" contains the true Docstring,
as this file just serves to set up the GUI for my converter. 
'''

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 300, 400)                        # Position on screen followed by width and height
        self.setWindowTitle('Tyson\'s Converter!')                      # Window Title
        self.setStyleSheet("background-color:pink")
        self.b_hex = QPushButton('Hex', self)                                   #Creating our Hex button Option
        self.b_dec = QPushButton('Dec', self)
        self.b_bin = QPushButton('Bin', self)
        self.secret_picture = QLabel('There isn\'t anything to see here...', self)
        self.secret_picture.move(500, 200)
        self.secret_picture.setWindowIcon(QIcon('secretpic.jpg'))
        self.secret_picture.show()
        self.hex_count = 0
        self.bin_count = 0
        self.dec_count = 0
        self.finish_count = 0
        self.setup()

    def setup(self):                                                            #All of the functions of your widget go here
        b_quit = QPushButton('Force Quit', self)
        b_quit.clicked.connect(QApplication.instance().quit)                    #Quit when the button is pushed
        b_quit.resize(b_quit.sizeHint())
        b_quit.move(207, 375)                                                   #Button position
        self.my_label = QLabel('What base do you wish to convert FROM?')
        self.my_label.setParent(self)
        self.my_label.move(10, 170)
        self.my_label.show()
        self.show()

        self.b_hex.clicked.connect(self.hex_click)                            #Giving the hex button a function
        self.b_hex.resize(self.b_hex.sizeHint())
        self.b_hex.move(7, 1)
        self.b_hex.setFont('American Typewriter')
        self.b_bin.setFont('American Typewriter')
        self.b_dec.setFont('American Typewriter')
        self.b_dec.clicked.connect(self.dec_click)                                  #Giving the dec button a function
        self.b_dec.resize(self.b_dec.sizeHint())
        self.b_dec.move(115, 1)
        self.b_bin.clicked.connect(self.bin_click)                                  #Giving the bin button a function
        self.b_bin.resize(self.b_bin.sizeHint())
        self.b_bin.move(220, 1)

    def hex_click(self):
        if self.hex_count == 0:
            self.hex_count += 1
            self.b_hex.setEnabled(False)
            self.b_dec.setEnabled(False)
            self.b_bin.setEnabled(False)
            hbox = QHBoxLayout()
            self.line = QLineEdit(self)                                             #Created Line Edit
            self.line.returnPressed.connect(self.onPressed)
            hbox.addWidget(self.line)
            self.setLayout(hbox)
            self.my_label.setText('Your Number(s): (Separate with commas)')
        else:
            self.number = self.number.split(',')
            if self.dec_count == 1:
                converter = DecConverter(*[x for x in self.number])
                line1, line2 = converter.to_hex()
                self.b_hex.hide()
                self.b_bin.hide()
                self.b_dec.hide()
                self.my_label.hide()
                self.Final1 = QLabel(line1 + '\n' + line2)
                self.Final1.setParent(self)
                self.Final1.move(50, -100)
                self.Final1.show()
                print(line1 + '\n' + line2)
            else:
                converter = BinConverter(*[int(x) for x in self.number])
                line1, line2 = converter.to_hex()
                self.b_hex.hide()
                self.b_dec.hide()
                self.b_bin.hide()
                self.my_label.hide()
                self.Final1 = QLabel(line1 + '\n' + line2)
                self.Final1.setParent(self)
                self.Final1.move(50, -100)
                self.Final1.show()
                print(line1 + '\n' + line2)

    def bin_click(self):
        if self.bin_count == 0:
            self.bin_count += 1
            self.b_bin.setEnabled(False)
            self.b_hex.setEnabled(False)
            self.b_dec.setEnabled(False)
            hbox = QHBoxLayout()
            self.line = QLineEdit(self)
            self.line.returnPressed.connect(self.onPressed)
            hbox.addWidget(self.line)
            self.setLayout(hbox)
            self.my_label.setText('Your Number(s): (Separate with commas)')
        else:
            self.number = self.number.split(',')
            if self.hex_count == 1:
                converter = HexConverter(*[x for x in self.number])
                line1, line2 = converter.to_bin()
                self.b_dec.hide()
                self.b_bin.hide()
                self.b_hex.hide()
                self.my_label.hide()
                self.Final1 = QLabel(line1 + '\n' + line2)
                self.Final1.setParent(self)
                self.Final1.move(50, -100)
                self.Final1.show()
                print(line1 + '\n' + line2)
            else:
                converter = DecConverter(*[int(x) for x in self.number])
                line1, line2 = converter.to_bin()
                self.b_hex.hide()
                self.b_bin.hide()
                self.b_dec.hide()
                self.my_label.hide()
                self.Final1 = QLabel(line1 + '\n' + line2)
                self.Final1.setParent(self)
                self.Final1.move(50, -100)
                self.Final1.show()
                print(line1 + '\n' + line2)

    def dec_click(self):
        if self.dec_count == 0:
            self.dec_count += 1
            self.b_dec.setEnabled(False)
            self.b_hex.setEnabled(False)
            self.b_bin.setEnabled(False)
            hbox = QHBoxLayout()
            self.line = QLineEdit(self)
            self.line.returnPressed.connect(self.onPressed)
            hbox.addWidget(self.line)
            self.setLayout(hbox)
            self.my_label.setText('Your Number(s): (Separate with commas)')
        else:
            self.number = self.number.split(',')
            if self.hex_count == 1:
                converter = HexConverter(*[x for x in self.number])
                line1, line2 = converter.to_dec()
                self.b_dec.hide()
                self.b_bin.hide()
                self.b_hex.hide()
                self.my_label.hide()
                self.Final1 = QLabel(line1 + '\n' + line2)
                self.Final1.setParent(self)
                self.Final1.move(50, -100)
                self.Final1.show()
                print(line1 + '\n' + line2)
            else:
                converter = BinConverter(*[int(x) for x in self.number])
                line1, line2 = converter.to_dec()
                self.b_dec.hide()
                self.b_hex.hide()
                self.b_bin.hide()
                self.my_label.hide()
                self.Final1 = QLabel(line1+'\n'+line2)
                self.Final1.setParent(self)
                self.Final1.move(50, -100)
                self.Final1.show()
                print(line1+'\n'+line2)

    def onPressed(self):
        self.number = self.line.text()                                 #self.line.text() is how you access what was entered into your line edit.
        self.line.hide()
        self.my_label.setText('Please click your desired base.')
        if self.hex_count == 0:
            self.b_hex.setEnabled(True)
            self.hex_count += 2
        if self.bin_count == 0:
            self.b_bin.setEnabled(True)
            self.bin_count = 2
        if self.dec_count == 0:
            self.b_dec.setEnabled(True)
            self.dec_count = 2


    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message:', ';(',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)             #Returns what was clicked?
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def run():
    app = QApplication([])
    ex = Example()
    app.exec()


if __name__ == '__main__':
    run()
