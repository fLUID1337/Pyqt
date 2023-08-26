from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QToolBar,QAction,QLabel,QPushButton, QSplitter,QHBoxLayout,QSlider
import sys
from PyQt5.QtGui import QPixmap,QIcon,QColor,QPainter,QFont,QPen,QBrush
import random
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart,QChartView,QPieSeries

class Pizza(QWidget):
    def __init__(self,):
        super().__init__()
        series=QPieSeries()
        series.append("тесто",39)
        series.append("томатная паста",50)
        series.append("пеперони",4)
        series.append("сыр",5)
        series.append("любовь",2)
        series.setHoleSize(0)
        slice=series.slices()[3]
        slice.setLabelVisible(True)
        slice.setPen(QPen(QColor("yellow"),2))
        slice.setBrush(QColor("yellow"))
        slice.setExploded(True)
        chart=QChart()
        chart.addSeries(series)
        chart.setTitle("Пицца")
        chart.setTheme(QChart.ChartThemeLight)
        chart.setAnimationOptions(QChart.AllAnimations)
        qchart=QChartView(chart)
        layout=QHBoxLayout()
        layout.addWidget(qchart)
        self.setLayout(layout)
        self.show()
                    
        
        
a = QApplication(sys.argv)
d = Pizza()
sys.exit(a.exec())                 
        