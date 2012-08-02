# -*- coding: utf-8 -*-

import os
import settings
from PySide import QtGui, QtCore
from ui_main import Ui_Main
from new_ticket import NewTicket
from close_ticket import CloseTicket
from mango.api import API

class Main(QtGui.QMainWindow):
  def __init__(self):
    super(Main, self).__init__()
    self.ui = Ui_Main()
    self.ui.setupUi(self)
    self.enabled = False
    self.ticketsTableModel = TicketsTableModel([])
    self.ui.ticketsTableView.setModel(self.ticketsTableModel)
    horizontalHeader = self.ui.ticketsTableView.horizontalHeader()
    horizontalHeader.setResizeMode(QtGui.QHeaderView.ResizeToContents)
    self.api = API(settings.SERVERNAME, settings.SERVERPORT)
    self.api.login(settings.USERNAME, settings.USERPASSWORD)
    
    self.ui.actionNewReception.triggered.connect(self.openTicket)
    self.ui.actionNewDispatch.triggered.connect(self.openTicket)
    self.ui.refreshButton.clicked.connect(self.getTickets)
    self.api.loginFinished.connect(self.loginFinished)
    self.api.getTicketsFinished.connect(self.getTicketsFinished)
    self.api.createTicketFinished.connect(self.getTickets)
    self.api.closeTicketFinished.connect(self.printTicket)
    self.api.printTicketFinished.connect(self.printTicketFinished)
    self.ui.ticketsTableView.doubleClicked.connect(self.closeTicket)
    
    self.show()

  def openTicket(self):
    actionSender = self.sender()
    if actionSender == self.ui.actionNewReception:
      newTicketDialog = NewTicket(1, self)
    elif actionSender == self.ui.actionNewDispatch:
      newTicketDialog = NewTicket(2, self)
    self.api.get_drivers()
    self.api.getDriversFinished.connect(newTicketDialog.getDriversFinished)
    self.api.get_trucks()
    self.api.getTrucksFinished.connect(newTicketDialog.getTrucksFinished)
    
    if newTicketDialog.exec_() == QtGui.QDialog.Accepted:
      self.api.create_ticket(newTicketDialog.ticket)
    newTicketDialog.st.alive = False

  def closeTicket(self, tableIndex):
    ticket = self.ticketsTableModel.getTicket(tableIndex.row())
    closeTicketDialog = CloseTicket(ticket, self)
    self.api.get_clients()
    self.api.getClientsFinished.connect(closeTicketDialog.getClientsFinished)
    self.api.get_factories()
    self.api.getFactoriesFinished.connect(closeTicketDialog.getFactoriesFinished)
    self.api.get_warehouses()
    self.api.getWarehousesFinished.connect(closeTicketDialog.getWarehousesFinished)
    if closeTicketDialog.exec_() == QtGui.QDialog.Accepted:
      self.api.close_ticket(closeTicketDialog.ticket)
      self.currentTicket = closeTicketDialog.ticket
    closeTicketDialog.st.alive = False
      
  def printTicket(self):
    self.getTickets()
    self.api.print_ticket(self.currentTicket)
    
  def printTicketFinished(self, data):
    dialogStrings = QtGui.QFileDialog.getSaveFileName(self, "Guardar ticket", "", "Archivo PDF (*.pdf)")
    filename = dialogStrings[0]
    if filename != '':
      _file = QtCore.QFile(filename)
      _file.open(QtCore.QIODevice.WriteOnly)
      _file.write(data)
      _file.close
      if os.name == "posix":
        os.system("xdg-open %s" % filename)
      elif os.name == "nt":
        os.startfile(filename)

  def loginFinished(self):
    self.enabled = True
    self.ui.refreshButton.setEnabled(False)
    self.api.get_tickets()

  def getTickets(self):
    self.ui.refreshButton.setEnabled(False)
    self.api.get_tickets()
  
  def getTicketsFinished(self, tickets):
    self.ui.ticketsTableView.model().refreshTickets(tickets)
    self.ui.refreshButton.setEnabled(True)
    
class TicketsTableModel(QtCore.QAbstractTableModel):
  def __init__(self, tickets, parent = None):
    super(TicketsTableModel, self).__init__(parent)
    self._tickets = tickets
    self._headers = [u'Número', 'Tipo', 'Placa', 'Peso de entrada', 'Fecha de entrada', 'Comentario']
    
  def getTicket(self, row):
    return self._tickets[row]
    
  def refreshTickets(self, tickets):
    self.beginResetModel()
    self._tickets = tickets
    self.endResetModel()
    
  def headerData(self, section, orientation, role):
    if role == QtCore.Qt.DisplayRole:
      if orientation == QtCore.Qt.Horizontal:
        return self._headers[section]
        
  def rowCount(self, parent):
    return len(self._tickets)
    
  def columnCount(self, parent):
    return len(self._headers)
    
  def data(self, index, role):
    row = index.row()
    column = index.column()
    
    if role == QtCore.Qt.DisplayRole:
      if column == 0:
        return self._tickets[row].number
      elif column == 1:
        return self._tickets[row].ticket_type.code
      elif column == 2:
        return self._tickets[row].truck.license_plate
      elif column == 3:
        return "%s Kg" % self._tickets[row].incoming_weight
      elif column == 4:
        return self._tickets[row].incoming_date
      elif column == 5:
        return self._tickets[row].comment
    elif role == QtCore.Qt.TextAlignmentRole:
      if column == 3:
        return QtCore.Qt.AlignRight
      elif column == 5:
        return QtCore.Qt.AlignLeft
      else:
        return QtCore.Qt.AlignCenter
