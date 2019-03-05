import sys
import os
from configparser import ConfigParser
from PyQt5.QtWidgets import QApplication
from application import MainWindow

from helper.theme_helper import theme_obj

def initialize(): #Sets application directory
    app_dir = (os.path.dirname(os.path.realpath("__main__")))
    os.chdir(app_dir)

class parser():
    def __init__(self): #Tries to read config.ini
        self.config = ConfigParser()
        try:
            self.config.read("config.ini")
        except:
            print("config.ini Not Found. Continuing with default settings...")

    def default(self,ini_property): #Returns values in [DEFAULT] of config
        default_section = self.config["DEFAULT"]
        return default_section[ini_property]
    
    def other(self,ini_property): #Returns values in [OTHER] of config
        other_section = self.config["OTHER"]
        return other_section[ini_property]

def main():
    initialize()
    ini_parser = parser()
    app = QApplication(sys.argv)
    
    #Set all configs
    try:
        #app.setStyle(str(ini_parser.default("Style"))) # Style
        
        p1 = str(os.getcwd()) #Jimmy rigged to get working, will fix some other time
        p2 = "\\ui\\themes\\"
        p3 = str(ini_parser.default("Palette"))
        p4 = "{}{}{}".format(p1,p2,p3)
        
        p4.replace(" ","")
    
        app.setPalette(theme_obj(p4)) #Palette
    except:
        print("Error loading config.ini. Continuing with default settings...")
        pass
     
    #Load Application GUI
    app_main = MainWindow()
    app_main.show()
    app.exec_()
        
if __name__=="__main__":
    main()
     