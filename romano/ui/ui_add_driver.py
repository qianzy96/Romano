# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_driver.ui'
#
# Created: Thu Aug 16 23:35:03 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddDriver(object):
    def setupUi(self, AddDriver):
        AddDriver.setObjectName("AddDriver")
        AddDriver.resize(695, 482)
        self.verticalLayout = QtGui.QVBoxLayout(AddDriver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(AddDriver)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newButton = QtGui.QRadioButton(self.widget)
        self.newButton.setChecked(True)
        self.newButton.setObjectName("newButton")
        self.horizontalLayout.addWidget(self.newButton)
        self.frequentButton = QtGui.QRadioButton(self.widget)
        self.frequentButton.setChecked(False)
        self.frequentButton.setObjectName("frequentButton")
        self.horizontalLayout.addWidget(self.frequentButton)
        self.verticalLayout.addWidget(self.widget)
        self.driverLayout = QtGui.QHBoxLayout()
        self.driverLayout.setObjectName("driverLayout")
        self.newWidget = QtGui.QWidget(AddDriver)
        self.newWidget.setObjectName("newWidget")
        self.formLayout = QtGui.QFormLayout(self.newWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.newWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.nameLineEdit = QtGui.QLineEdit(self.newWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_3 = QtGui.QLabel(self.newWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.ciLineEdit = QtGui.QLineEdit(self.newWidget)
        self.ciLineEdit.setObjectName("ciLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.ciLineEdit)
        self.saveAsFrequentBox = QtGui.QCheckBox(self.newWidget)
        self.saveAsFrequentBox.setObjectName("saveAsFrequentBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.saveAsFrequentBox)
        self.driverLayout.addWidget(self.newWidget)
        self.line = QtGui.QFrame(AddDriver)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.driverLayout.addWidget(self.line)
        self.frequentWidget = QtGui.QWidget(AddDriver)
        self.frequentWidget.setObjectName("frequentWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frequentWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.frequentWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.filterLineEdit = QtGui.QLineEdit(self.frequentWidget)
        self.filterLineEdit.setObjectName("filterLineEdit")
        self.horizontalLayout_2.addWidget(self.filterLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.driversTableView = QtGui.QTableView(self.frequentWidget)
        self.driversTableView.setAlternatingRowColors(True)
        self.driversTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.driversTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.driversTableView.setObjectName("driversTableView")
        self.driversTableView.horizontalHeader().setHighlightSections(False)
        self.driversTableView.horizontalHeader().setStretchLastSection(True)
        self.driversTableView.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.driversTableView)
        self.driverLayout.addWidget(self.frequentWidget)
        self.verticalLayout.addLayout(self.driverLayout)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem)
        self.addButton = QtGui.QPushButton(AddDriver)
        self.addButton.setObjectName("addButton")
        self.buttonsLayout.addWidget(self.addButton)
        self.cancelButton = QtGui.QPushButton(AddDriver)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonsLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonsLayout)

        self.retranslateUi(AddDriver)
        QtCore.QMetaObject.connectSlotsByName(AddDriver)

    def retranslateUi(self, AddDriver):
        AddDriver.setWindowTitle(QtGui.QApplication.translate("AddDriver", "Agregar chofer", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("AddDriver", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.frequentButton.setText(QtGui.QApplication.translate("AddDriver", "Frecuente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddDriver", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddDriver", "Cédula", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsFrequentBox.setText(QtGui.QApplication.translate("AddDriver", "Guardar como frequente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddDriver", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("AddDriver", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("AddDriver", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

