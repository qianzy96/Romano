# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'close_ticket.ui'
#
# Created: Thu Aug  2 15:38:37 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CloseTicket(object):
    def setupUi(self, CloseTicket):
        CloseTicket.setObjectName("CloseTicket")
        CloseTicket.resize(1200, 500)
        CloseTicket.setMinimumSize(QtCore.QSize(1024, 500))
        self.verticalLayout = QtGui.QVBoxLayout(CloseTicket)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dialogLayout = QtGui.QHBoxLayout()
        self.dialogLayout.setObjectName("dialogLayout")
        self.ticketLayout = QtGui.QVBoxLayout()
        self.ticketLayout.setObjectName("ticketLayout")
        self.ticketFormLayout = QtGui.QFormLayout()
        self.ticketFormLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.ticketFormLayout.setObjectName("ticketFormLayout")
        self.numberLabel = QtGui.QLabel(CloseTicket)
        self.numberLabel.setObjectName("numberLabel")
        self.ticketFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.numberLabel)
        self.numberTypeLayout = QtGui.QHBoxLayout()
        self.numberTypeLayout.setObjectName("numberTypeLayout")
        self.numberLineEdit = QtGui.QLineEdit(CloseTicket)
        self.numberLineEdit.setEnabled(False)
        self.numberLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.numberTypeLayout.addWidget(self.numberLineEdit)
        self.ticketTypeLabel = QtGui.QLabel(CloseTicket)
        self.ticketTypeLabel.setObjectName("ticketTypeLabel")
        self.numberTypeLayout.addWidget(self.ticketTypeLabel)
        self.ticketTypeLineEdit = QtGui.QLineEdit(CloseTicket)
        self.ticketTypeLineEdit.setEnabled(False)
        self.ticketTypeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ticketTypeLineEdit.setObjectName("ticketTypeLineEdit")
        self.numberTypeLayout.addWidget(self.ticketTypeLineEdit)
        self.ticketFormLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.numberTypeLayout)
        self.driverLabel = QtGui.QLabel(CloseTicket)
        self.driverLabel.setObjectName("driverLabel")
        self.ticketFormLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.driverLabel)
        self.driverLineEdit = QtGui.QLineEdit(CloseTicket)
        self.driverLineEdit.setEnabled(False)
        self.driverLineEdit.setObjectName("driverLineEdit")
        self.ticketFormLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.driverLineEdit)
        self.truckLabel = QtGui.QLabel(CloseTicket)
        self.truckLabel.setObjectName("truckLabel")
        self.ticketFormLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.truckLabel)
        self.truckLineEdit = QtGui.QLineEdit(CloseTicket)
        self.truckLineEdit.setEnabled(False)
        self.truckLineEdit.setObjectName("truckLineEdit")
        self.ticketFormLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.truckLineEdit)
        self.weightLabelsLayout = QtGui.QVBoxLayout()
        self.weightLabelsLayout.setObjectName("weightLabelsLayout")
        self.label_6 = QtGui.QLabel(CloseTicket)
        self.label_6.setObjectName("label_6")
        self.weightLabelsLayout.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(CloseTicket)
        self.label_4.setObjectName("label_4")
        self.weightLabelsLayout.addWidget(self.label_4)
        self.ticketFormLayout.setLayout(3, QtGui.QFormLayout.LabelRole, self.weightLabelsLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.captureWeightButton = QtGui.QPushButton(CloseTicket)
        self.captureWeightButton.setMinimumSize(QtCore.QSize(120, 0))
        self.captureWeightButton.setCheckable(True)
        self.captureWeightButton.setChecked(False)
        self.captureWeightButton.setAutoDefault(False)
        self.captureWeightButton.setDefault(False)
        self.captureWeightButton.setFlat(False)
        self.captureWeightButton.setObjectName("captureWeightButton")
        self.gridLayout.addWidget(self.captureWeightButton, 1, 2, 1, 1)
        self.incomingWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.incomingWeightSpinBox.setEnabled(False)
        self.incomingWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.incomingWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.incomingWeightSpinBox.setMaximum(500000.0)
        self.incomingWeightSpinBox.setProperty("value", 54430.4)
        self.incomingWeightSpinBox.setObjectName("incomingWeightSpinBox")
        self.gridLayout.addWidget(self.incomingWeightSpinBox, 0, 0, 1, 1)
        self.outgoingWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.outgoingWeightSpinBox.setFrame(True)
        self.outgoingWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outgoingWeightSpinBox.setReadOnly(True)
        self.outgoingWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.outgoingWeightSpinBox.setMaximum(500000.0)
        self.outgoingWeightSpinBox.setObjectName("outgoingWeightSpinBox")
        self.gridLayout.addWidget(self.outgoingWeightSpinBox, 1, 0, 1, 1)
        self.ticketFormLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.gridLayout)
        self.clientSelectLayout = QtGui.QHBoxLayout()
        self.clientSelectLayout.setObjectName("clientSelectLayout")
        self.factoryButton = QtGui.QRadioButton(CloseTicket)
        self.factoryButton.setEnabled(False)
        self.factoryButton.setObjectName("factoryButton")
        self.clientSelectLayout.addWidget(self.factoryButton)
        self.clientButton = QtGui.QRadioButton(CloseTicket)
        self.clientButton.setEnabled(False)
        self.clientButton.setObjectName("clientButton")
        self.clientSelectLayout.addWidget(self.clientButton)
        self.ticketFormLayout.setLayout(4, QtGui.QFormLayout.LabelRole, self.clientSelectLayout)
        self.weightsLayout = QtGui.QVBoxLayout()
        self.weightsLayout.setObjectName("weightsLayout")
        self.clientsComboBox = QtGui.QComboBox(CloseTicket)
        self.clientsComboBox.setEditable(True)
        self.clientsComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.clientsComboBox.setObjectName("clientsComboBox")
        self.weightsLayout.addWidget(self.clientsComboBox)
        self.ticketFormLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.weightsLayout)
        self.ticketLayout.addLayout(self.ticketFormLayout)
        self.commentLabel = QtGui.QLabel(CloseTicket)
        self.commentLabel.setObjectName("commentLabel")
        self.ticketLayout.addWidget(self.commentLabel)
        self.commentTextEdit = QtGui.QTextEdit(CloseTicket)
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.ticketLayout.addWidget(self.commentTextEdit)
        self.dialogLayout.addLayout(self.ticketLayout)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.dialogLayout.addItem(spacerItem)
        self.transactionsLayout = QtGui.QVBoxLayout()
        self.transactionsLayout.setObjectName("transactionsLayout")
        self.transactionsTitleLayout = QtGui.QHBoxLayout()
        self.transactionsTitleLayout.setObjectName("transactionsTitleLayout")
        self.transactionsLabel = QtGui.QLabel(CloseTicket)
        self.transactionsLabel.setObjectName("transactionsLabel")
        self.transactionsTitleLayout.addWidget(self.transactionsLabel)
        self.addTransactionButton = QtGui.QPushButton(CloseTicket)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add-transaction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTransactionButton.setIcon(icon)
        self.addTransactionButton.setObjectName("addTransactionButton")
        self.transactionsTitleLayout.addWidget(self.addTransactionButton)
        self.removeTransactionButton = QtGui.QPushButton(CloseTicket)
        self.removeTransactionButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/remove-transaction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeTransactionButton.setIcon(icon1)
        self.removeTransactionButton.setObjectName("removeTransactionButton")
        self.transactionsTitleLayout.addWidget(self.removeTransactionButton)
        self.transactionsLayout.addLayout(self.transactionsTitleLayout)
        self.transactionsTableView = QtGui.QTableView(CloseTicket)
        self.transactionsTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.transactionsTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.transactionsTableView.setObjectName("transactionsTableView")
        self.transactionsTableView.horizontalHeader().setHighlightSections(False)
        self.transactionsTableView.horizontalHeader().setStretchLastSection(False)
        self.transactionsTableView.verticalHeader().setVisible(False)
        self.transactionsLayout.addWidget(self.transactionsTableView)
        self.transactionsTotalLayout = QtGui.QHBoxLayout()
        self.transactionsTotalLayout.setObjectName("transactionsTotalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.transactionsTotalLayout.addItem(spacerItem1)
        self.transactionsTotalLabel = QtGui.QLabel(CloseTicket)
        self.transactionsTotalLabel.setObjectName("transactionsTotalLabel")
        self.transactionsTotalLayout.addWidget(self.transactionsTotalLabel)
        self.transactionsTotalSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.transactionsTotalSpinBox.setEnabled(False)
        self.transactionsTotalSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.transactionsTotalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.transactionsTotalSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.transactionsTotalSpinBox.setMaximum(999999.0)
        self.transactionsTotalSpinBox.setObjectName("transactionsTotalSpinBox")
        self.transactionsTotalLayout.addWidget(self.transactionsTotalSpinBox)
        self.transactionsLayout.addLayout(self.transactionsTotalLayout)
        self.dialogLayout.addLayout(self.transactionsLayout)
        self.verticalLayout.addLayout(self.dialogLayout)
        self.line_2 = QtGui.QFrame(CloseTicket)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.weightLayout = QtGui.QHBoxLayout()
        self.weightLayout.setObjectName("weightLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.weightLayout.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(CloseTicket)
        self.label_10.setMinimumSize(QtCore.QSize(100, 0))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.weightLayout.addWidget(self.label_10)
        self.grossWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.grossWeightSpinBox.setEnabled(False)
        self.grossWeightSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.grossWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.grossWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.grossWeightSpinBox.setMaximum(999999.0)
        self.grossWeightSpinBox.setObjectName("grossWeightSpinBox")
        self.weightLayout.addWidget(self.grossWeightSpinBox)
        self.label_8 = QtGui.QLabel(CloseTicket)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.weightLayout.addWidget(self.label_8)
        self.tareWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.tareWeightSpinBox.setEnabled(False)
        self.tareWeightSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.tareWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tareWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.tareWeightSpinBox.setMaximum(999999.0)
        self.tareWeightSpinBox.setObjectName("tareWeightSpinBox")
        self.weightLayout.addWidget(self.tareWeightSpinBox)
        self.label_11 = QtGui.QLabel(CloseTicket)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.weightLayout.addWidget(self.label_11)
        self.netWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.netWeightSpinBox.setEnabled(False)
        self.netWeightSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.netWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.netWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.netWeightSpinBox.setMaximum(999999.0)
        self.netWeightSpinBox.setObjectName("netWeightSpinBox")
        self.weightLayout.addWidget(self.netWeightSpinBox)
        self.verticalLayout.addLayout(self.weightLayout)
        self.providerWidget = QtGui.QWidget(CloseTicket)
        self.providerWidget.setObjectName("providerWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.providerWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.providerWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.providerDocumentNumberLineEdit = QtGui.QLineEdit(self.providerWidget)
        self.providerDocumentNumberLineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.providerDocumentNumberLineEdit.setObjectName("providerDocumentNumberLineEdit")
        self.horizontalLayout.addWidget(self.providerDocumentNumberLineEdit)
        self.label_9 = QtGui.QLabel(self.providerWidget)
        self.label_9.setMinimumSize(QtCore.QSize(100, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.providerWeightSpinBox = QtGui.QDoubleSpinBox(self.providerWidget)
        self.providerWeightSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.providerWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.providerWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.providerWeightSpinBox.setMaximum(999999.0)
        self.providerWeightSpinBox.setObjectName("providerWeightSpinBox")
        self.horizontalLayout.addWidget(self.providerWeightSpinBox)
        self.verticalLayout.addWidget(self.providerWidget)
        self.line = QtGui.QFrame(CloseTicket)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.dialogButtonsLayout = QtGui.QHBoxLayout()
        self.dialogButtonsLayout.setObjectName("dialogButtonsLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.dialogButtonsLayout.addItem(spacerItem4)
        self.cancelButton = QtGui.QPushButton(CloseTicket)
        self.cancelButton.setObjectName("cancelButton")
        self.dialogButtonsLayout.addWidget(self.cancelButton)
        self.closeTicketButton = QtGui.QPushButton(CloseTicket)
        self.closeTicketButton.setObjectName("closeTicketButton")
        self.dialogButtonsLayout.addWidget(self.closeTicketButton)
        self.verticalLayout.addLayout(self.dialogButtonsLayout)

        self.retranslateUi(CloseTicket)
        QtCore.QMetaObject.connectSlotsByName(CloseTicket)

    def retranslateUi(self, CloseTicket):
        CloseTicket.setWindowTitle(QtGui.QApplication.translate("CloseTicket", "Cerrar ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.numberLabel.setText(QtGui.QApplication.translate("CloseTicket", "Número", None, QtGui.QApplication.UnicodeUTF8))
        self.ticketTypeLabel.setText(QtGui.QApplication.translate("CloseTicket", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.driverLabel.setText(QtGui.QApplication.translate("CloseTicket", "Chofer", None, QtGui.QApplication.UnicodeUTF8))
        self.truckLabel.setText(QtGui.QApplication.translate("CloseTicket", "Camión", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CloseTicket", "Peso de entrada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CloseTicket", "Peso de salida", None, QtGui.QApplication.UnicodeUTF8))
        self.captureWeightButton.setText(QtGui.QApplication.translate("CloseTicket", "Capturar peso", None, QtGui.QApplication.UnicodeUTF8))
        self.incomingWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.outgoingWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.factoryButton.setText(QtGui.QApplication.translate("CloseTicket", "Fábrica", None, QtGui.QApplication.UnicodeUTF8))
        self.clientButton.setText(QtGui.QApplication.translate("CloseTicket", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.commentLabel.setText(QtGui.QApplication.translate("CloseTicket", "Comentario", None, QtGui.QApplication.UnicodeUTF8))
        self.transactionsLabel.setText(QtGui.QApplication.translate("CloseTicket", "Transacciones", None, QtGui.QApplication.UnicodeUTF8))
        self.addTransactionButton.setText(QtGui.QApplication.translate("CloseTicket", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.removeTransactionButton.setText(QtGui.QApplication.translate("CloseTicket", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.transactionsTotalLabel.setText(QtGui.QApplication.translate("CloseTicket", "Total transacciones", None, QtGui.QApplication.UnicodeUTF8))
        self.transactionsTotalSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("CloseTicket", "Peso bruto", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CloseTicket", "Peso tara", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CloseTicket", "Peso neto", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CloseTicket", "Número de guia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("CloseTicket", "Peso SADA", None, QtGui.QApplication.UnicodeUTF8))
        self.providerWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("CloseTicket", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.closeTicketButton.setText(QtGui.QApplication.translate("CloseTicket", "Cerrar ticket", None, QtGui.QApplication.UnicodeUTF8))

import pixmaps_rc
