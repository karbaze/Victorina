#Main_Window

from PyQt6.QtCore import*
from PyQt6.QtWidgets import*

window_main = QWidget()
window_main_layout = QVBoxLayout()


# WIGETS #

Menu_Pbtn = QPushButton("Налаштування")
Rest_Pbtn = QPushButton("Відпочинок")
Give_Answer_Pbtn = QPushButton("Відповісти")

Rest_Sbox = QSpinBox()
Rest_Sbox.setValue(30)

Ans1_Rbtn = QRadioButton("Answer1")
Ans2_Rbtn = QRadioButton("Answer2")
Ans3_Rbtn = QRadioButton("Answer3")
Ans4_Rbtn = QRadioButton("Answer4")

Question_Lbl = QLabel("Question")
Minutes_Lbl = QLabel("Хвилин")
Result_lbl = QLabel("Правильна відповідь")

Answers_Gbox = QGroupBox()
Result_Gbox = QGroupBox()

# layout

Header_layout = QHBoxLayout()

Answers_Gbox_layout = QVBoxLayout()
Result_Gbox_layout = QVBoxLayout()

Answer_buttons_row1 = QHBoxLayout()
Answer_buttons_row2 = QHBoxLayout()

Header_layout.addWidget(Menu_Pbtn)
Header_layout.addWidget(Rest_Pbtn)
Header_layout.addWidget(Rest_Sbox)
Header_layout.addWidget(Minutes_Lbl)
window_main_layout.addLayout(Header_layout)

window_main_layout.addWidget(Question_Lbl)

Answer_buttons_row1.addWidget(Ans1_Rbtn)
Answer_buttons_row1.addWidget(Ans2_Rbtn)                        

Answer_buttons_row2.addWidget(Ans3_Rbtn)
Answer_buttons_row2.addWidget(Ans4_Rbtn)

Answers_Gbox_layout.addLayout(Answer_buttons_row1)
Answers_Gbox_layout.addLayout(Answer_buttons_row2)

Answers_Gbox.setLayout(Answers_Gbox_layout)
window_main_layout.addWidget(Answers_Gbox)

Result_Gbox_layout.addWidget(Result_lbl)
Result_Gbox.setLayout(Result_Gbox_layout)
window_main_layout.addWidget(Result_Gbox)

window_main_layout.addWidget(Give_Answer_Pbtn)


window_main.setLayout(window_main_layout)