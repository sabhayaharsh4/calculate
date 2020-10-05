import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5')
window.setGeometry(100, 100, 280, 80)
window.move(600, 15)
helloMsg = QLabel('Testing', parent=window)
helloMsg.move(50, 40)

window.show()

sys.exit(app.exec_())
