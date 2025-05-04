# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_WinLinker(object):
    def setupUi(self, WinLinker):
        if not WinLinker.objectName():
            WinLinker.setObjectName(u"WinLinker")
        WinLinker.resize(720, 388)
        WinLinker.setMinimumSize(QSize(400, 388))
        WinLinker.setMaximumSize(QSize(16777215, 388))
        icon = QIcon()
        icon.addFile(u":/icon/winlinker.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        WinLinker.setWindowIcon(icon)
        WinLinker.setLocale(QLocale(QLocale.English, QLocale.World))
        self.verticalLayout = QVBoxLayout(WinLinker)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 75)
        self.label_Title = QLabel(WinLinker)
        self.label_Title.setObjectName(u"label_Title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Title.sizePolicy().hasHeightForWidth())
        self.label_Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.label_Title.setFont(font)

        self.verticalLayout.addWidget(self.label_Title)

        self.verticalSpacer_1 = QSpacerItem(0, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_1)

        self.groupBox_Destination = QGroupBox(WinLinker)
        self.groupBox_Destination.setObjectName(u"groupBox_Destination")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_Destination.sizePolicy().hasHeightForWidth())
        self.groupBox_Destination.setSizePolicy(sizePolicy1)
        self.groupBox_Destination.setFlat(True)
        self.gridLayout_Destination = QGridLayout(self.groupBox_Destination)
        self.gridLayout_Destination.setObjectName(u"gridLayout_Destination")
        self.gridLayout_Destination.setVerticalSpacing(2)
        self.gridLayout_Destination.setContentsMargins(2, -1, 2, -1)
        self.pushButton_SelectDestinationFile = QPushButton(self.groupBox_Destination)
        self.pushButton_SelectDestinationFile.setObjectName(u"pushButton_SelectDestinationFile")

        self.gridLayout_Destination.addWidget(self.pushButton_SelectDestinationFile, 0, 1, 1, 1)

        self.lineEdit_Destination = QLineEdit(self.groupBox_Destination)
        self.lineEdit_Destination.setObjectName(u"lineEdit_Destination")
        self.lineEdit_Destination.setMinimumSize(QSize(21, 0))

        self.gridLayout_Destination.addWidget(self.lineEdit_Destination, 0, 0, 1, 1)

        self.pushButton_SelectDestinationFolder = QPushButton(self.groupBox_Destination)
        self.pushButton_SelectDestinationFolder.setObjectName(u"pushButton_SelectDestinationFolder")

        self.gridLayout_Destination.addWidget(self.pushButton_SelectDestinationFolder, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_Destination)

        self.verticalSpacer_2 = QSpacerItem(0, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.groupBox_Entrance = QGroupBox(WinLinker)
        self.groupBox_Entrance.setObjectName(u"groupBox_Entrance")
        sizePolicy1.setHeightForWidth(self.groupBox_Entrance.sizePolicy().hasHeightForWidth())
        self.groupBox_Entrance.setSizePolicy(sizePolicy1)
        self.groupBox_Entrance.setMinimumSize(QSize(0, 127))
        self.groupBox_Entrance.setFlat(True)
        self.gridLayout_Entrance = QGridLayout(self.groupBox_Entrance)
        self.gridLayout_Entrance.setObjectName(u"gridLayout_Entrance")
        self.gridLayout_Entrance.setVerticalSpacing(2)
        self.gridLayout_Entrance.setContentsMargins(2, -1, 2, -1)
        self.pushButton_SelectEntranceFolder = QPushButton(self.groupBox_Entrance)
        self.pushButton_SelectEntranceFolder.setObjectName(u"pushButton_SelectEntranceFolder")

        self.gridLayout_Entrance.addWidget(self.pushButton_SelectEntranceFolder, 4, 1, 1, 1)

        self.comboBox_LinkType = QComboBox(self.groupBox_Entrance)
        self.comboBox_LinkType.setObjectName(u"comboBox_LinkType")
        sizePolicy.setHeightForWidth(self.comboBox_LinkType.sizePolicy().hasHeightForWidth())
        self.comboBox_LinkType.setSizePolicy(sizePolicy)
        self.comboBox_LinkType.setMinimumSize(QSize(0, 22))
        self.comboBox_LinkType.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_Entrance.addWidget(self.comboBox_LinkType, 1, 1, 1, 1)

        self.label_EntranceLocation = QLabel(self.groupBox_Entrance)
        self.label_EntranceLocation.setObjectName(u"label_EntranceLocation")

        self.gridLayout_Entrance.addWidget(self.label_EntranceLocation, 3, 0, 1, 1)

        self.lineEdit_EntranceName = QLineEdit(self.groupBox_Entrance)
        self.lineEdit_EntranceName.setObjectName(u"lineEdit_EntranceName")
        self.lineEdit_EntranceName.setMinimumSize(QSize(0, 21))

        self.gridLayout_Entrance.addWidget(self.lineEdit_EntranceName, 1, 0, 1, 1)

        self.lineEdit_EntranceFolder = QLineEdit(self.groupBox_Entrance)
        self.lineEdit_EntranceFolder.setObjectName(u"lineEdit_EntranceFolder")
        self.lineEdit_EntranceFolder.setMinimumSize(QSize(0, 21))

        self.gridLayout_Entrance.addWidget(self.lineEdit_EntranceFolder, 4, 0, 1, 1)

        self.pushButton_Create = QPushButton(self.groupBox_Entrance)
        self.pushButton_Create.setObjectName(u"pushButton_Create")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_Create.sizePolicy().hasHeightForWidth())
        self.pushButton_Create.setSizePolicy(sizePolicy2)

        self.gridLayout_Entrance.addWidget(self.pushButton_Create, 1, 2, 4, 1)

        self.verticalSpacer_3 = QSpacerItem(0, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_Entrance.addItem(self.verticalSpacer_3, 2, 0, 1, 2)

        self.label_EntranceName = QLabel(self.groupBox_Entrance)
        self.label_EntranceName.setObjectName(u"label_EntranceName")

        self.gridLayout_Entrance.addWidget(self.label_EntranceName, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_Entrance)

        QWidget.setTabOrder(self.lineEdit_Destination, self.pushButton_SelectDestinationFile)
        QWidget.setTabOrder(self.pushButton_SelectDestinationFile, self.pushButton_SelectDestinationFolder)
        QWidget.setTabOrder(self.pushButton_SelectDestinationFolder, self.lineEdit_EntranceName)
        QWidget.setTabOrder(self.lineEdit_EntranceName, self.comboBox_LinkType)
        QWidget.setTabOrder(self.comboBox_LinkType, self.lineEdit_EntranceFolder)
        QWidget.setTabOrder(self.lineEdit_EntranceFolder, self.pushButton_SelectEntranceFolder)
        QWidget.setTabOrder(self.pushButton_SelectEntranceFolder, self.pushButton_Create)

        self.retranslateUi(WinLinker)

        QMetaObject.connectSlotsByName(WinLinker)
    # setupUi

    def retranslateUi(self, WinLinker):
        WinLinker.setWindowTitle(QCoreApplication.translate("WinLinker", u"WinLinker", None))
        self.label_Title.setText(QCoreApplication.translate("WinLinker", u"Create a Link", None))
        self.groupBox_Destination.setTitle(QCoreApplication.translate("WinLinker", u"Destination", None))
        self.pushButton_SelectDestinationFile.setText(QCoreApplication.translate("WinLinker", u"File", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Destination.setToolTip(QCoreApplication.translate("WinLinker", u"Path to the destination", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_SelectDestinationFolder.setText(QCoreApplication.translate("WinLinker", u"Folder", None))
        self.groupBox_Entrance.setTitle(QCoreApplication.translate("WinLinker", u"Entrance", None))
        self.pushButton_SelectEntranceFolder.setText(QCoreApplication.translate("WinLinker", u"Select", None))
        self.label_EntranceLocation.setText(QCoreApplication.translate("WinLinker", u"Folder", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_EntranceName.setToolTip(QCoreApplication.translate("WinLinker", u"Name of the link", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_EntranceFolder.setToolTip(QCoreApplication.translate("WinLinker", u"Path to the folder where the the link is placed", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Create.setText(QCoreApplication.translate("WinLinker", u"Create", None))
        self.label_EntranceName.setText(QCoreApplication.translate("WinLinker", u"Name", None))
    # retranslateUi

