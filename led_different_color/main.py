from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
from serial.tools.list_ports import comports
import serial

class Ui_Dialog(object):
    def setupUi(self, Dialog: QColorDialog):
        try:
            self.serial_com = serial.Serial("COM4", 115200)
        except serial.SerialException:
            print("Choose PORT from following list")
            for port in comports():
                print(f"""    {port}""")
            self.serial_com = serial.Serial("COM"+input("\nEnter PORT, COM"), 115200)
        except Exception as e:
            print(e.__class__.__name__, str(e))
        else:
            print("Graphic Windows is started")
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(493, 275)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: #000;\n"
"}\n"
"\n"
"#title {\n"
"    color: #ccc;\n"
"}\n"
"\n"
"#pushButton {\n"
"    background: #222;\n"
"    color: #ccc;\n"
"    border: 1px solid #333;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"    background: #333;\n"
"}\n"
"\n"
"#pushButton:pressed {\n"
"    background: #444;\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 220, 156, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonBox.setFont(font)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(60, 50, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 140, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.chooseColor)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def chooseColor(self):
        color = QColorDialog.getColor()
        try:
            color_code = color.getRgb()
            color_cords = str(" ".join(map(lambda a: str(a).zfill(3), color_code[:3])))
            self.serial_com.write(color_cords.encode('utf-8'))
            print("Sent To -> ", color_cords)
            print("Received By -> ", self.serial_com.readline().decode().strip())
        except Exception as e:
            print("CodeError", e.__class__.__name__, str(e))
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate # 204 222 192
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "Color Picker for LED"))
        self.pushButton.setText(_translate("Dialog", "Pick Color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
