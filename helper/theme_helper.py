from PyQt5.QtGui import QPalette, QColor
from configparser import ConfigParser

class parser():
    def __init__(self,file_dir): #Tries to read config.ini
        self.theme_ini = ConfigParser()
        try:
            self.theme_ini.read(file_dir)
        except:
            print("config.ini Not Found. Continuing with default settings...")
    
    def to_qcolor(self,section,ini_property):
        self.num_color = self.theme_ini[str(section)][str(ini_property)]
        self.num_color = self.num_color.split(",")
        qcolor = QColor(int(self.num_color[0]),int(self.num_color[1]),int(self.num_color[2]))
        return qcolor

def theme_obj(input_dir):
    theme = QPalette()
    theme_parser = parser(input_dir)
    try:
        theme.setColor(QPalette.Window, theme_parser.to_qcolor("PALETTE","Window"))
        theme.setColor(QPalette.WindowText, theme_parser.to_qcolor("PALETTE","WindowText"))
        theme.setColor(QPalette.Base, theme_parser.to_qcolor("PALETTE","Base"))
        theme.setColor(QPalette.AlternateBase, theme_parser.to_qcolor("PALETTE","AlternateBase"))
        theme.setColor(QPalette.ToolTipBase,theme_parser.to_qcolor("PALETTE","ToolTipBase"))
        theme.setColor(QPalette.ToolTipText, theme_parser.to_qcolor("PALETTE","ToolTipText"))
        theme.setColor(QPalette.Text, theme_parser.to_qcolor("PALETTE","Text"))
        theme.setColor(QPalette.Button, theme_parser.to_qcolor("PALETTE","Button"))
        theme.setColor(QPalette.ButtonText, theme_parser.to_qcolor("PALETTE","ButtonText"))
        theme.setColor(QPalette.BrightText, theme_parser.to_qcolor("PALETTE","BrightText"))
        theme.setColor(QPalette.Link, theme_parser.to_qcolor("PALETTE","Link"))
        theme.setColor(QPalette.Highlight, theme_parser.to_qcolor("PALETTE","Highlight"))
        theme.setColor(QPalette.HighlightedText, theme_parser.to_qcolor("PALETTE","HighlightedText"))
    except:
        print("Theme may not be complete. ")
        pass
    return theme

#test: theme_obj("O:\\NeuralNetworkProject\\ui\\themes\\default_dark.ini")