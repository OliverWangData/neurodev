from PyQt5.QtWidgets import QMainWindow, QTextEdit, QDockWidget, QTabWidget
from PyQt5.QtCore import Qt

from module.file_explorer import fileExplorer
from module.workspace_graphic import workspace_graphic
from module.tool_explorer import toolExplorer
from ui.menu_bar import initialize_menu, initialize_actions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        #General Properties
        self.setWindowTitle("NeuroNet Designer Prototype - Oliver Wang")
        
        #Creates a menubar via ui.menu_bar script
        initialize_actions(self)
        initialize_menu(self)
        
        
        #Widgets
        #"Permanent" Widget
        self.center_tab = QTabWidget()
        self.center_tab.addTab(workspace_graphic(),"Untitled1")
        self.setCentralWidget(self.center_tab)
        self.setCorner(Qt.BottomRightCorner,Qt.RightDockWidgetArea)
        #Left Docked Widget
        self.left_default_dock = QDockWidget("Tools",self)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.left_default_dock)
        self.tool_explorer = toolExplorer()
        self.left_default_dock.setWidget(self.tool_explorer)
        #Bottom Docked Widget
        self.bottom_default_dock = QDockWidget("Console",self)
        self.addDockWidget(Qt.BottomDockWidgetArea,self.bottom_default_dock)
        self.testwidget1 = QTextEdit()
        self.bottom_default_dock.setWidget(self.testwidget1)
        #Right Docked 1
        self.topright_default_dock = QDockWidget("File Explorer",self)
        self.addDockWidget(Qt.RightDockWidgetArea,self.topright_default_dock)
        self.file_explorer = fileExplorer()
        self.topright_default_dock.setWidget(self.file_explorer)
        self.topright_default_dock.show()
        #Right Docked 2
        self.bottomright_default_dock = QDockWidget("Properties Editor",self)
        self.splitDockWidget(self.topright_default_dock,self.bottomright_default_dock,Qt.Vertical)
        self.testwidget3 = QTextEdit()
        self.bottomright_default_dock.setWidget(self.testwidget3)
        
        
        
        
        
        
        #Initialize final elements
        self.statusBar().showMessage("Ready")
        self.showMaximized() #Opens in full screen