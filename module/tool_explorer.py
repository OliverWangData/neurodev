from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from PyQt5.QtGui import QIcon

class toolExplorer(QWidget):
    def __init__(self):
        super().__init__()
        
        tool1_icon = QIcon(QApplication.style().standardIcon(QStyle.SP_DesktopIcon))
        
        