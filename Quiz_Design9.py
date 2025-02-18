questions_and_answers = {
    "What is the capital of France?": ("Paris", ["Berlin", "Madrid", "Rome"]),
    "What is 2 + 2?": ("4", ["3", "5", "6"]),
    "What color is the sky on a clear day?": ("Blue", ["Red", "Green", "Yellow"]),
    "What is the largest mammal?": ("Blue Whale", ["Elephant", "Giraffe", "Hippopotamus"]),
    "Which continent is Egypt in?": ("Africa", ["Asia", "Europe", "South America"]),
    "What is the boiling point of water?": ("100°C", ["0°C", "50°C", "150°C"]),
    "What is the square root of 64?": ("8", ["6", "7", "9"]),
    "Which planet is known as the Red Planet?": ("Mars", ["Venus", "Jupiter", "Saturn"]),
    "How many continents are there?": ("7", ["5", "6", "8"]),
    "Who wrote 'Romeo and Juliet'?": ("William Shakespeare", ["Charles Dickens", "Mark Twain", "Jane Austen"]),
    "What is the tallest mountain in the world?": ("Mount Everest", ["K2", "Kilimanjaro", "Denali"]),
    "What is the capital of Japan?": ("Tokyo", ["Beijing", "Seoul", "Bangkok"]),
    "Which animal is known as the King of the Jungle?": ("Lion", ["Tiger", "Leopard", "Cheetah"]),
    "What is the smallest country in the world?": ("Vatican City", ["Monaco", "San Marino", "Liechtenstein"]),
    "What is the national sport of Canada?": ("Ice Hockey", ["Baseball", "Soccer", "Basketball"]),
    "What is the currency of the United States?": ("Dollar", ["Euro", "Pound", "Yen"]),
    "Who painted the Mona Lisa?": ("Leonardo da Vinci", ["Pablo Picasso", "Vincent van Gogh", "Claude Monet"]),
    "What is the capital of the United Kingdom?": ("London", ["Edinburgh", "Dublin", "Manchester"]),
    "Which gas do plants absorb from the atmosphere?": ("Carbon Dioxide", ["Oxygen", "Nitrogen", "Hydrogen"]),
    "What is the largest ocean on Earth?": ("Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]),
    "What is the main ingredient in guacamole?": ("Avocado", ["Tomato", "Lettuce", "Cucumber"]),
    "Which country is famous for tulips and windmills?": ("Netherlands", ["Belgium", "Denmark", "Switzerland"]),
    "What is the largest desert in the world?": ("Sahara Desert", ["Gobi Desert", "Atacama Desert", "Kalahari Desert"]),
    "What is the longest river in the world?": ("Amazon River", ["Nile River", "Yangtze River", "Mississippi River"]),
    "Which planet is closest to the sun?": ("Mercury", ["Venus", "Mars", "Neptune"]),
    "What is the main language spoken in Brazil?": ("Portuguese", ["Spanish", "French", "Italian"]),
    "What is the largest island in the world?": ("Greenland", ["Madagascar", "Borneo", "New Guinea"]),
    "How many hours are in a day?": ("24", ["12", "36", "48"]),
    "What is the capital of Australia?": ("Canberra", ["Sydney", "Melbourne", "Brisbane"]),
    "Which fruit is known as the 'king of fruits'?": ("Durian", ["Mango", "Pineapple", "Banana"]),
    "What is the chemical symbol for water?": ("H2O", ["CO2", "O2", "H2"]),
    "Which country is known as the Land of the Rising Sun?": ("Japan", ["China", "South Korea", "Thailand"]),
    "How many legs does a spider have?": ("8", ["6", "10", "12"]),
    "What is the hardest natural substance on Earth?": ("Diamond", ["Gold", "Iron", "Platinum"]),
    "What is the largest country by area?": ("Russia", ["Canada", "China", "United States"]),
    "What is the capital of Italy?": ("Rome", ["Milan", "Venice", "Florence"]),
    "What is the color of an emerald?": ("Green", ["Blue", "Red", "Yellow"]),
    "Who invented the light bulb?": ("Thomas Edison", ["Nikola Tesla",   "Alexander Graham Bell", "Albert Einstein"]),
    "What is the official language of China?": ("Mandarin", ["Cantonese", "Korean", "Japanese"]),
    "What is the capital of Canada?": ("Ottawa", ["Toronto", "Vancouver", "Montreal"]),
    "Who is the Greek god of thunder?": ("Zeus", ["Apollo", "Poseidon", "Ares"]),
    "How many players are there in a soccer team?": ("11", ["10", "12", "13"]),
    "Which month has 28 days?": ("February", ["January", "March", "April"]),
    "What is the capital of Germany?": ("Berlin", ["Hamburg", "Munich", "Frankfurt"]),
    "Which bird is known for its colorful feathers and ability to mimic sounds?": ("Parrot", ["Peacock", "Eagle", "Sparrow"]),
    "Who was the first president of the United States?": ("George Washington", ["Abraham Lincoln", "John Adams", "Thomas Jefferson"]),
    "What is the smallest bone in the human body?": ("Stapes", ["Femur", "Radius", "Ulna"]),
    "What is the capital of Spain?": ("Madrid", ["Barcelona", "Seville", "Valencia"]),
    "What is the largest country by population?": ("China", ["India", "United States", "Indonesia"]),
    "Which animal can sleep for three years?": ("Snail", ["Bear", "Frog", "Turtle"]),
    "Who discovered gravity?": ("Isaac Newton", ["Albert Einstein", "Galileo Galilei", "Johannes Kepler"]),
    "What is the fastest land animal?": ("Cheetah", ["Leopard", "Horse", "Jaguar"]),
    "Who was the first man to walk on the moon?": ("Neil Armstrong", ["Buzz Aldrin", "Yuri Gagarin", "Michael Collins"]),
    "Which animal is known for its black and white stripes?": ("Zebra", ["Tiger", "Panda", "Skunk"]),
    "Which city is known as the Big Apple?": ("New York City", ["Los Angeles", "Chicago", "Miami"]),
    "What is the currency of Japan?": ("Yen", ["Won", "Peso", "Rupee"]),
    "Which planet is known for its rings?": ("Saturn", ["Jupiter", "Uranus", "Neptune"]),
    "Which country invented pizza?": ("Italy", ["France", "Greece", "Spain"]),
    "What is the national flower of Japan?": ("Cherry Blossom", ["Rose", "Lotus", "Tulip"]),
}


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QScrollArea
from PyQt6.QtCore import Qt
import sys
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.556818, y1:0, x2:0.533, y2:1, stop:0.357955 rgba(109, 185, 213, 255), stop:1 rgba(116, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 401, 101))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setVisible(False)
        self.textEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("color: black;")
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 431, 301))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.textEdit.setFont(font)
        self.value = 0
        self.count = 0
        self.textEdit.setStyleSheet("QTextEdit{\n"
"border: 5px solid #2e3b5f;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 310, 349, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFD700, stop:1 #FFC300); \n"
"    color: White;  \n"
"    border: 2px solid #CC9C00;  \n"
"    border-radius: 10px;  \n"
"    padding: 8px 15px;  \n"
"\n"
"    font-family: \"Arial\";  \n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFEA00, stop:1 #FFD700); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFC300, stop:1 #FFB000); \n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 349, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFD700, stop:1 #FFC300); \n"
"    color: White;  \n"
"    border: 2px solid #CC9C00;  \n"
"    border-radius: 10px;  \n"
"    padding: 8px 15px;  \n"
"\n"
"    font-family: \"Arial\";  \n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFEA00, stop:1 #FFD700); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFC300, stop:1 #FFB000); \n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 190, 349, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFD700, stop:1 #FFC300); \n"
"    color: White;  \n"
"    border: 2px solid #CC9C00;  \n"
"    border-radius: 10px;  \n"
"    padding: 8px 15px;\n"
"\n"
"    \n"
"    font-family: \"Arial\";  \n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-style: italic;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFEA00, stop:1 #FFD700); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFC300, stop:1 #FFB000); \n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 230, 349, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFD700, stop:1 #FFC300); \n"
"    color: White;  \n"
"    border: 2px solid #CC9C00;  \n"
"    border-radius: 10px;  \n"
"    padding: 8px 15px;\n"
"\n"
"    \n"
"    font-family: \"Arial\";  \n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-style: italic;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFEA00, stop:1 #FFD700); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFC300, stop:1 #FFB000); \n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 270, 349, 41))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFD700, stop:1 #FFC300); \n"
"    color: White;  \n"
"    border: 2px solid #CC9C00;  \n"
"    border-radius: 10px;  \n"
"    padding: 8px 15px;  \n"
"\n"
"    font-family: \"Arial\";  \n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFEA00, stop:1 #FFD700); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFC300, stop:1 #FFB000); \n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 61, 31))
        self.label_2.setText(f'{self.value}')
        self.label_2.setStyleSheet("QLabel {\n"
"    border: 2px solid #B8860B; \n"
"    background-color: yellow;\n"
"    border-radius: 10px; \n"
"    padding: 5px; \n"
"    font-size: 16px; \n"
"    font-weight: bold; \n"
"    text-align: center;\n"
"    color: black;"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "General Quiz Game"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; font-style:italic; color:#ffffff;\">General Quiz Game</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "EXIT"))
        self.pushButton.setText(_translate("MainWindow", "Play"))
        self.pushButton_4.setText(_translate("MainWindow", "Help"))
        self.pushButton_2.setText(_translate("MainWindow", "Option 3"))
        self.pushButton_5.setText(_translate("MainWindow", "Option 4"))
        self.pushButton.clicked.connect(self.play_button_clicked)
        self.pushButton_4.clicked.connect(self.help_button)
        self.pushButton_3.clicked.connect(self.extit_button_clicked)
        self.pushButton_2.hide()
        self.pushButton_5.hide()
        self.pushButton_3.hide()

    def help_button(self):
        self.textEdit.setVisible(True)
        self.pushButton_5.setVisible(False)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(True)
        self.pushButton_4.setVisible(False)
        
        if self.pushButton_4.text() == "Help":
                self.textEdit.setVisible(True)
        else:
                self.textEdit.setVisible(False)
                self.pushButton_3.hide()
                self.pushButton.setVisible(True)
                self.pushButton_5.setVisible(True)
                self.pushButton_4.setVisible(True)
                self.pushButton_2.setVisible(True)
        
        self.textEdit.setText("""General Instructions:

"Welcome to the quiz game! Answer the questions correctly to score points."
1."Each question answered correctly earns you one point."
2."Choose the most appropriate answer from the 3 or 4 options provided."
3."If you score 7 or more points, you can proceed to the next round."

Round Progression:

1."You need a minimum of 7 points to proceed to the next round."
2."Good luck, and aim for a high score to unlock more rounds!"

Game Rules:

1."Answer each question by selecting the correct option."
2."You cannot skip questions. Choose wisely!""")
    def play_button_clicked(self):
        self.count = 0 
        self.value = 0 
        self.label_2.setText("0") 
        
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(True)
        self.pushButton_5.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.pushButton.setVisible(True)
        self.label_2.setVisible(True)
        
        push_button_font = QtGui.QFont()
        push_button_font.setPointSize(16)
        push_button_font.setBold(True)
        self.pushButton.setFont(push_button_font)

        buttons = [self.pushButton_5, self.pushButton_4, self.pushButton_2, self.pushButton]
        for button in buttons:
                try:
                        button.clicked.disconnect()
                except TypeError:
                        pass  # Ensures it doesn't crash if no previous connection exists

        # Connect buttons to check_answer
        for button in buttons:
                button.clicked.connect(lambda _, btn=button: self.check_answer(btn))


        self.load_next_question()

        
    def extit_button_clicked(self):
            self.textEdit.setVisible(False)
            self.pushButton_3.setVisible(False)
            self.pushButton.setVisible(True)
            self.pushButton_4.setVisible(True)
    def check_answer(self, button):
        if button.text() == self.correct_answer:
                self.value += 1  
        self.label_2.setText(f'{self.value}')

        if self.count < 10:  # Ensures game stops properly
                self.load_next_question()

        
    def load_next_question(self):
        self.random_Question = random.choice(list(questions_and_answers.keys()))
        self.correct_answer, self.wrong_answer = questions_and_answers[self.random_Question]
        self.label.setText(f'{self.random_Question}')
        
        all_answers = [self.correct_answer] + self.wrong_answer
        random.shuffle(all_answers)
        
        self.pushButton.setText(all_answers[0])  
        self.pushButton_4.setText(all_answers[1])
        self.pushButton_5.setText(all_answers[2])
        self.pushButton_2.setText(all_answers[3])
        self.count += 1
        if self.count >= 10:
                self.pushButton_2.hide()
                self.pushButton_4.hide()
                self.pushButton_5.hide()
                self.pushButton.hide()
                self.label_2.hide()
                self.label.setText(f'Final Score: {self.value}')
                
                self.pushButton_3.setText('Play Again')
                self.pushButton_3.setVisible(True)

                try:
                        self.pushButton_3.clicked.disconnect()
                except TypeError:
                        pass  

                self.pushButton_3.clicked.connect(self.play_button_clicked)
                return  # Ensures function stops executing here


if __name__ == "__main__":      
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print(ui.count)
    sys.exit(app.exec())
    