from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QFormLayout, QPushButton, QComboBox,
                             QSpinBox, QRadioButton, QCheckBox, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Score(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("MonsteraCare 1.0")
        self.setGeometry(20, 20, 400, 200)


class MCare(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.interface()

    def interface(self):
        label1 = QLabel("Place at house: ", self)
        label2 = QLabel("Watering: ", self)
        label2a = QLabel("every ", self)
        label2b = QLabel(" week(s)", self)
        label3 = QLabel("Soil fertilizing: ", self)
        label4 = QLabel("Air humidity: ", self)
        label5 = QLabel("Drainage: ", self)
        
        self.place = QComboBox()
        self.place.addItems(["on a windowsill", "near a window", "against the middle of a wall", "in a dark room without light"])
        self.watering = QSpinBox()
        self.watering.setRange(0, 4)
        self.fertilizing = QComboBox()
        self.fertilizing.addItems(["never", "once a week", "once a month for a whole year", "once a month in summer"])
        self.humidity1 = QRadioButton("low")
        self.humidity2 = QRadioButton("medium")
        self.humidity2.setChecked(True)
        self.humidity3 = QRadioButton("high")
        self.drainage = QCheckBox()
        self.drainage.setChecked(True)
        
        scheme = QFormLayout()
        scheme.addRow(label1, self.place)
        row2 = QHBoxLayout()
        row2.addWidget(label2a)
        row2.addWidget(self.watering)
        row2.addWidget(label2b)
        row2.addStretch()
        scheme.addRow(label2, row2)
        scheme.addRow(label3, self.fertilizing)
        row4 = QHBoxLayout()
        row4.addWidget(self.humidity1)
        row4.addWidget(self.humidity2)
        row4.addWidget(self.humidity3)
        row4.addStretch()
        scheme.addRow(label4, row4)
        row5 = QHBoxLayout()
        row5.addWidget(self.drainage)
        row5.addStretch()
        scheme.addRow(label5, row5)
        
        self.scoreBn = QPushButton("Score", self)
        self.endBn = QPushButton("Exit", self)
        empty = QLabel()
        buttons = QHBoxLayout()
        buttons.addWidget(self.scoreBn)
        buttons.addWidget(self.endBn)
        buttons.addStretch()
        scheme.addRow(empty, buttons)
        
        self.setLayout(scheme)
        self.endBn.clicked.connect(self.end)
        self.scoreBn.clicked.connect(self.scoring)
        self.setGeometry(20, 20, 400, 200)
        self.setWindowIcon(QIcon('monstera.png'))
        self.setWindowTitle("MonsteraCare 1.0")
        self.show()
    
    
    def end(self):
        self.close()
    
    
    def escKeyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    
    def scoring(self):
        self.result = Score()
        self.messages = []
        
        if self.place.currentText() == "near a window":
            self.messages.append("You have placed your monstera in a good area!")
        else:
            self.messages.append("You should place your plant near a window, remembering that monsteras don't like direct sunlight (it can harm them)")
        
        if self.watering.value() == 1 or self.watering.value() == 2:
            self.messages.append("You water your monstera very well!")
        else:
            self.messages.append("Watering your plant too often can lead to decay of roots whereas watering it too rarely can lead to death of it.\nTry to water your plant more/less often!")
        
        if self.fertilizing.currentText() == "once a month in summer":
            self.messages.append("It feels like your plant's soil is fertilized often enough!")
        else:
            self.messages.append("Fertilizing your plant too often or not at all can cause damages in your plant like chemical burn or malnutrition!\nThe best way is to fertilize your monstera once a month only in summer and when a winter comes, leave it alone.")
        
        if self.humidity3.isChecked() == True:
            self.messages.append("High air humidity is required for your monstera to grow properly! Great!")
        else:
            self.messages.append("Try to sprinkle your monstera's leaves with water! It'll thank you later!")
        
        if self.drainage.isChecked() == True:
            self.messages.append("Superb! Drainage is important to keep the monstera's roots away from the direct contact with water!")
        else:
            self.messages.append("Next time you transplant your plant, remember to buy some rocks to isolate roots from the water and prevent them\nfrom decaying!")
        
        layout = QGridLayout()
        for i, m in enumerate(self.messages):
            label = QLabel(m, self)
            layout.addWidget(label, i, 0)
        self.result.setLayout(layout)
        self.result.show()
        self.hide()       

        
if __name__ == '__main__':
    import sys
    
    app = QApplication.instance()
    if not app:  
        app = QApplication(sys.argv)
    window = MCare()
    app.exec_()