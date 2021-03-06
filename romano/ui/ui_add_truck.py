# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_truck.ui'
#
# Created: Sat Dec 14 02:03:48 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddTruck(object):
    def setupUi(self, AddTruck):
        AddTruck.setObjectName("AddTruck")
        AddTruck.resize(695, 482)
        self.verticalLayout = QtGui.QVBoxLayout(AddTruck)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(AddTruck)
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
        self.newWidget = QtGui.QWidget(AddTruck)
        self.newWidget.setObjectName("newWidget")
        self.formLayout = QtGui.QFormLayout(self.newWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.newWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.licensePlateLineEdit = QtGui.QLineEdit(self.newWidget)
        self.licensePlateLineEdit.setObjectName("licensePlateLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.licensePlateLineEdit)
        self.label_3 = QtGui.QLabel(self.newWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.saveAsFrequentBox = QtGui.QCheckBox(self.newWidget)
        self.saveAsFrequentBox.setObjectName("saveAsFrequentBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.saveAsFrequentBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carrierLineEdit = QtGui.QLineEdit(self.newWidget)
        self.carrierLineEdit.setReadOnly(True)
        self.carrierLineEdit.setObjectName("carrierLineEdit")
        self.horizontalLayout_3.addWidget(self.carrierLineEdit)
        self.addCarrierButton = QtGui.QToolButton(self.newWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add-transaction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addCarrierButton.setIcon(icon)
        self.addCarrierButton.setObjectName("addCarrierButton")
        self.horizontalLayout_3.addWidget(self.addCarrierButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.driverLayout.addWidget(self.newWidget)
        self.line = QtGui.QFrame(AddTruck)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.driverLayout.addWidget(self.line)
        self.frequentWidget = QtGui.QWidget(AddTruck)
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
        self.trucksTableView = QtGui.QTableView(self.frequentWidget)
        self.trucksTableView.setAlternatingRowColors(True)
        self.trucksTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.trucksTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.trucksTableView.setObjectName("trucksTableView")
        self.trucksTableView.horizontalHeader().setHighlightSections(False)
        self.trucksTableView.horizontalHeader().setStretchLastSection(True)
        self.trucksTableView.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.trucksTableView)
        self.driverLayout.addWidget(self.frequentWidget)
        self.verticalLayout.addLayout(self.driverLayout)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem)
        self.addButton = QtGui.QPushButton(AddTruck)
        self.addButton.setObjectName("addButton")
        self.buttonsLayout.addWidget(self.addButton)
        self.cancelButton = QtGui.QPushButton(AddTruck)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonsLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonsLayout)

        self.retranslateUi(AddTruck)
        QtCore.QMetaObject.connectSlotsByName(AddTruck)

    def retranslateUi(self, AddTruck):
        AddTruck.setWindowTitle(QtGui.QApplication.translate("AddTruck", "Agregar camión", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("AddTruck", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.frequentButton.setText(QtGui.QApplication.translate("AddTruck", "Frecuente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddTruck", "Placa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddTruck", "Transportista", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsFrequentBox.setText(QtGui.QApplication.translate("AddTruck", "Guardar como frecuente", None, QtGui.QApplication.UnicodeUTF8))
        self.addCarrierButton.setText(QtGui.QApplication.translate("AddTruck", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddTruck", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("AddTruck", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("AddTruck", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

from . import pixmaps_rc
