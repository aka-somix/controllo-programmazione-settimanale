import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from modules.widgets.Window import Window

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Graphic settings
        self.title = "Controllo Programmazione Settimanale"
        self.size = QSize(800, 600)
        
        # init ui 
        self.__init_ui__()
        
        
    def __init_ui__(self):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(250,250,250,255))
        self.setPalette(palette)
        
        self.setWindowTitle(self.title)
        self.resize(self.size)
        mainWindow = Window()
        
        self.setCentralWidget(mainWindow)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
