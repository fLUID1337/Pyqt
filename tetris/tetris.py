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
        self.tboard = Board(self)
        self.tboard.start()
        self.setCentralWidget(self.tboard)
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
        self.score_label.setText(str(self.score))
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
        self.clear_board()
    
    def shape_At(self,x,y):
        return self.board[(y*Board.board_width)+x] 
    
    def setShapeAt(self,x,y,shape):
        self.board[(y * Board.board_width) + x ] = shape
        
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
    
    def try_move(self,newPiece,newX,newY):
        for i in range(4): 
            
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i) 
            
            if x < 0 or x >= Board.board_width or y < 0 or y >= Board.board_height:
                return False
            if self.shape_At(x,y) != Tetraminoe.no_shape:
                return False
            
        self.cur_piece = newPiece
        self.cur_x= newX    
        self.cur_y = newY    
        self.update()
        
        return True
    
    def timerEvent(self,event):
        
        if event.timerId() == self.timer.timerId():
            
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.new_piece()
            else:
                self.one_line_down()
                
        else:
            super(Board,self).timerEvent(event)   
            
    def clear_board(self):
        
        for i in range(Board.board_height * Board.board_width):
            self.board.append(Tetraminoe.no_shape)
    
    def remove_full_lines(self):
 
        
        num_full_lines=0
        row_to_removes=[]
        
        for i in range(Board.board_height):
            n=0
            for j in range(Board.board_width):
                if not self.shape_At(j,i) == Tetraminoe.no_shape:
                    n += 1   
            if n == 10:
                row_to_removes.append(i)                            
        row_to_removes.reverse()
        for g in row_to_removes:
            for k in range(g,Board.board_height):
                for l in range(Board.board_width):
                    self.setShapeAt(l,k,self.shape_At(l,k+1))    
        num_full_lines += len(row_to_removes)
        if num_full_lines >0:
            self.numLinesRemoved += num_full_lines
            self.score_label.setText(f"{self.numLinesRemoved}")  
            self.isWaitingAfterLine = True
            self.cur_piece.setShape(Tetraminoe.no_shape)
            self.update() 
            
    def new_piece(self):
        self.cur_piece = Shape()
        self.cur_piece.set_random_shape()
        self.cur_x = Board.board_width // 2 + 1   
        self.cur_y = Board.board_height - 1 + self.cur_piece.min_y()
        
        if not self.try_move(self.cur_piece,self.cur_x,self.cur_y):
            self.cur_piece.setShape(Tetraminoe.no_shape)
            self.timer.stop()
            self.isStarted = False
            self.game_over()            
                                   
    def draw_square(self,painter:QPainter,x,y,shape):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1,self.square_width() - 2,self.square_height() - 2,color)
        painter.setPen(color.lighter())
        painter.drawLine(x,y + self.square_height() - 1,x,y)
        painter.drawLine(x,y,x + self.square_width() - 1,y)
        painter.setPen(color.darker())
        painter.drawLine(x + 1,y + self.square_height() - 1,x + self.square_width() - 1,y + self.square_height() - 1)
        painter.drawLine(x + self.square_width() - 1,y + 1,x + self.square_width() - 1,y + self.square_height() - 1)

    def drop_down(self):
        new_y = self.cur_y
        while new_y > 0:
            if not self.try_move(self.cur_piece,self.cur_x,new_y - 1):
                break
            new_y -= 1
        self.piece_dropped()
        
    def piece_dropped(self):
        for i in range(4):
            x = self.cur_x + self.cur_piece.x(i)
            y = self.cur_y - self.cur_piece.y(i)
            self.setShapeAt(x,y,self.cur_piece.shape())
        self.remove_full_lines()
        if not self.isWaitingAfterLine:
            self.new_piece()
    
    def one_line_down(self):
        if not self.try_move(self.cur_piece,self.cur_x,self.cur_y - 1):
            self.piece_dropped()
                       
    def start(self):
        if self.isPaused:
            return
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clear_board()
        
        self.score_label.setText(str(self.numLinesRemoved))
        self.new_piece()
        self.timer.start(Board.speed,self)
        
    def paused(self):
        if not self.isStarted:
            return
        self.isPaused = not self.isPaused
        if self.isPaused:
            self.timer.stop()
            self.score_label.setText("Пауза")
        else:
            self.score_label.setText(str(self.numLinesRemoved))
            self.timer.start(Board.speed,self) 
    
    def game_over(self):
        self.setWindowTitle("Вы проиграли!")                                   
        
        
    def paintEvent(self,event):
        painter=QPainter(self)
        rect=self.contentsRect()
        board_Top=rect.bottom()-Board.board_height*self.square_height()
        
        for i in range(Board.board_height):
            for j in range(Board.board_width):
                shape=self.shape_At(j,Board.board_height-i-1)
                if shape!=Tetraminoe.no_shape:
                    self.draw_square(painter,rect.left()+j*self.square_width(),board_Top+i*self.square_height(),shape)
        if self.cur_piece.shape()!=Tetraminoe.no_shape:
            for i in range(4):
                x=self.cur_x + self.cur_piece.x(i)
                y=self.cur_y - self.cur_piece.y(i)
                self.draw_square(painter,rect.left()+x*self.square_width(),board_Top+(Board.board_height - y - 1) * self.square_height(),self.cur_piece.shape())
                
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
        

    def set_random_shape(self):
        self.setShape(random.randint(1, 7))
        
    def x(self, index):
        return self.coords[index][0]
    
    def y(self, index):
        return self.coords[index][1]
    
    def set_x(self, index, x):
        self.coords[index][0] = x
        
    def set_y(self, index, y):
        self.coords[index][1] = y

    def min_x(self):
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
            return m
        
    def max_x(self):
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])
            return m 
    
    def min_y(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
            return m
        
    def max_y(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
            return m         
    
    
    def rotate_left(self):
        if self.piece_shape == Tetraminoe.square_shape:
            return self
        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.set_x(i, self.y(i))
            result.set_y(i, -self.x(i))
        return result
    
    def rotate_right(self):
        if self.piece_shape == Tetraminoe.square_shape:
            return self
        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.set_x(i, -self.y(i))
            result.set_y(i, self.x(i))
        return result
       
if __name__=="__main__":
    a = QApplication(sys.argv)
    d = Tetris("tetris")
    sys.exit(a.exec())            