# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'close_ticket.ui'
#
# Created: Thu Aug  6 16:46:51 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CloseTicket(object):
    def setupUi(self, CloseTicket):
        CloseTicket.setObjectName("CloseTicket")
        CloseTicket.resize(1000, 633)
        CloseTicket.setMinimumSize(QtCore.QSize(1000, 530))
        self.verticalLayout = QtGui.QVBoxLayout(CloseTicket)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dialogLayout = QtGui.QHBoxLayout()
        self.dialogLayout.setObjectName("dialogLayout")
        self.ticketWidget = QtGui.QWidget(CloseTicket)
        self.ticketWidget.setMaximumSize(QtCore.QSize(450, 16777215))
        self.ticketWidget.setObjectName("ticketWidget")
        self.ticketLayout = QtGui.QVBoxLayout(self.ticketWidget)
        self.ticketLayout.setContentsMargins(0, 0, 0, 0)
        self.ticketLayout.setObjectName("ticketLayout")
        self.ticketFormLayout = QtGui.QFormLayout()
        self.ticketFormLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.ticketFormLayout.setContentsMargins(0, 0, 0, 0)
        self.ticketFormLayout.setObjectName("ticketFormLayout")
        self.ticketTypeLabel = QtGui.QLabel(self.ticketWidget)
        self.ticketTypeLabel.setObjectName("ticketTypeLabel")
        self.ticketFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ticketTypeLabel)
        self.widget = QtGui.QWidget(self.ticketWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.receptionButton = QtGui.QRadioButton(self.widget)
        self.receptionButton.setObjectName("receptionButton")
        self.horizontalLayout_2.addWidget(self.receptionButton)
        self.dispatchButton = QtGui.QRadioButton(self.widget)
        self.dispatchButton.setObjectName("dispatchButton")
        self.horizontalLayout_2.addWidget(self.dispatchButton)
        self.ticketFormLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget)
        self.numberLabel = QtGui.QLabel(self.ticketWidget)
        self.numberLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.numberLabel.setObjectName("numberLabel")
        self.ticketFormLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.numberLabel)
        self.numberTypeLayout = QtGui.QHBoxLayout()
        self.numberTypeLayout.setObjectName("numberTypeLayout")
        self.numberLineEdit = QtGui.QLineEdit(self.ticketWidget)
        self.numberLineEdit.setEnabled(False)
        self.numberLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.numberTypeLayout.addWidget(self.numberLineEdit)
        self.ticketFormLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.numberTypeLayout)
        self.driverLabel = QtGui.QLabel(self.ticketWidget)
        self.driverLabel.setObjectName("driverLabel")
        self.ticketFormLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.driverLabel)
        self.driverLineEdit = QtGui.QLineEdit(self.ticketWidget)
        self.driverLineEdit.setEnabled(False)
        self.driverLineEdit.setObjectName("driverLineEdit")
        self.ticketFormLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.driverLineEdit)
        self.truckLabel = QtGui.QLabel(self.ticketWidget)
        self.truckLabel.setObjectName("truckLabel")
        self.ticketFormLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.truckLabel)
        self.truckLineEdit = QtGui.QLineEdit(self.ticketWidget)
        self.truckLineEdit.setEnabled(False)
        self.truckLineEdit.setObjectName("truckLineEdit")
        self.ticketFormLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.truckLineEdit)
        self.weightLabelsLayout = QtGui.QVBoxLayout()
        self.weightLabelsLayout.setObjectName("weightLabelsLayout")
        self.label_6 = QtGui.QLabel(self.ticketWidget)
        self.label_6.setObjectName("label_6")
        self.weightLabelsLayout.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.ticketWidget)
        self.label_4.setObjectName("label_4")
        self.weightLabelsLayout.addWidget(self.label_4)
        self.ticketFormLayout.setLayout(4, QtGui.QFormLayout.LabelRole, self.weightLabelsLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.captureWeightButton = QtGui.QPushButton(self.ticketWidget)
        self.captureWeightButton.setMinimumSize(QtCore.QSize(0, 0))
        self.captureWeightButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.captureWeightButton.setStyleSheet("QPushButton:checked {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border: 0px;\n"
"}")
        self.captureWeightButton.setCheckable(True)
        self.captureWeightButton.setChecked(False)
        self.captureWeightButton.setAutoDefault(False)
        self.captureWeightButton.setDefault(False)
        self.captureWeightButton.setFlat(False)
        self.captureWeightButton.setObjectName("captureWeightButton")
        self.gridLayout.addWidget(self.captureWeightButton, 1, 2, 1, 1)
        self.incomingWeightSpinBox = QtGui.QDoubleSpinBox(self.ticketWidget)
        self.incomingWeightSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.incomingWeightSpinBox.setFont(font)
        self.incomingWeightSpinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.incomingWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.incomingWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.incomingWeightSpinBox.setMaximum(500000.0)
        self.incomingWeightSpinBox.setProperty("value", 54430.4)
        self.incomingWeightSpinBox.setObjectName("incomingWeightSpinBox")
        self.gridLayout.addWidget(self.incomingWeightSpinBox, 0, 0, 1, 1)
        self.outgoingWeightSpinBox = QtGui.QDoubleSpinBox(self.ticketWidget)
        self.outgoingWeightSpinBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outgoingWeightSpinBox.sizePolicy().hasHeightForWidth())
        self.outgoingWeightSpinBox.setSizePolicy(sizePolicy)
        self.outgoingWeightSpinBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.outgoingWeightSpinBox.setFont(font)
        self.outgoingWeightSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.outgoingWeightSpinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.outgoingWeightSpinBox.setFrame(True)
        self.outgoingWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outgoingWeightSpinBox.setReadOnly(False)
        self.outgoingWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.outgoingWeightSpinBox.setMaximum(500000.0)
        self.outgoingWeightSpinBox.setProperty("value", 99999.99)
        self.outgoingWeightSpinBox.setObjectName("outgoingWeightSpinBox")
        self.gridLayout.addWidget(self.outgoingWeightSpinBox, 1, 0, 1, 1)
        self.ticketFormLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.gridLayout)
        self.manualCheckBox = QtGui.QCheckBox(self.ticketWidget)
        self.manualCheckBox.setObjectName("manualCheckBox")
        self.ticketFormLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.manualCheckBox)
        self.clientSelectWidget = QtGui.QWidget(self.ticketWidget)
        self.clientSelectWidget.setObjectName("clientSelectWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.clientSelectWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.clientSelectWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ticketFormLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.clientSelectWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.clientLineEdit = QtGui.QLineEdit(self.ticketWidget)
        self.clientLineEdit.setReadOnly(True)
        self.clientLineEdit.setObjectName("clientLineEdit")
        self.horizontalLayout_3.addWidget(self.clientLineEdit)
        self.addClientButton = QtGui.QToolButton(self.ticketWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add-transaction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addClientButton.setIcon(icon)
        self.addClientButton.setObjectName("addClientButton")
        self.horizontalLayout_3.addWidget(self.addClientButton)
        self.ticketFormLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.ticketLayout.addLayout(self.ticketFormLayout)
        self.addressWidget = QtGui.QWidget(self.ticketWidget)
        self.addressWidget.setObjectName("addressWidget")
        self.formLayout = QtGui.QFormLayout(self.addressWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtGui.QLabel(self.addressWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.addressComboBox = QtGui.QComboBox(self.addressWidget)
        self.addressComboBox.setObjectName("addressComboBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.addressComboBox)
        self.ticketLayout.addWidget(self.addressWidget)
        self.commentLabel = QtGui.QLabel(self.ticketWidget)
        self.commentLabel.setObjectName("commentLabel")
        self.ticketLayout.addWidget(self.commentLabel)
        self.commentPlainTextEdit = QtGui.QPlainTextEdit(self.ticketWidget)
        self.commentPlainTextEdit.setTabChangesFocus(True)
        self.commentPlainTextEdit.setObjectName("commentPlainTextEdit")
        self.ticketLayout.addWidget(self.commentPlainTextEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.ticketLayout.addItem(spacerItem)
        self.dialogLayout.addWidget(self.ticketWidget)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.dialogLayout.addItem(spacerItem1)
        self.transactionsLayout = QtGui.QVBoxLayout()
        self.transactionsLayout.setObjectName("transactionsLayout")
        self.transactionsTitleLayout = QtGui.QHBoxLayout()
        self.transactionsTitleLayout.setObjectName("transactionsTitleLayout")
        self.transactionsLabel = QtGui.QLabel(CloseTicket)
        self.transactionsLabel.setObjectName("transactionsLabel")
        self.transactionsTitleLayout.addWidget(self.transactionsLabel)
        self.addTransactionButton = QtGui.QPushButton(CloseTicket)
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
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.transactionsTotalLayout.addItem(spacerItem2)
        self.transactionsTotalLabel = QtGui.QLabel(CloseTicket)
        self.transactionsTotalLabel.setObjectName("transactionsTotalLabel")
        self.transactionsTotalLayout.addWidget(self.transactionsTotalLabel)
        self.transactionsTotalSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.transactionsTotalSpinBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transactionsTotalSpinBox.sizePolicy().hasHeightForWidth())
        self.transactionsTotalSpinBox.setSizePolicy(sizePolicy)
        self.transactionsTotalSpinBox.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.transactionsTotalSpinBox.setFont(font)
        self.transactionsTotalSpinBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.transactionsTotalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.transactionsTotalSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.transactionsTotalSpinBox.setMaximum(999999.0)
        self.transactionsTotalSpinBox.setObjectName("transactionsTotalSpinBox")
        self.transactionsTotalLayout.addWidget(self.transactionsTotalSpinBox)
        self.transactionsLayout.addLayout(self.transactionsTotalLayout)
        self.dialogLayout.addLayout(self.transactionsLayout)
        self.verticalLayout.addLayout(self.dialogLayout)
        self.line_3 = QtGui.QFrame(CloseTicket)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.providerWidget = QtGui.QWidget(CloseTicket)
        self.providerWidget.setObjectName("providerWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.providerWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.documentTypeWidget = QtGui.QWidget(self.providerWidget)
        self.documentTypeWidget.setObjectName("documentTypeWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.documentTypeWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtGui.QLabel(self.documentTypeWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.documentTypeComboBox = QtGui.QComboBox(self.documentTypeWidget)
        self.documentTypeComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.documentTypeComboBox.setObjectName("documentTypeComboBox")
        self.horizontalLayout_4.addWidget(self.documentTypeComboBox)
        self.horizontalLayout.addWidget(self.documentTypeWidget)
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.providerWeightSpinBox.sizePolicy().hasHeightForWidth())
        self.providerWeightSpinBox.setSizePolicy(sizePolicy)
        self.providerWeightSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.providerWeightSpinBox.setFont(font)
        self.providerWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.providerWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.providerWeightSpinBox.setMaximum(999999.0)
        self.providerWeightSpinBox.setObjectName("providerWeightSpinBox")
        self.horizontalLayout.addWidget(self.providerWeightSpinBox)
        self.verticalLayout.addWidget(self.providerWidget)
        self.line_2 = QtGui.QFrame(CloseTicket)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.weightLayout = QtGui.QHBoxLayout()
        self.weightLayout.setObjectName("weightLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.weightLayout.addItem(spacerItem4)
        self.label_10 = QtGui.QLabel(CloseTicket)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(100, 0))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.weightLayout.addWidget(self.label_10)
        self.grossWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.grossWeightSpinBox.setEnabled(False)
        self.grossWeightSpinBox.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.grossWeightSpinBox.setFont(font)
        self.grossWeightSpinBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.grossWeightSpinBox.setAutoFillBackground(True)
        self.grossWeightSpinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.grossWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.grossWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.grossWeightSpinBox.setMaximum(999999.0)
        self.grossWeightSpinBox.setProperty("value", 999999.0)
        self.grossWeightSpinBox.setObjectName("grossWeightSpinBox")
        self.weightLayout.addWidget(self.grossWeightSpinBox)
        self.label_8 = QtGui.QLabel(CloseTicket)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.weightLayout.addWidget(self.label_8)
        self.tareWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.tareWeightSpinBox.setEnabled(False)
        self.tareWeightSpinBox.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.tareWeightSpinBox.setFont(font)
        self.tareWeightSpinBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tareWeightSpinBox.setAutoFillBackground(True)
        self.tareWeightSpinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.tareWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tareWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.tareWeightSpinBox.setMaximum(999999.0)
        self.tareWeightSpinBox.setProperty("value", 999999.0)
        self.tareWeightSpinBox.setObjectName("tareWeightSpinBox")
        self.weightLayout.addWidget(self.tareWeightSpinBox)
        self.label_11 = QtGui.QLabel(CloseTicket)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.weightLayout.addWidget(self.label_11)
        self.netWeightSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.netWeightSpinBox.setEnabled(False)
        self.netWeightSpinBox.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.netWeightSpinBox.setFont(font)
        self.netWeightSpinBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.netWeightSpinBox.setAutoFillBackground(True)
        self.netWeightSpinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.netWeightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.netWeightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.netWeightSpinBox.setMaximum(999999.0)
        self.netWeightSpinBox.setProperty("value", 999999.0)
        self.netWeightSpinBox.setObjectName("netWeightSpinBox")
        self.weightLayout.addWidget(self.netWeightSpinBox)
        self.verticalLayout.addLayout(self.weightLayout)
        self.line = QtGui.QFrame(CloseTicket)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.dialogButtonsLayout = QtGui.QHBoxLayout()
        self.dialogButtonsLayout.setObjectName("dialogButtonsLayout")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.dialogButtonsLayout.addItem(spacerItem5)
        self.cancelButton = QtGui.QPushButton(CloseTicket)
        self.cancelButton.setObjectName("cancelButton")
        self.dialogButtonsLayout.addWidget(self.cancelButton)
        self.closeTicketButton = QtGui.QPushButton(CloseTicket)
        self.closeTicketButton.setObjectName("closeTicketButton")
        self.dialogButtonsLayout.addWidget(self.closeTicketButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.dialogButtonsLayout.addItem(spacerItem6)
        self.label_3 = QtGui.QLabel(CloseTicket)
        self.label_3.setObjectName("label_3")
        self.dialogButtonsLayout.addWidget(self.label_3)
        self.diffSpinBox = QtGui.QDoubleSpinBox(CloseTicket)
        self.diffSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.diffSpinBox.setFont(font)
        self.diffSpinBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.diffSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diffSpinBox.setReadOnly(True)
        self.diffSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.diffSpinBox.setMinimum(-999.0)
        self.diffSpinBox.setMaximum(999.0)
        self.diffSpinBox.setObjectName("diffSpinBox")
        self.dialogButtonsLayout.addWidget(self.diffSpinBox)
        self.verticalLayout.addLayout(self.dialogButtonsLayout)

        self.retranslateUi(CloseTicket)
        QtCore.QMetaObject.connectSlotsByName(CloseTicket)

    def retranslateUi(self, CloseTicket):
        CloseTicket.setWindowTitle(QtGui.QApplication.translate("CloseTicket", "Cerrar ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.ticketTypeLabel.setText(QtGui.QApplication.translate("CloseTicket", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.receptionButton.setText(QtGui.QApplication.translate("CloseTicket", "Recepción", None, QtGui.QApplication.UnicodeUTF8))
        self.dispatchButton.setText(QtGui.QApplication.translate("CloseTicket", "Despacho", None, QtGui.QApplication.UnicodeUTF8))
        self.numberLabel.setText(QtGui.QApplication.translate("CloseTicket", "Número", None, QtGui.QApplication.UnicodeUTF8))
        self.driverLabel.setText(QtGui.QApplication.translate("CloseTicket", "Chofer", None, QtGui.QApplication.UnicodeUTF8))
        self.truckLabel.setText(QtGui.QApplication.translate("CloseTicket", "Camión", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CloseTicket", "Peso de entrada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CloseTicket", "Peso de salida", None, QtGui.QApplication.UnicodeUTF8))
        self.captureWeightButton.setText(QtGui.QApplication.translate("CloseTicket", "Capturar peso", None, QtGui.QApplication.UnicodeUTF8))
        self.incomingWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.outgoingWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.manualCheckBox.setText(QtGui.QApplication.translate("CloseTicket", "Captura manual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CloseTicket", "Cliente/Fábrica", None, QtGui.QApplication.UnicodeUTF8))
        self.addClientButton.setText(QtGui.QApplication.translate("CloseTicket", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CloseTicket", "Dirección", None, QtGui.QApplication.UnicodeUTF8))
        self.commentLabel.setText(QtGui.QApplication.translate("CloseTicket", "Comentario", None, QtGui.QApplication.UnicodeUTF8))
        self.transactionsLabel.setText(QtGui.QApplication.translate("CloseTicket", "Transacciones", None, QtGui.QApplication.UnicodeUTF8))
        self.addTransactionButton.setText(QtGui.QApplication.translate("CloseTicket", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.removeTransactionButton.setText(QtGui.QApplication.translate("CloseTicket", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.transactionsTotalLabel.setText(QtGui.QApplication.translate("CloseTicket", "Total transacciones", None, QtGui.QApplication.UnicodeUTF8))
        self.transactionsTotalSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CloseTicket", "Tipo de documento", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CloseTicket", "Número de documento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("CloseTicket", "Peso Proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.providerWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("CloseTicket", "Peso bruto", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CloseTicket", "Peso tara", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CloseTicket", "Peso neto", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("CloseTicket", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.closeTicketButton.setText(QtGui.QApplication.translate("CloseTicket", "Cerrar ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CloseTicket", "Diferencia", None, QtGui.QApplication.UnicodeUTF8))
        self.diffSpinBox.setSuffix(QtGui.QApplication.translate("CloseTicket", " %", None, QtGui.QApplication.UnicodeUTF8))

from . import pixmaps_rc
