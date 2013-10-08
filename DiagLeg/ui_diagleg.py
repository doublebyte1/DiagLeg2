# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_diagleg.ui'
#
# Created: Tue Oct  8 11:39:09 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DiagLeg(object):
    def setupUi(self, DiagLeg):
        DiagLeg.setObjectName(_fromUtf8("DiagLeg"))
        DiagLeg.resize(525, 634)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.view = QtGui.QGraphicsView(self.dockWidgetContents)
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout.addWidget(self.view)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushGenerate = QtGui.QPushButton(self.dockWidgetContents)
        self.pushGenerate.setObjectName(_fromUtf8("pushGenerate"))
        self.horizontalLayout.addWidget(self.pushGenerate)
        self.pushExport = QtGui.QPushButton(self.dockWidgetContents)
        self.pushExport.setObjectName(_fromUtf8("pushExport"))
        self.horizontalLayout.addWidget(self.pushExport)
        self.pushClose = QtGui.QPushButton(self.dockWidgetContents)
        self.pushClose.setObjectName(_fromUtf8("pushClose"))
        self.horizontalLayout.addWidget(self.pushClose)
        self.pushAbout = QtGui.QPushButton(self.dockWidgetContents)
        self.pushAbout.setObjectName(_fromUtf8("pushAbout"))
        self.horizontalLayout.addWidget(self.pushAbout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DiagLeg.setWidget(self.dockWidgetContents)

        self.retranslateUi(DiagLeg)
        QtCore.QObject.connect(self.pushGenerate, QtCore.SIGNAL(_fromUtf8("clicked()")), DiagLeg.onOk)
        QtCore.QObject.connect(self.pushClose, QtCore.SIGNAL(_fromUtf8("clicked()")), DiagLeg.close)
        QtCore.QObject.connect(self.pushExport, QtCore.SIGNAL(_fromUtf8("clicked()")), DiagLeg.onExport)
        QtCore.QObject.connect(self.pushAbout, QtCore.SIGNAL(_fromUtf8("clicked()")), DiagLeg.onAbout)
        QtCore.QMetaObject.connectSlotsByName(DiagLeg)

    def retranslateUi(self, DiagLeg):
        DiagLeg.setWindowTitle(QtGui.QApplication.translate("DiagLeg", "DiagLeg", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGenerate.setToolTip(QtGui.QApplication.translate("DiagLeg", "Click to generate legend", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGenerate.setWhatsThis(QtGui.QApplication.translate("DiagLeg", "It generates the legend", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGenerate.setText(QtGui.QApplication.translate("DiagLeg", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushExport.setToolTip(QtGui.QApplication.translate("DiagLeg", "Export the legend to an image or a webpage", None, QtGui.QApplication.UnicodeUTF8))
        self.pushExport.setWhatsThis(QtGui.QApplication.translate("DiagLeg", "Click to export the legend to an image or a webpage", None, QtGui.QApplication.UnicodeUTF8))
        self.pushExport.setText(QtGui.QApplication.translate("DiagLeg", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setToolTip(QtGui.QApplication.translate("DiagLeg", "Closes this dialogue", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setWhatsThis(QtGui.QApplication.translate("DiagLeg", "This closes the dialogue", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setText(QtGui.QApplication.translate("DiagLeg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAbout.setToolTip(QtGui.QApplication.translate("DiagLeg", "About DiagLeg", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAbout.setWhatsThis(QtGui.QApplication.translate("DiagLeg", "Click to show information about the credits of plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAbout.setText(QtGui.QApplication.translate("DiagLeg", "About", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
