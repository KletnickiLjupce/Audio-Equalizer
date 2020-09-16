import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from EqualizerWindow import EqualizerWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    eq = EqualizerWindow()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
