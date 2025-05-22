#   Copyright 2025 Yumin Zhan
#
#   This file if part of WinLinker.
#
#   WinLinker is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   WinLinker is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   Contact me at this email address: ZYumi0769@outlook.com

import os
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from typing import Literal

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

from main_windows_ui import Ui_WinLinker


class WinLinkerUI(Ui_WinLinker):
    def __init__(self, destination: str = '', entrance_folder: str = '', entrance_name: str = ''):
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.lineEdit_Destination.setText(destination)
        self.lineEdit_Destination.setPlaceholderText(os.getcwd())
        self.lineEdit_Destination.editingFinished.connect(self.Update_EntranceInfo)
        self.lineEdit_Destination.textChanged.connect(self.label_ActionResult.clear)
        self.pushButton_SelectDestinationFile.clicked.connect(lambda: self.Explore_Destination('file'))
        self.pushButton_SelectDestinationFolder.clicked.connect(lambda: self.Explore_Destination('folder'))
        self.lineEdit_EntranceName.setText(entrance_name)
        self.lineEdit_EntranceName.textChanged.connect(self.label_ActionResult.clear)
        self.comboBox_LinkType.currentTextChanged.connect(self.label_ActionResult.clear)
        self.lineEdit_EntranceFolder.setText(entrance_folder)
        self.lineEdit_EntranceFolder.setPlaceholderText(os.getcwd())
        self.lineEdit_EntranceFolder.textChanged.connect(self.label_ActionResult.clear)
        self.pushButton_SelectEntranceFolder.clicked.connect(self.Select_EntranceFolder)
        self.pushButton_Create.clicked.connect(self.Create_Link)
        self.Update_EntranceInfo()
    def Update_EntranceInfo(self) -> None:
        self.lineEdit_EntranceName.setPlaceholderText(os.path.basename(os.path.abspath(self.lineEdit_Destination.text())))
        self.comboBox_LinkType.clear()
        destination_path = os.path.abspath(self.lineEdit_Destination.text())
        Create_SymbolicLink = lambda entrance_path: os.symlink(destination_path, entrance_path, os.path.isdir(destination_path))
        if os.path.isfile(destination_path):
            self.comboBox_LinkType.addItem('hard', lambda entrance_path: os.link(destination_path, entrance_path))
            self.comboBox_LinkType.addItem('symbolic', Create_SymbolicLink)
            self.pushButton_Create.setEnabled(True)
        elif os.path.isdir(destination_path):
            self.comboBox_LinkType.addItem('symbolic', Create_SymbolicLink)
            self.comboBox_LinkType.addItem('junction', lambda entrance_path: subprocess.run(f'mklink /J "{entrance_path}" "{destination_path}"', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
            self.pushButton_Create.setEnabled(True)
        else:
            self.pushButton_Create.setDisabled(True)
    def Explore_Destination(self, destination_type: Literal['file', 'folder']) -> None:
        match destination_type:
            case 'file':
                destination, _ = QFileDialog.getOpenFileName(self.dialog, 'Select Destination', self.lineEdit_Destination.text())
            case 'folder':
                destination = QFileDialog.getExistingDirectory(self.dialog, 'Select Destination', lineEdit_Destination if os.path.isdir(lineEdit_Destination := self.lineEdit_Destination.text()) else os.path.dirname(lineEdit_Destination))
        if not destination:
            return
        self.lineEdit_Destination.setText(os.path.abspath(destination))
        self.Update_EntranceInfo()
    def Select_EntranceFolder(self) -> None:
        entrance_folder = QFileDialog.getExistingDirectory(self.dialog, 'Select folder where the Entrance is located', self.lineEdit_EntranceFolder.text())
        if not entrance_folder:
            return
        self.lineEdit_EntranceFolder.setText(os.path.abspath(entrance_folder))
    def Create_Link(self) -> None:
        entrance_folder = self.lineEdit_EntranceFolder.text()
        os.makedirs(entrance_folder, exist_ok=True)
        entrance_path = os.path.abspath(os.path.join(entrance_folder, self.lineEdit_EntranceName.text() if self.lineEdit_EntranceName.text() else self.lineEdit_EntranceName.placeholderText()))
        if os.path.exists(entrance_path):
            match QMessageBox.warning(self.dialog, 'The path exists', f'Replace "{entrance_path}" with the link entrance?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No):
                case QMessageBox.StandardButton.Yes:
                    try:
                        if os.path.islink(entrance_path) or os.path.isfile(entrance_path):
                            os.remove(entrance_path)
                        elif os.path.isdir(entrance_path):
                            shutil.rmtree(entrance_path)
                        else:
                            pass
                    except Exception as exception:
                        if QMessageBox.critical(self.dialog, 'Cannot remove item', f'Path: {entrance_path}\nException Info: {'\n'.join(exception.args)}', QMessageBox.StandardButton.Ignore | QMessageBox.StandardButton.Abort) is QMessageBox.StandardButton.Abort:
                            self.label_ActionResult.setText('Link creation cancelled')
                            return
                case QMessageBox.StandardButton.No:
                    self.label_ActionResult.setText('Link creation cancelled')
                    return
        try:
            self.comboBox_LinkType.currentData()(entrance_path)
        except Exception as exception:
            QMessageBox.critical(self.dialog, 'Failed to create link', f'Exception Info: {'\n'.join(map(str, exception.args))}')
            self.label_ActionResult.setText('Failed to create link')
            return
        self.label_ActionResult.setText('Link is created')

def main() -> None:
    argparser = ArgumentParser(description='WinLinker provides user-friendly GUI for creating hard/symbolic/junction links on Microsoft Windows')
    argparser.add_argument('-d', '--destination', metavar='Destination', type=str, default='', help='destination of the link')
    argparser.add_argument('-f', '--folder', metavar='Folder', type=str, default='', help='folder where the entrance of the link is located')
    argparser.add_argument('-n', '--name', metavar='Name', type=str, default='', help='name of the entrance')
    args = argparser.parse_args()
    app = QApplication(sys.argv)
    main_ui = WinLinkerUI(args.destination, args.folder, os.path.basename(args.name))
    main_ui.dialog.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
