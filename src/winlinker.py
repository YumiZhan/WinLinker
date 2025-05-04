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
from typing import Any, Callable, Literal

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

from main_windows_ui import Ui_WinLinker


class WinLinkerUI(Ui_WinLinker):
    __linktypes: dict[str, Callable[[str, str], Any]] = {
        'hard': lambda entrance, destination: os.link(destination, entrance),
        'symbolic': lambda entrance, destination: os.symlink(destination, entrance, os.path.isdir(destination)),
        'junction': lambda entrance, destination: subprocess.run(f'mklink /J "{entrance}" "{destination}"', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE),
    }
    def __init__(self, destination: str = '', entrance_folder: str = '', entrance_name: str = ''):
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.lineEdit_Destination.setText(destination)
        self.lineEdit_Destination.setPlaceholderText(os.getcwd())
        self.lineEdit_Destination.editingFinished.connect(self.Update_EntranceInfo)
        self.pushButton_SelectDestinationFile.clicked.connect(lambda: self.Explore_Destination('file'))
        self.pushButton_SelectDestinationFolder.clicked.connect(lambda: self.Explore_Destination('folder'))
        self.lineEdit_EntranceName.setText(entrance_name)
        self.lineEdit_EntranceFolder.setText(entrance_folder)
        self.lineEdit_EntranceFolder.setPlaceholderText(os.getcwd())
        self.pushButton_SelectEntranceFolder.clicked.connect(self.Select_EntranceFolder)
        self.pushButton_Create.clicked.connect(self.Create_Link)
        self.Update_EntranceInfo()
    def Update_EntranceInfo(self) -> None:
        self.lineEdit_EntranceName.setPlaceholderText(os.path.basename(os.path.abspath(self.lineEdit_Destination.text())))
        self.comboBox_LinkType.clear()
        destination = os.path.abspath(self.lineEdit_Destination.text())
        if os.path.isfile(destination):
            self.comboBox_LinkType.addItems(('hard', 'symbolic'))
            self.pushButton_Create.setEnabled(True)
        elif os.path.isdir(destination):
            self.comboBox_LinkType.addItems(('symbolic', 'junction'))
            self.pushButton_Create.setEnabled(True)
        else:
            self.pushButton_Create.setDisabled(True)
    def Explore_Destination(self, destination_type: Literal['file', 'folder']) -> None:
        match destination_type:
            case 'file':
                destination, _ = QFileDialog.getOpenFileName(self.dialog, 'Select Destination', self.lineEdit_Destination.text())
            case 'folder':
                destination = QFileDialog.getExistingDirectory(self.dialog, 'Select Destination', self.lineEdit_Destination.text())
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
            match QMessageBox.warning(self.dialog, 'The path exists', f'Replace "{entrance_path}" with the link entrance?', QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No):
                case QMessageBox.StandardButton.Yes:
                    if os.path.isdir(entrance_path):
                        shutil.rmtree(entrance_path, False, onexc = lambda _, path, exc_info: QMessageBox.critical(self.dialog, 'Cannot remove item', f'Path: {path}\nException Info: {'; '.join(exc_info.args)}', QMessageBox.StandardButton.NoButton, QMessageBox.StandardButton.Ok))
                    else:
                        try:
                            os.remove(entrance_path)
                        except Exception as exception:
                            QMessageBox.critical(self.dialog, 'Cannot remove item', f'Path: {entrance_path}\nException Info: {'; '.join(exception.args)}', QMessageBox.StandardButton.NoButton, QMessageBox.StandardButton.Ok)
                case QMessageBox.StandardButton.No:
                    return
        WinLinkerUI.__linktypes[self.comboBox_LinkType.currentText()](entrance_path, self.lineEdit_Destination.text())

def main() -> None:
    argparser = ArgumentParser(description='WinLinker is a GUI tool to create symbolic/hard/junction links on Microsoft Windows')
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
