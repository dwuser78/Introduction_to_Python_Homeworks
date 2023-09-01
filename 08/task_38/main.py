import sys
import os
import sqlite3
import csv
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QWidget, QFileDialog
from gui import Ui_MainWindow, Ui_DiagWindow

class DB():
    def __init__(self, file_name):
        super(DB, self).__init__()
        self.sqlite_connection, self.cursor = self.db_connect(file_name)

    def __del__(self):
        self.cursor.close()
        self.sqlite_connection.close()

    def db_connect(self, file_name):
        try:
            sqlite_connection = sqlite3.connect(file_name)
            cursor = sqlite_connection.cursor()
        except sqlite3.Error as error:
            print("Error connecting to the database: ", error)
        finally:
            if (sqlite_connection):
                return sqlite_connection, cursor

    def get_data(self, sql_query: str) -> list:
        self.cursor.execute(sql_query)

        return self.cursor.fetchall()

    def run_sql_query(self, sql_query: str):
        self.cursor.execute(sql_query)
        self.sqlite_connection.commit()

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Delete records...")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Are you sure you want to delete the records?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.resize(300, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(300, 100))
        self.setMaximumSize(QtCore.QSize(300, 100))

class EditDialog(QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main_wnd = root
        self.diag_wnd = Ui_DiagWindow()
        self.diag_wnd.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.diag_wnd.pushButton_2.clicked.connect(self.close)

    def edit_entry(self):
        recor_id = self.main_wnd.entry_id
        first_name = self.diag_wnd.lineEdit.text()
        last_name = self.diag_wnd.lineEdit_2.text()
        phone = self.diag_wnd.lineEdit_3.text()

        sql_query = "UPDATE contacts SET"
        sql_query += (f" first_name = '{first_name}', "
                      f"last_name = '{last_name}', phone = '{phone}' "
                      f"WHERE id = '{recor_id}';")

        self.main_wnd.contacts.run_sql_query(sql_query)
        self.main_wnd.get_all_records()

        self.main_wnd.main_from.pushButton_2.setEnabled(False)
        self.close()

    def add_entry(self):
        first_name = self.diag_wnd.lineEdit.text()
        last_name = self.diag_wnd.lineEdit_2.text()
        phone = self.diag_wnd.lineEdit_3.text()

        sql_query = "INSERT INTO contacts (first_name, last_name, phone) VALUES"
        sql_query += f" ('{first_name}', '{last_name}', '{phone}');"

        self.main_wnd.contacts.run_sql_query(sql_query)
        self.main_wnd.get_all_records()

        self.close()

class MainWnd(QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edit_dialog = EditDialog(self)
        self.main_from = Ui_MainWindow()
        self.main_from.setupUi(self)

        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.tableModel = QtGui.QStandardItemModel(parent=self)

        self.init_UI()
        self.main()

    def __del__(self):
        del self.contacts

    def init_UI(self):
        tableView = self.main_from.tableView

        self.tableModel.setHorizontalHeaderLabels(["id", "First Name",
                                                   "Last Name", "Phone"])

        icon_path = os.path.join(self.base_dir, "phone.png")
        self.setWindowIcon(QIcon(icon_path))

        self.main_from.lineEdit.setPlaceholderText("Enter the search data")

        tableView.setModel(self.tableModel)
        tableView.setColumnWidth(0, 8)
        tableView.setColumnWidth(1, 115)
        tableView.setColumnWidth(2, 120)
        tableView.setColumnWidth(3, 80)
        tableView.hideColumn(0)

        self.main_from.tableView.selectionModel() \
            .selectionChanged.connect(self.check_change_ability)
        self.main_from.lineEdit.textChanged.connect(self.search_entry)
        self.main_from.pushButton.clicked.connect(self.show_add_diag)
        self.main_from.pushButton_2.clicked.connect(self.show_edit_diag)
        self.main_from.pushButton_3.clicked.connect(self.del_selected)
        self.main_from.pushButton_4.clicked.connect(self.show_import_diag)
        self.main_from.pushButton_5.clicked.connect(self.search_entry)

    def show_data(self, records: list):
        columns = []

        self.tableModel.removeRows(0, self.main_from.tableView \
                                                        .model().rowCount())

        for curr_row in records:
            for i in range(len(curr_row)):
                columns.append(QtGui.QStandardItem(str(curr_row[i])))
            self.tableModel.appendRow(columns)
            columns.clear()

    def get_all_records(self):
        records = self.contacts.get_data("SELECT * FROM contacts ORDER BY "
                                         "last_name;")
        self.show_data(records)

    def check_change_ability(self):
        indexes = []

        indexes = self.main_from.tableView.selectedIndexes()

        if len(indexes) == 0:
            self.main_from.pushButton_3.setEnabled(False)
        elif len(indexes) > 1:
            self.main_from.pushButton_2.setEnabled(False)
            self.main_from.pushButton_3.setEnabled(True)
        else:
            self.main_from.pushButton_2.setEnabled(True)
            self.main_from.pushButton_3.setEnabled(True)

    def del_selected(self):
        indexes = []
        sql_query = "DELETE FROM contacts WHERE"

        indexes = self.main_from.tableView.selectedIndexes()
        for i, value in enumerate(indexes):
            sql_query += " id = '{}'".format(value.model() \
                                             .index(value.row(), 0).data())
            if i < len(indexes) - 1:
                sql_query += " OR"
            else:
                sql_query += ";"

        del_diag = CustomDialog()

        if del_diag.exec():
            self.contacts.run_sql_query(sql_query)
            self.get_all_records()
            self.main_from.pushButton_2.setEnabled(False)
            self.main_from.pushButton_3.setEnabled(False)


    def show_edit_diag(self):
        self.edit_dialog.setWindowTitle("Edit an entry")
        self.edit_dialog.diag_wnd.pushButton.setText("Apply")
        self.edit_dialog.diag_wnd.pushButton.clicked.connect(self.edit_dialog \
                                                                .edit_entry)

        curr_row = self.main_from.tableView.currentIndex().row()
        self.entry_id = self.main_from.tableView.model().index(curr_row, 0).data()
        
        value = self.main_from.tableView.model().index(curr_row, 1).data()
        self.edit_dialog.diag_wnd.lineEdit.setText(value)

        value = self.main_from.tableView.model().index(curr_row, 2).data()
        self.edit_dialog.diag_wnd.lineEdit_2.setText(value)
        
        value = self.main_from.tableView.model().index(curr_row, 3).data()
        self.edit_dialog.diag_wnd.lineEdit_3.setText(value)

        self.edit_dialog.exec()

    def show_add_diag(self):
        self.edit_dialog.setWindowTitle("Add an entry")
        self.edit_dialog.diag_wnd.pushButton.setText("Add")
        self.edit_dialog.diag_wnd.pushButton.clicked.connect(self.edit_dialog \
                                                                .add_entry)
        self.edit_dialog.diag_wnd.lineEdit.clear()
        self.edit_dialog.diag_wnd.lineEdit_2.clear()
        self.edit_dialog.diag_wnd.lineEdit_3.clear()

        self.edit_dialog.exec()

    def search_entry(self):
        search_str = self.main_from.lineEdit.text()

        sql_query = (f"SELECT * FROM contacts WHERE first_name "
                     f"LIKE '{search_str}%' OR last_name LIKE '{search_str}%' "
                     f"OR phone LIKE '{search_str}%' ORDER BY last_name;")

        records = self.contacts.get_data(sql_query)
        self.show_data(records)

    def show_import_diag(self):
        file_name = QFileDialog.getOpenFileName(self, "Import data from CSV",
                                               self.base_dir,
                                               "CSV Files (*.csv)")

        with open(file_name[0], "r") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=";")
            for i, csv_row in enumerate(csv_data):
                if i == 0:
                    bad_csv = False

                    if "first_name" not in csv_row:
                        bad_csv = True
                    elif "last_name" not in csv_row:
                        bad_csv = True
                    elif "phone" not in csv_row:
                        bad_csv = True

                    if bad_csv:
                        print("ERROR: Inappropriate CSV file format!")
                        return

                    sql_query_head = (f"INSERT INTO contacts ({csv_row[0]}, "
                                      f"{csv_row[1]}, {csv_row[2]}) VALUES")
                else:
                    sql_query= (f"{sql_query_head} ('{csv_row[0]}', "
                                f"'{csv_row[1]}', '{csv_row[2]}');")

                    self.contacts.run_sql_query(sql_query)
                    self.get_all_records()

    def main(self):
        db_path = os.path.join(self.base_dir, "phone_book.db")
        self.contacts = DB(db_path)

        self.get_all_records()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_wnd = MainWnd()
    main_wnd.show()
    sys.exit(app.exec_())