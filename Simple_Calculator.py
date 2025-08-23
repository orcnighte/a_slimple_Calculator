from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout
import sys
import re

def safe_eval(expr):
    
    if re.fullmatch(r'[0-9+\-*/. ]+', expr):
        try:
            return str(eval(expr))
        except:
            return "Error"
    return "Error"

app = QApplication(sys.argv)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        
    
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setPlaceholderText("0")
        
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        
        
        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)
        ]
        
        for text, row, col, *span in buttons:
            button = QPushButton(text)
            if span:
                grid_layout.addWidget(button, row, col, *span)
            else:
                grid_layout.addWidget(button, row, col)
            button.clicked.connect(self.evaluation_function)
        
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)
    
    def evaluation_function(self):
        text = self.sender().text()
        if text == "C":
            self.display.clear()
        elif text == "=":
            self.display.setText(safe_eval(self.display.text()))
        else:
            self.display.setText(self.display.text() + text)


window = Calculator()
window.show()

sys.exit(app.exec())
