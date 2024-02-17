import sys,random
from PyQt5.QtWidgets import QMainWindow,QFrame,QLabel,QApplication
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPainter,QColor

class Tetris(QMainWindow):
    def __init__(self,name):
        super().__init__()
        self.tboard=None
        self.name=name
        self.initUi()
        
    def initUi(self):
        self.setFixedSize(360,760)
        self.setWindowTitle(self.name)
        self.show()
  
class Board(QFrame):
    board_width=10
    board_height=20
    speed=300
    
    def __init__(self,parent):
        super().__init__(parent)
        self.score=0  
        self.score_label=QLabel(self)
        self.score_label.setGeometry(0,0,200,10)
        self.score_label.setText(self.score)
        self.init_Board()
    
    def init_Board(self):
        self.timer=QBasicTimer()
        self.isWaitingAfterLine=False
        self.cur_x=0
        self.cur_y=0   
        self.numLinesRemoved=0
        self.board=[] 
        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted=False
        self.isPaused=False
    
    def shapeAt(self,x,y):
        return self.board[(y*Board.board_width)+x] 
        
    def square_width(self):
        return self.contentsRect().width()//Board.board_width
    
    def square_height(self):
        return self.contentsRect().height()//Board.board_height
    
    def keyPressEvent(self,event):
        if not self.isStarted or self.cur_piece.shape() == Tetraminoe.no_shape:
            super(Board,self).keyPressEvent(event)
            return
        key = event.key()  
        
        if key == Qt.Key_P:
            self.paused()
            return
        
        if self.isPaused:
            return
        elif key == Qt.Key_Left:
            self.try_move(self.cur_piece,self.cur_x - 1,self.cur_y)
            
        elif key == Qt.Key_Right:
            self.try_move(self.cur_piece,self.cur_x + 1,self.cur_y)  
            
        elif key == Qt.Key_Up:
            self.try_move(self.cur_piece.rotate_left(),self.cur_x,self.cur_y)
            
        elif key == Qt.Key_Down:
            self.try_move(self.cur_piece.rotate_right(),self.cur_x,self.cur_y)
            
        elif key == Qt.Key_Space:
            self.drop_down()
            
        elif key == Qt.Key_D:
            self.one_line_down()
            
        else:
            super(Board,self).keyPressEvent(event)
    
    def tryMove(self,newPiece,newX,newY):
        for i in range(4): 
            
            x = newX + newPiece.x(i)
            y = newY + newPiece.y(i) 
            
            if x < 0 or x >= Board.board_width or y < 0 or y >= Board.board_height:
                return False
            if self.shapeAt(x,y) != Tetraminoe.no_shape:
                return False
            
        self.cur_piece = newPiece
        self.cur_x = newX    
        self.cur_y = newY    
        self.update()
        
        return True
    
    def timerEvent(self,event):
        
        if event.timerId() == self.timer.timerId():
            
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
                
        else:
            super(Board,self).timerEvent(event)   
            
    def clearBoard(self):
        
        for i in range(Board.board_height * Board.board_width):
            self.board.append(Tetraminoe.no_shape)
    
    def remove_full_lines(self):
 
        
        num_full_lines=0
        row_to_removes=[]
        
        for i in range(Board.board_height):
            n=0
            for j in range(Board.board_width):
                if not self.shapeAt(j,i) == Tetraminoe.no_shape:
                    n += 1   
            if n == 10:
                row_to_removes.append(i)                            
        row_to_removes.reverse()
        for g in row_to_removes:
            for k in range(g,Board.board_height):
                for l in range(Board.board_width):
                    self.setshapeAt(l,k,self.shapeAt(l,k+1))    
        num_full_lines += len(row_to_removes)
        if num_full_lines >0:
            self.numLinesRemoved += num_full_lines
            self.score_label.setText(f"{self.numLinesRemoved}")  
            self.isWaitingAfterLine = True
            self.cur_piece.setShape(Tetraminoe.no_shape)
            self.update() 
            
    def newPiece(self):
        self.cur_piece = Shape()
        self.cur_piece.setRandomShape()
        self.cur_x = Board.board_width // 2 + 1   
        self.cur_y = Board.board_height - 1 + self.cur_piece.min_y()
        if not self.tryMove(self.cur_piece,self.cur_x,self.cur_y):
            self.cur_piece.setShape(Tetraminoe.no_shape)
            self.timer.stop()
            self.isStarted = False
            self.gameover()            
                                   
        
    # def paintEvent(self,event):
    #     painter=QPainter(self)
    #     rect=self.contentsRect()
    #     board_Top=rect.bottom()-Board.board_height*self.square_height()
        
    #     for i in range(Board.board_height):
    #         for j in range(Board.board_width):
    #             shape=self.shapeAt(j,Board.board_height-i-1)
    #             if shape!=Tetraminoe.no_shape:
    #                 self.drawSquare(painter,rect.left()+j*self.square_width(),board_Top+i*self.square_height(),shape)
    #     if self.cur_piece.shape()!=Tetraminoe.no_shape:
    #         for i in range(4):
    #             x=self.cur_x + self.cur_piece.x(i)
    #             y=self.cur_y - self.cur_piece.y(i)
    #             self.drawSquare(painter,rect.left()+x*self.square_width(),board_Top+y*self.square_height(),self.cur_piece.shape())
                
class Tetraminoe(object):
    no_shape = 0
    zshape = 1                            
    sshape = 2
    line_shape = 3
    tshape = 4
    square_shape = 5
    lshape_shape = 6
    mirorred_l_shape = 7
    

class Shape():
    coordsTable = (
      ((0, 0), (0, 0), (0, 0), (0, 0)),
      ((0, -1), (0, 0), (-1, 0), (-1, 1)),
      ((0, -1), (0, 0), (1, 0), (1, 1)),
      ((0, -1), (0, 0), (0, 1), (0, 2)),
      ((-1, 0), (0, 0), (1, 0), (0, 1)),
      ((0, 0), (1, 0), (0, 1), (1, 1)),
      ((-1, -1), (0, -1), (0, 0), (0, 1)),
      ((1, -1), (0, -1), (0, 0), (0, 1))
  )
    def __init__(self):
        self.coords = [[0,0] for i in range(4)]
        self.piece_shape = Tetraminoe.no_shape
        self.setShape(Tetraminoe.no_shape)
    
    def shape(self):
        return self.piece_shape 
    
    def setShape(self,shape):
        table = Shape.coordsTable[shape]
        for i in range(4):
            self.coords[i][0],self.coords[i][1] = table[i][0],table[i][1] 
        self.piece_shape = shape        
        

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))
        
    def x(self, index):
        return self.coords[index][0]
    
    def y(self, index):
        return self.coords[index][1]
    
    def setX(self, index, x):
        self.coords[index][0] = x
        
    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
            return m
        
    def maxX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])
            return m 
    
    def minY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
            return m
        
    def maxY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
            return m         
    
    
    def rotateLeft(self):
        if self.piece_shape == Tetraminoe.square_shape:
            return self
        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
        return result
    
    def rotateRight(self):
        if self.piece_shape == Tetraminoe.square_shape:
            return self
        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
        return result
       
if __name__=="__main__":
    a = QApplication(sys.argv)
    d = Tetris("tetris")
    sys.exit(a.exec())            