""" Game: Piggy Peppa and her happy family """

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtCore import *
import sys

# global vars
peppa_george_ball = '../piggy_peppa_gifs/peppa_george_playing_ball.gif'
peppa_george_jumping = '../piggy_peppa_gifs/peppa_george_jumping.gif'
peppa_eating = '../piggy_peppa_gifs/peppa_eating.gif'
george_eating = '../piggy_peppa_gifs/george_eating.gif'
george_cry = '../piggy_peppa_gifs/george_cry.gif'
family_jumping = '../piggy_peppa_gifs/family_jumping.gif'
family_happiness = '../piggy_peppa_gifs/family_happiness.gif'


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Init game window
        self.resize(900, 800)
        self.setWindowTitle('小猪佩奇游戏')

        from PyQt5.QtGui import QFont
        font_title = QFont()
        font_title.setPointSize(32)
        font_title.setBold(True)

        self.title = QLabel('小猪佩奇开心一家', self)
        self.title.setGeometry(200, 50, 500, 100)
        self.title.setFont(font_title)

        # Game content containers
        font_content = QFont()
        font_content.setPointSize(32)
        font_content.setBold(True)
        self.gif_content = QLabel('哈喽，你好，\n      我是小猪佩奇!', self)
        self.gif_content.setFont(font_content)
        self.gif_content.setGeometry(150, 230, 600, 500)
        self.gif_content.setStyleSheet('border: 2px solid black')

        # Game buttons
        self.btn_peppa_george_playing_ball = QPushButton('佩奇乔治玩球', self)
        self.btn_peppa_george_jumping = QPushButton('佩奇乔治跳跳', self)
        self.btn_peppa_eating = QPushButton('佩奇吃吃', self)
        self.btn_george_eating = QPushButton('乔治吃吃', self)
        self.btn_george_cry = QPushButton('乔治哭泣', self)
        self.btn_family_jumping = QPushButton('佩奇全家跳跳', self)
        self.btn_family_happiness = QPushButton('佩奇开心全家', self)

        self.btn_peppa_george_playing_ball.move(50, 170)
        self.btn_peppa_george_jumping.move(160, 170)
        self.btn_peppa_eating.move(270, 170)
        self.btn_george_eating.move(380, 170)
        self.btn_george_cry.move(490, 170)
        self.btn_family_jumping.move(600, 170)
        self.btn_family_happiness.move(710, 170)

        # Game roles
        self.gif_peppa_george_playing_ball = QPixmap(peppa_george_ball)
        self.gif_peppa_george_jumping = QPixmap(peppa_george_jumping)
        self.gif_peppa_eating = QPixmap(peppa_eating)
        self.gif_george_eating = QPixmap(george_eating)
        self.gif_george_cry = QPixmap(george_cry)
        self.gif_family_jumping = QPixmap(family_jumping)
        self.gif_family_happiness = QPixmap(family_happiness)

        # signals and slots between all buttons and funcations
        self.btn_peppa_george_playing_ball.clicked.connect(self.run)
        self.btn_peppa_george_jumping.clicked.connect(self.run)
        self.btn_peppa_eating.clicked.connect(self.run)
        self.btn_george_eating.clicked.connect(self.run)
        self.btn_george_cry.clicked.connect(self.run)
        self.btn_family_jumping.clicked.connect(self.run)
        self.btn_family_happiness.clicked.connect(self.run)

        # show all
        self.show()

    # slot functions
    def run(self):
        from PyQt5.QtGui import QMovie
        # peppa_george_ball
        if self.sender() == self.btn_peppa_george_playing_ball:
            self.set_pix_for_label(peppa_george_ball)
            self.movie = QMovie(peppa_george_ball)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

        # peppa_george_jumping
        if self.sender() == self.btn_peppa_george_jumping:
            self.set_pix_for_label(peppa_george_jumping)
            self.movie = QMovie(peppa_george_jumping)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

        # peppa_eating
        if self.sender() == self.btn_peppa_eating:
            self.set_pix_for_label(peppa_eating)
            self.movie = QMovie(peppa_eating)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

        # george_eating
        if self.sender() == self.btn_george_eating:
            self.set_pix_for_label(george_eating)
            self.movie = QMovie(george_eating)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

        # george_cry
        if self.sender() == self.btn_george_cry:
            self.set_pix_for_label(george_cry)
            self.movie = QMovie(george_cry)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

        # family jumping
        if self.sender() == self.btn_family_jumping:
            self.set_pix_for_label(family_jumping)
            self.movie = QMovie(family_jumping)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

        # family_happiness
        if self.sender() == self.btn_family_happiness:
            self.set_pix_for_label(family_happiness)
            self.movie = QMovie(family_happiness)
            self.gif_content.setMovie(self.movie)
            self.movie.start()

    # helper functions
    def set_pix_for_label(self, gif_file):
        pix = QPixmap(gif_file)
        self.gif_content.setPixmap(pix)
        self.gif_content.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())
