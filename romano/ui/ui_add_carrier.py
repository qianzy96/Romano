# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_carrier.ui'
#
# Created: Fri Aug 17 22:08:52 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddCarrier(object):
    def setupUi(self, AddCarrier):
        AddCarrier.setObjectName("AddCarrier")
        AddCarrier.resize(695, 482)
        self.verticalLayout = QtGui.QVBoxLayout(AddCarrier)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(AddCarrier)
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
        self.newWidget = QtGui.QWidget(AddCarrier)
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
        self.saveAsFrequentBox = QtGui.QCheckBox(self.newWidget)
        self.saveAsFrequentBox.setObjectName("saveAsFrequentBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.saveAsFrequentBox)
        self.driverLayout.addWidget(self.newWidget)
        self.line = QtGui.QFrame(AddCarrier)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.driverLayout.addWidget(self.line)
        self.frequentWidget = QtGui.QWidget(AddCarrier)
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
        self.carriersTableView = QtGui.QTableView(self.frequentWidget)
        self.carriersTableView.setAlternatingRowColors(True)
        self.carriersTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.carriersTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.carriersTableView.setObjectName("carriersTableView")
        self.carriersTableView.horizontalHeader().setHighlightSections(False)
        self.carriersTableView.horizontalHeader().setStretchLastSection(True)
        self.carriersTableView.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.carriersTableView)
        self.driverLayout.addWidget(self.frequentWidget)
        self.verticalLayout.addLayout(self.driverLayout)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem)
        self.addButton = QtGui.QPushButton(AddCarrier)
        self.addButton.setObjectName("addButton")
        self.buttonsLayout.addWidget(self.addButton)
        self.cancelButton = QtGui.QPushButton(AddCarrier)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonsLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonsLayout)

        self.retranslateUi(AddCarrier)
        QtCore.QMetaObject.connectSlotsByName(AddCarrier)

    def retranslateUi(self, AddCarrier):
        AddCarrier.setWindowTitle(QtGui.QApplication.translate("AddCarrier", "Agregar transportista", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("AddCarrier", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.frequentButton.setText(QtGui.QApplication.translate("AddCarrier", "Frecuente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddCarrier", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsFrequentBox.setText(QtGui.QApplication.translate("AddCarrier", "Guardar como frequente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddCarrier", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("AddCarrier", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("AddCarrier", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

