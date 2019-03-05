from PyQt5.QtWidgets import QAction, QMainWindow, QTextEdit, QDockWidget, QTabWidget, qApp
from PyQt5.QtCore import Qt

def initialize_actions(parent):
    parent.new_project = QAction("New Project",parent) #Not Assigned Yet
    parent.new_project.setShortcut("Ctrl+N")
    parent.new_project.setStatusTip("Creates new project")

    parent.new_workspace = QAction("New Workspace",parent) #Not ssigned Yet
    parent.new_workspace.setStatusTip("Creates new workspace")

    parent.new_script = QAction("New Script",parent) #Not Assigned Yet
    parent.new_script.setStatusTip("Creates new script")

    parent.open_file = QAction("Open...",parent) #Not Assigned Yet
    parent.open_file.setShortcut("Ctrl+O")
    parent.open_file.setStatusTip("Opens a file")
        
    parent.open_recent = QAction("Open Recent",parent) #Not Assigned Yet
    parent.open_recent.setStatusTip("Opens a recent file")

    parent.import_data = QAction("Import Dataset...",parent) #Not Assigned Yet
    parent.import_data.setStatusTip("Imports a dataset")

    parent.save_file = QAction("Save",parent) #Not Assigned Yet
    parent.save_file.setShortcut("Ctrl+S")
    parent.save_file.setStatusTip("Saves file")

    parent.save_as = QAction("Save As...",parent) #Not Assigned Yet
    parent.save_as.setShortcut("Ctrl+Shift+S")
    parent.save_as.setStatusTip("Select directory to save file")
    
    parent.exit_file = QAction("Exit",parent)
    parent.exit_file.setShortcut("Ctrl+Shift+Q")
    parent.exit_file.setStatusTip("Exit the application")
    parent.exit_file.triggered.connect(qApp.quit)
    
    parent.undo_action = QAction("Undo",parent)#n
    parent.undo_action.setShortcut("Ctrl+Z")
    parent.undo_action.setStatusTip("Undoes last action")
            
    parent.redo_action = QAction("Redo",parent)#n
    parent.redo_action.setShortcut("Ctrl+Y")
    parent.redo_action.setStatusTip("Redo last action")
            
    parent.edit_cut = QAction("Cut",parent)#n
    parent.edit_cut.setShortcut("Ctrl+X")
    parent.edit_cut.setStatusTip("Cut text")
            
    parent.edit_copy = QAction("Copy",parent)#n
    parent.edit_copy.setShortcut("Ctrl+C")
    parent.edit_copy.setStatusTip("Copy text")
            
    parent.edit_paste = QAction("Paste",parent)#n
    parent.edit_paste.setShortcut("Ctrl+V")
    parent.edit_paste.setStatusTip("Paste text")
            
    parent.edit_del = QAction("Del",parent)#n
    parent.edit_del.setShortcut("Del")
    parent.edit_del.setStatusTip("Delete selected")
    
def initialize_menu(parent):
    parent.default_menu = parent.menuBar()
    parent.menu_file = parent.default_menu.addMenu("File")
    parent.menu_file.addAction(parent.new_project)
    parent.menu_file_newextra = parent.menu_file.addMenu("New...")
    parent.menu_file_newextra.addAction(parent.new_workspace)
    parent.menu_file_newextra.addSeparator()
    parent.menu_file_newextra.addAction(parent.new_script)
    parent.menu_file.addSeparator()
    parent.menu_file.addAction(parent.open_file)
    parent.menu_file.addAction(parent.open_recent)
    parent.menu_file.addAction(parent.import_data)
    parent.menu_file.addSeparator()
    parent.menu_file.addAction(parent.save_file)
    parent.menu_file.addAction(parent.save_as)
    parent.menu_file.addSeparator()
    parent.menu_file.addAction(parent.exit_file)

    parent.menu_edit = parent.default_menu.addMenu("Edit")
    parent.menu_edit.addAction(parent.undo_action)
    parent.menu_edit.addAction(parent.redo_action)
    parent.menu_edit.addSeparator()
    parent.menu_edit.addAction(parent.edit_cut)
    parent.menu_edit.addAction(parent.edit_copy)
    parent.menu_edit.addAction(parent.edit_paste)
    parent.menu_edit.addAction(parent.edit_del)
        
    parent.menu_view = parent.default_menu.addMenu("View")
        
    parent.menu_create = parent.default_menu.addMenu("Create")
        
    parent.menu_run = parent.default_menu.addMenu("Run")
        
    parent.menu_console = parent.default_menu.addMenu("Console")
        
    parent.menu_settings = parent.default_menu.addMenu("Settings")
        
    parent.menu_help = parent.default_menu.addMenu("Help")