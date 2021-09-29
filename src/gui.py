from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

import sys

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())