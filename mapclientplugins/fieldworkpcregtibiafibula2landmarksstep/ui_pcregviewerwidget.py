# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/pcregviewerwidget.ui'
#
# Created: Fri Oct  9 13:51:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1263, 762)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget1 = QtGui.QWidget(self.widget)
        self.widget1.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtGui.QTableWidget(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBoxLM = QtGui.QComboBox(self.widget1)
        self.comboBoxLM.setObjectName("comboBoxLM")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxLM)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBoxMM = QtGui.QComboBox(self.widget1)
        self.comboBoxMM.setObjectName("comboBoxMM")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBoxMM)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBoxTT = QtGui.QComboBox(self.widget1)
        self.comboBoxTT.setObjectName("comboBoxTT")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBoxTT)
        self.comboBoxMC = QtGui.QComboBox(self.widget1)
        self.comboBoxMC.setObjectName("comboBoxMC")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxMC)
        self.comboBoxLC = QtGui.QComboBox(self.widget1)
        self.comboBoxLC.setObjectName("comboBoxLC")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxLC)
        self.comboBoxKC = QtGui.QComboBox(self.widget1)
        self.comboBoxKC.setObjectName("comboBoxKC")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.comboBoxKC)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.doubleSpinBoxMarkerOffset = QtGui.QDoubleSpinBox(self.widget1)
        self.doubleSpinBoxMarkerOffset.setObjectName("doubleSpinBoxMarkerOffset")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMarkerOffset)
        self.label_9 = QtGui.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.regButton = QtGui.QPushButton(self.widget1)
        self.regButton.setObjectName("regButton")
        self.gridLayout_2.addWidget(self.regButton, 0, 0, 1, 1)
        self.resetButton = QtGui.QPushButton(self.widget1)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout_2.addWidget(self.resetButton, 0, 1, 1, 1)
        self.acceptButton = QtGui.QPushButton(self.widget1)
        self.acceptButton.setObjectName("acceptButton")
        self.gridLayout_2.addWidget(self.acceptButton, 1, 1, 1, 1)
        self.abortButton = QtGui.QPushButton(self.widget1)
        self.abortButton.setObjectName("abortButton")
        self.gridLayout_2.addWidget(self.abortButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox = QtGui.QGroupBox(self.widget1)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditTransformation = QtGui.QLineEdit(self.groupBox)
        self.lineEditTransformation.setReadOnly(True)
        self.lineEditTransformation.setObjectName("lineEditTransformation")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditTransformation)
        self.lineEditRMSE = QtGui.QLineEdit(self.groupBox)
        self.lineEditRMSE.setReadOnly(True)
        self.lineEditRMSE.setObjectName("lineEditRMSE")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditRMSE)
        self.verticalLayout.addWidget(self.groupBox)
        self.screenshotgroup = QtGui.QGroupBox(self.widget1)
        self.screenshotgroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.screenshotgroup.setObjectName("screenshotgroup")
        self.formLayout = QtGui.QFormLayout(self.screenshotgroup)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.pixelsXLabel = QtGui.QLabel(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy)
        self.pixelsXLabel.setObjectName("pixelsXLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pixelsXLabel)
        self.screenshotPixelXLineEdit = QtGui.QLineEdit(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelXLineEdit.setObjectName("screenshotPixelXLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.screenshotPixelXLineEdit)
        self.pixelsYLabel = QtGui.QLabel(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy)
        self.pixelsYLabel.setObjectName("pixelsYLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pixelsYLabel)
        self.screenshotPixelYLineEdit = QtGui.QLineEdit(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelYLineEdit.setObjectName("screenshotPixelYLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.screenshotPixelYLineEdit)
        self.screenshotFilenameLabel = QtGui.QLabel(self.screenshotgroup)
        self.screenshotFilenameLabel.setObjectName("screenshotFilenameLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.screenshotFilenameLabel)
        self.screenshotFilenameLineEdit = QtGui.QLineEdit(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy)
        self.screenshotFilenameLineEdit.setObjectName("screenshotFilenameLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.screenshotFilenameLineEdit)
        self.screenshotSaveButton = QtGui.QPushButton(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy)
        self.screenshotSaveButton.setObjectName("screenshotSaveButton")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.screenshotSaveButton)
        self.verticalLayout.addWidget(self.screenshotgroup)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.widget1, 0, 0, 1, 1)
        self.MayaviScene = MayaviSceneWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy)
        self.MayaviScene.setObjectName("MayaviScene")
        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tableWidget, self.comboBoxLC)
        Dialog.setTabOrder(self.comboBoxLC, self.comboBoxMC)
        Dialog.setTabOrder(self.comboBoxMC, self.comboBoxLM)
        Dialog.setTabOrder(self.comboBoxLM, self.comboBoxMM)
        Dialog.setTabOrder(self.comboBoxMM, self.comboBoxTT)
        Dialog.setTabOrder(self.comboBoxTT, self.comboBoxKC)
        Dialog.setTabOrder(self.comboBoxKC, self.doubleSpinBoxMarkerOffset)
        Dialog.setTabOrder(self.doubleSpinBoxMarkerOffset, self.regButton)
        Dialog.setTabOrder(self.regButton, self.resetButton)
        Dialog.setTabOrder(self.resetButton, self.abortButton)
        Dialog.setTabOrder(self.abortButton, self.acceptButton)
        Dialog.setTabOrder(self.acceptButton, self.lineEditRMSE)
        Dialog.setTabOrder(self.lineEditRMSE, self.lineEditTransformation)
        Dialog.setTabOrder(self.lineEditTransformation, self.screenshotPixelXLineEdit)
        Dialog.setTabOrder(self.screenshotPixelXLineEdit, self.screenshotPixelYLineEdit)
        Dialog.setTabOrder(self.screenshotPixelYLineEdit, self.screenshotFilenameLineEdit)
        Dialog.setTabOrder(self.screenshotFilenameLineEdit, self.screenshotSaveButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Tibia Fibula PCA Landmark Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Lat. Maleolus:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Med. Maleolus:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Tib. Tuberosity:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Lat. Epicondyle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Med. Epicondyle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Knee Centre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Marker Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.regButton.setText(QtGui.QApplication.translate("Dialog", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptButton.setText(QtGui.QApplication.translate("Dialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.abortButton.setText(QtGui.QApplication.translate("Dialog", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Registration Results", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "RMSE:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Transformation:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotgroup.setTitle(QtGui.QApplication.translate("Dialog", "Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsXLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels X:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelXLineEdit.setText(QtGui.QApplication.translate("Dialog", "800", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsYLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelYLineEdit.setText(QtGui.QApplication.translate("Dialog", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLabel.setText(QtGui.QApplication.translate("Dialog", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLineEdit.setText(QtGui.QApplication.translate("Dialog", "screenshot.png", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotSaveButton.setText(QtGui.QApplication.translate("Dialog", "Save Screenshot", None, QtGui.QApplication.UnicodeUTF8))

from gias2.mappluginutils.mayaviviewer import MayaviSceneWidget
