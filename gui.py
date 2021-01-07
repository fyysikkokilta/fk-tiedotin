#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
        QRadioButton, QHBoxLayout, QVBoxLayout, QStyleFactory, QLineEdit,
        QTextEdit, QLabel, QPushButton, QTabWidget, QWidget, QButtonGroup,
        QDateEdit, QCheckBox, QShortcut, QTextBrowser)
from utils import save_entry


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.createCategorySelectionGroupBox()
        self.createTextEditLayout()
        self.createButtonLayout()

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.categorySelectionLayout, 0, 0)
        mainLayout.addLayout(self.textEditLayout, 1, 0)
        mainLayout.addLayout(self.buttonLayout, 2, 0)
        self.setLayout(mainLayout)

        QApplication.setStyle(QStyleFactory.create("cleanlooks"))
        self.setWindowTitle("FK-tiedotin")
        self.setWindowIcon(QtGui.QIcon('templates/fi.png'))

        # Always-on-top mode. Currently does not work on Windows.
        #alwaysOnTopShortcut = QShortcut(QtGui.QKeySequence("Ctrl+O"), self)
        #alwaysOnTopShortcut.activated.connect(lambda:
        #    super(MainWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint))

    def createCategorySelectionGroupBox(self):
        self.languageCheckBox = QCheckBox("Text in English", self)
        self.languageCheckBox.stateChanged.connect(self.languageCheckBoxClicked)

        self.toBothBulletinsCheckBox = QCheckBox("Add to both versions", self)

        categorySelectionGroupBox = QGroupBox("Category")
        self.categorySelectionButtonGroup = QButtonGroup()

        self.radioButton1 = QRadioButton("Killan tapahtumat")
        self.radioButton2 = QRadioButton("Muut tapahtumat")
        self.radioButton3 = QRadioButton("Yleistä")
        self.radioButton4 = QRadioButton("Opinnot")
        self.radioButton1.setChecked(True)

        self.categorySelectionButtonGroup.addButton(self.radioButton1)
        self.categorySelectionButtonGroup.addButton(self.radioButton2)
        self.categorySelectionButtonGroup.addButton(self.radioButton3)
        self.categorySelectionButtonGroup.addButton(self.radioButton4)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.radioButton1)
        buttonLayout.addWidget(self.radioButton2)
        buttonLayout.addWidget(self.radioButton3)
        buttonLayout.addWidget(self.radioButton4)
        categorySelectionGroupBox.setLayout(buttonLayout)

        self.dateEdit = QDateEdit()
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)

        dateLabel = QLabel("Date")
        dateLabel.setBuddy(self.dateEdit)

        self.categorySelectionLayout = QVBoxLayout()
        self.categorySelectionLayout.addWidget(self.languageCheckBox)
        self.categorySelectionLayout.addWidget(self.toBothBulletinsCheckBox)
        self.categorySelectionLayout.addWidget(categorySelectionGroupBox)
        self.categorySelectionLayout.addWidget(dateLabel)
        self.categorySelectionLayout.addWidget(self.dateEdit)


    def otherLanguageText(self, text): # convert to dictionary

        if (text == "Guild's events"):
            return "Killan tapahtumat"
        elif (text == "Killan tapahtumat"):
            return "Guild's events"
        elif (text == "Other events"):
            return "Muut tapahtumat"
        elif (text == "Muut tapahtumat"):
            return "Other events"
        elif (text == "General"):
            return "Yleistä"
        elif (text == "Yleistä"):
            return "General"
        elif (text == "Studies"):
            return "Opinnot"
        elif (text == "Opinnot"):
            return "Studies"
        else:
            raise Exception("Wrong value for otherLanguageText")

        """
        categoriesDict_en = {
            "Guild's events":"Killan tapahtumat",
            "Other events":"Muut tapahtumat",
            "General":"Yleistä",
            "Studies":"Opinnot"
        }

        categoriesDict_fi = dict(reversed(item) for item in categoriesDict_en.items())
        categoriesDict = dict(categoriesDict_en, categoriesDict_fi)

        try:
            return categoriesDict(text)
        except ValueError:
            raise Exception("Wrong value for otherLanguageText")
        """


    def languageCheckBoxClicked(self, state):
        if state == QtCore.Qt.Checked:
            self.radioButton1.setText("Guild's events")
            self.radioButton2.setText("Other events")
            self.radioButton3.setText("General")
            self.radioButton4.setText("Studies")
        else:
            self.radioButton1.setText("Killan tapahtumat")
            self.radioButton2.setText("Muut tapahtumat")
            self.radioButton3.setText("Yleistä")
            self.radioButton4.setText("Opinnot")



    #def hide(self):
    #    self.headerLineEdit.hide()
    #    self.textBrowser = QTextBrowser()
    #    self.textBrowser.setGeometry(QtCore.QRect(390, 10, 531, 681))
    #    self.textBrowser.setObjectName("textBrowser")
    #    self.textBrowser.show()


    def createTextEditLayout(self):
        self.textEditLayout = QVBoxLayout()

        self.additionalWeeksEdit = QLineEdit()
        self.additionalWeeksEdit.setText("0") # default
        self.headerLineEdit = QLineEdit()
        self.imageUrl = QLineEdit()
        self.contentTextEdit = QTextEdit()

        addWeeksLabel = QLabel("Additional weeks")
        addWeeksLabel.setBuddy(self.additionalWeeksEdit)
        headerLabel = QLabel("Header")
        headerLabel.setBuddy(self.headerLineEdit)
        imageUrlLabel = QLabel("Image URL")
        imageUrlLabel.setBuddy(self.imageUrl)
        contentLabel = QLabel("Content")
        contentLabel.setBuddy(self.contentTextEdit)

        self.textEditLayout.addWidget(addWeeksLabel)
        self.textEditLayout.addWidget(self.additionalWeeksEdit)
        self.textEditLayout.addWidget(headerLabel)
        self.textEditLayout.addWidget(self.headerLineEdit)
        self.textEditLayout.addWidget(imageUrlLabel)
        self.textEditLayout.addWidget(self.imageUrl)
        self.textEditLayout.addWidget(contentLabel)
        self.textEditLayout.addWidget(self.contentTextEdit)



    def createButtonLayout(self):
        self.buttonLayout = QHBoxLayout()

        savePushButton = QPushButton("Save")
        savePushButton.clicked.connect(self.save)

        clearPushButton = QPushButton("Clear")
        clearPushButton.clicked.connect(self.clear)

        self.buttonLayout.addWidget(clearPushButton)
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(savePushButton)


    def save(self):
        category = self.categorySelectionButtonGroup.checkedButton().text()
        date = [self.dateEdit.date().day(), self.dateEdit.date().month(), self.dateEdit.date().year()]
        weeks = int(self.additionalWeeksEdit.text())
        header = self.headerLineEdit.text()
        image = self.imageUrl.text()
        content = self.contentTextEdit.toPlainText()

        save_entry({
            'category': category,
            'date': date,
            'header': header,
            'image': image,
            'content': content
            }, self.languageCheckBox.isChecked(), weeks)

        if self.toBothBulletinsCheckBox.isChecked():
            save_entry({
                'category': self.otherLanguageText(category),   # both languages fix here
                'date': date,
                'header': header,
                'image': image,
                'content': content
                }, not self.languageCheckBox.isChecked(), weeks)

        self.clear()


    def clear(self):
        self.headerLineEdit.clear()
        self.imageUrl.clear()
        self.contentTextEdit.clear()
        self.languageCheckBox.setCheckState(0)
        self.toBothBulletinsCheckBox.setCheckState(0)
        self.dateEdit.setDateTime(QDateTime.currentDateTime())



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    tiedotin = MainWindow()
    tiedotin.show()
    sys.exit(app.exec_())
