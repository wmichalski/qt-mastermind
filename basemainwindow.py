# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/mainwindowmodelW13574.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaseMainWindow(object):
    def setupUi(self, BaseMainWindow):
        BaseMainWindow.setObjectName("BaseMainWindow")
        BaseMainWindow.setWindowModality(QtCore.Qt.NonModal)
        BaseMainWindow.resize(386, 780)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BaseMainWindow.sizePolicy().hasHeightForWidth())
        BaseMainWindow.setSizePolicy(sizePolicy)
        BaseMainWindow.setBaseSize(QtCore.QSize(3, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("diamond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BaseMainWindow.setWindowIcon(icon)
        BaseMainWindow.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.centralwidget = QtWidgets.QWidget(BaseMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.oldGuessesView = QtWidgets.QTableView(self.centralwidget)
        self.oldGuessesView.setEnabled(False)
        self.oldGuessesView.setMinimumSize(QtCore.QSize(200, 500))
        self.oldGuessesView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.oldGuessesView.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.oldGuessesView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.oldGuessesView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oldGuessesView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oldGuessesView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oldGuessesView.setObjectName("oldGuessesView")
        self.oldGuessesView.horizontalHeader().setVisible(False)
        self.oldGuessesView.horizontalHeader().setHighlightSections(False)
        self.oldGuessesView.verticalHeader().setVisible(False)
        self.oldGuessesView.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_4.addWidget(self.oldGuessesView)
        self.scoreView = QtWidgets.QTableView(self.centralwidget)
        self.scoreView.setEnabled(False)
        self.scoreView.setMinimumSize(QtCore.QSize(60, 0))
        self.scoreView.setMaximumSize(QtCore.QSize(60, 16777215))
        self.scoreView.setAutoFillBackground(False)
        self.scoreView.setStyleSheet("background-color: rgb(186, 189, 182)")
        self.scoreView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scoreView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scoreView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scoreView.setAutoScroll(False)
        self.scoreView.setObjectName("scoreView")
        self.scoreView.horizontalHeader().setVisible(False)
        self.scoreView.horizontalHeader().setHighlightSections(False)
        self.scoreView.verticalHeader().setVisible(False)
        self.scoreView.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_4.addWidget(self.scoreView)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.thisGuessTable = QtWidgets.QTableWidget(self.centralwidget)
        self.thisGuessTable.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thisGuessTable.sizePolicy().hasHeightForWidth())
        self.thisGuessTable.setSizePolicy(sizePolicy)
        self.thisGuessTable.setMinimumSize(QtCore.QSize(0, 50))
        self.thisGuessTable.setMaximumSize(QtCore.QSize(200, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 189, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.thisGuessTable.setPalette(palette)
        self.thisGuessTable.setAcceptDrops(True)
        self.thisGuessTable.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.thisGuessTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.thisGuessTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thisGuessTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thisGuessTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.thisGuessTable.setWordWrap(True)
        self.thisGuessTable.setCornerButtonEnabled(False)
        self.thisGuessTable.setRowCount(1)
        self.thisGuessTable.setColumnCount(4)
        self.thisGuessTable.setObjectName("thisGuessTable")
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.thisGuessTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.thisGuessTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.thisGuessTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.thisGuessTable.setItem(0, 3, item)
        self.thisGuessTable.horizontalHeader().setVisible(False)
        self.thisGuessTable.horizontalHeader().setCascadingSectionResizes(False)
        self.thisGuessTable.horizontalHeader().setDefaultSectionSize(50)
        self.thisGuessTable.horizontalHeader().setHighlightSections(False)
        self.thisGuessTable.horizontalHeader().setMinimumSectionSize(0)
        self.thisGuessTable.verticalHeader().setVisible(False)
        self.thisGuessTable.verticalHeader().setDefaultSectionSize(50)
        self.thisGuessTable.verticalHeader().setHighlightSections(False)
        self.thisGuessTable.verticalHeader().setMinimumSectionSize(0)
        self.horizontalLayout_5.addWidget(self.thisGuessTable)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_5.addWidget(self.resetButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.colorsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.colorsTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorsTable.sizePolicy().hasHeightForWidth())
        self.colorsTable.setSizePolicy(sizePolicy)
        self.colorsTable.setMinimumSize(QtCore.QSize(270, 46))
        self.colorsTable.setMaximumSize(QtCore.QSize(270, 46))
        self.colorsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.colorsTable.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.colorsTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.colorsTable.setStyleSheet("border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.colorsTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.colorsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.colorsTable.setAutoScroll(False)
        self.colorsTable.setProperty("showDropIndicator", False)
        self.colorsTable.setDragDropOverwriteMode(False)
        self.colorsTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.colorsTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.colorsTable.setCornerButtonEnabled(False)
        self.colorsTable.setRowCount(1)
        self.colorsTable.setColumnCount(6)
        self.colorsTable.setObjectName("colorsTable")
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(247, 13, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 95, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 227, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(166, 214, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(159, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 5, item)
        self.colorsTable.horizontalHeader().setVisible(False)
        self.colorsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.colorsTable.horizontalHeader().setDefaultSectionSize(45)
        self.colorsTable.horizontalHeader().setMinimumSectionSize(0)
        self.colorsTable.horizontalHeader().setStretchLastSection(False)
        self.colorsTable.verticalHeader().setVisible(False)
        self.colorsTable.verticalHeader().setDefaultSectionSize(45)
        self.colorsTable.verticalHeader().setMinimumSectionSize(0)
        self.horizontalLayout_6.addWidget(self.colorsTable)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 46))
        self.submitButton.setMaximumSize(QtCore.QSize(270, 16777215))
        self.submitButton.setAcceptDrops(False)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout_3.addWidget(self.submitButton)
        spacerItem2 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        BaseMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BaseMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BaseMainWindow)

    def retranslateUi(self, BaseMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BaseMainWindow.setWindowTitle(_translate("BaseMainWindow", "Mastermind"))
        __sortingEnabled = self.thisGuessTable.isSortingEnabled()
        self.thisGuessTable.setSortingEnabled(False)
        self.thisGuessTable.setSortingEnabled(__sortingEnabled)
        self.resetButton.setText(_translate("BaseMainWindow", "Reset"))
        __sortingEnabled = self.colorsTable.isSortingEnabled()
        self.colorsTable.setSortingEnabled(False)
        self.colorsTable.setSortingEnabled(__sortingEnabled)
        self.submitButton.setText(_translate("BaseMainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaseMainWindow = QtWidgets.QMainWindow()
    ui = Ui_BaseMainWindow()
    ui.setupUi(BaseMainWindow)
    BaseMainWindow.show()
    sys.exit(app.exec_())


