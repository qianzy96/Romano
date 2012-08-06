# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ticket.ui'
#
# Created: Mon Aug  6 10:47:35 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NewTicket(object):
    def setupUi(self, NewTicket):
        NewTicket.setObjectName("NewTicket")
        NewTicket.resize(530, 321)
        NewTicket.setMinimumSize(QtCore.QSize(480, 300))
        self.verticalLayout = QtGui.QVBoxLayout(NewTicket)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(NewTicket)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.driversComboBox = QtGui.QComboBox(NewTicket)
        self.driversComboBox.setEditable(True)
        self.driversComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.driversComboBox.setObjectName("driversComboBox")
        self.horizontalLayout_3.addWidget(self.driversComboBox)
        self.addDriverButton = QtGui.QToolButton(NewTicket)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add-transaction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDriverButton.setIcon(icon)
        self.addDriverButton.setObjectName("addDriverButton")
        self.horizontalLayout_3.addWidget(self.addDriverButton)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_3 = QtGui.QLabel(NewTicket)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.trucksComboBox = QtGui.QComboBox(NewTicket)
        self.trucksComboBox.setEditable(True)
        self.trucksComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.trucksComboBox.setObjectName("trucksComboBox")
        self.horizontalLayout_4.addWidget(self.trucksComboBox)
        self.addTruckButton = QtGui.QToolButton(NewTicket)
        self.addTruckButton.setIcon(icon)
        self.addTruckButton.setObjectName("addTruckButton")
        self.horizontalLayout_4.addWidget(self.addTruckButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.weightLabel = QtGui.QLabel(NewTicket)
        self.weightLabel.setObjectName("weightLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.weightLabel)
        self.weightLayout = QtGui.QHBoxLayout()
        self.weightLayout.setObjectName("weightLayout")
        self.incomingWeightSpinBox = QtGui.QDoubleSpinBox(NewTicket)
        self.incomingWeightSpinBox.setEnabled(False)
        self.incomingWeightSpinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.incomingWeightSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.incomingWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.incomingWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.incomingWeightSpinBox.setMaximum(999999.0)
        self.incomingWeightSpinBox.setObjectName("incomingWeightSpinBox")
        self.weightLayout.addWidget(self.incomingWeightSpinBox)
        self.captureWeightButton = QtGui.QPushButton(NewTicket)
        self.captureWeightButton.setMinimumSize(QtCore.QSize(120, 0))
        self.captureWeightButton.setCheckable(True)
        self.captureWeightButton.setChecked(False)
        self.captureWeightButton.setObjectName("captureWeightButton")
        self.weightLayout.addWidget(self.captureWeightButton)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.weightLayout)
        self.manualCheckBox = QtGui.QCheckBox(NewTicket)
        self.manualCheckBox.setObjectName("manualCheckBox")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.manualCheckBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.label = QtGui.QLabel(NewTicket)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.commentPlainTextEdit = QtGui.QPlainTextEdit(NewTicket)
        self.commentPlainTextEdit.setTabChangesFocus(True)
        self.commentPlainTextEdit.setObjectName("commentPlainTextEdit")
        self.verticalLayout.addWidget(self.commentPlainTextEdit)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(NewTicket)
        self.cancelButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonsLayout.addWidget(self.cancelButton)
        self.createTicketButton = QtGui.QPushButton(NewTicket)
        self.createTicketButton.setObjectName("createTicketButton")
        self.buttonsLayout.addWidget(self.createTicketButton)
        self.verticalLayout.addLayout(self.buttonsLayout)

        self.retranslateUi(NewTicket)
        QtCore.QMetaObject.connectSlotsByName(NewTicket)

    def retranslateUi(self, NewTicket):
        NewTicket.setWindowTitle(QtGui.QApplication.translate("NewTicket", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewTicket", "Chofer", None, QtGui.QApplication.UnicodeUTF8))
        self.addDriverButton.setToolTip(QtGui.QApplication.translate("NewTicket", "Crear nuevo chofer", None, QtGui.QApplication.UnicodeUTF8))
        self.addDriverButton.setText(QtGui.QApplication.translate("NewTicket", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewTicket", "Camión", None, QtGui.QApplication.UnicodeUTF8))
        self.addTruckButton.setToolTip(QtGui.QApplication.translate("NewTicket", "Crear nuevo camión", None, QtGui.QApplication.UnicodeUTF8))
        self.addTruckButton.setText(QtGui.QApplication.translate("NewTicket", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.weightLabel.setText(QtGui.QApplication.translate("NewTicket", "Peso de entrada", None, QtGui.QApplication.UnicodeUTF8))
        self.incomingWeightSpinBox.setSuffix(QtGui.QApplication.translate("NewTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.captureWeightButton.setText(QtGui.QApplication.translate("NewTicket", "Capturar peso", None, QtGui.QApplication.UnicodeUTF8))
        self.manualCheckBox.setText(QtGui.QApplication.translate("NewTicket", "Captura manual", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewTicket", "Comentario", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("NewTicket", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.createTicketButton.setText(QtGui.QApplication.translate("NewTicket", "Crear ticket", None, QtGui.QApplication.UnicodeUTF8))

import pixmaps_rc
