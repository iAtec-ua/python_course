from PySide2.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QHBoxLayout()  # HORIZONTAL BOX LAYOUT
label = QLabel('(㇏(•̀ᵥᵥ•́)ノ)')
button_1 = QPushButton("One Button")
button_2 = QPushButton("Two Button")
button_3 = QPushButton("Three Button")
layout.addWidget(label)
layout.addWidget(button_1)
layout.addWidget(button_2)
layout.addWidget(button_3)
window.setLayout(layout)
window.show()
app.exec_()
