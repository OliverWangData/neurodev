import sys
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication
from PyQt5.QtGui import QPixmap, QBrush


class workspace_graphic(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        
        #GraphicsView Settings
        self.background_image = QPixmap("O:/NeuralNetworkProject/assets/workspace_background.png")
        self.background_brush = QBrush(self.background_image)
        self.scene.setBackgroundBrush(self.background_brush)
        

    #Zoom In/Out
    def wheelEvent(self,event):
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)
        
        current_position = self.mapToScene(event.pos())
        
        if event.angleDelta().y() > 0:
            zoom_factor = 1.1
        else:
            zoom_factor = 1/1.1
        self.scale(zoom_factor,zoom_factor)
        
        new_position = self.mapToScene(event.pos())
        
        
        delta = new_position - current_position
        self.translate(delta.x(),delta.y())
        
        

        
        
        

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = workspace()
    view.show()
    sys.exit(app.exec_())

