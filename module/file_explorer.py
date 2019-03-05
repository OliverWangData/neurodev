from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QLineEdit

class fileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        
        self.model = QFileSystemModel(self)
        treemodel = self.model
        treemodel.setRootPath("")
        
        self.tree = QTreeView()
        treeView = self.tree
        treeView.setModel(treemodel)
        treeView.hideColumn(1)
        treeView.hideColumn(2)
        treeView.hideColumn(3)
        
        
        treeView.clicked.connect(self.mouse_click)
        
        self.path_display = QLineEdit()
        
        Layout = QVBoxLayout(self)
        Layout.addWidget(self.path_display)
        Layout.addWidget(treeView)
        self.setLayout(Layout)
    
    def mouse_click(self,path):
        self.path_display.setText(self.sender().model().filePath(path))