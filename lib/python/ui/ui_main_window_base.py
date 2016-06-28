# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main_window_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        MainWindowBase.setObjectName("MainWindowBase")
        MainWindowBase.resize(902, 506)
        MainWindowBase.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputGraphicsView = OverlaidGraphicsView(self.groupBox)
        self.inputGraphicsView.setAcceptDrops(False)
        self.inputGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.inputGraphicsView.setObjectName("inputGraphicsView")
        self.verticalLayout.addWidget(self.inputGraphicsView)
        self.videoPlaybackWidget = VideoPlaybackWidget(self.groupBox)
        self.videoPlaybackWidget.setObjectName("videoPlaybackWidget")
        self.verticalLayout.addWidget(self.videoPlaybackWidget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.zoomedGraphicsView = OverlaidGraphicsView(self.groupBox_2)
        self.zoomedGraphicsView.setObjectName("zoomedGraphicsView")
        self.verticalLayout_2.addWidget(self.zoomedGraphicsView)
        self.horizontalWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.frameNoSpinBox = QtWidgets.QSpinBox(self.horizontalWidget)
        self.frameNoSpinBox.setMinimum(1)
        self.frameNoSpinBox.setMaximum(10000)
        self.frameNoSpinBox.setObjectName("frameNoSpinBox")
        self.horizontalLayout_5.addWidget(self.frameNoSpinBox)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.horizontalWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.radiusSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalWidget1)
        self.radiusSpinBox.setMinimum(5.0)
        self.radiusSpinBox.setObjectName("radiusSpinBox")
        self.horizontalLayout_3.addWidget(self.radiusSpinBox)
        self.verticalLayout_2.addWidget(self.horizontalWidget1)
        self.formWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formWidget.setObjectName("formWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.formWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.markDeltaSpinBox = QtWidgets.QSpinBox(self.formWidget)
        self.markDeltaSpinBox.setMinimum(30)
        self.markDeltaSpinBox.setMaximum(10000)
        self.markDeltaSpinBox.setProperty("value", 1800)
        self.markDeltaSpinBox.setObjectName("markDeltaSpinBox")
        self.horizontalLayout_2.addWidget(self.markDeltaSpinBox)
        self.verticalLayout_2.addWidget(self.formWidget)
        self.overlayCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.overlayCheckBox.setObjectName("overlayCheckBox")
        self.verticalLayout_2.addWidget(self.overlayCheckBox)
        self.horizontalLayout.addWidget(self.groupBox_2)
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        MainWindowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
        self.statusbar.setObjectName("statusbar")
        MainWindowBase.setStatusBar(self.statusbar)
        self.actionOpenCSVFile = QtWidgets.QAction(MainWindowBase)
        self.actionOpenCSVFile.setObjectName("actionOpenCSVFile")
        self.actionSaveDataFiles = QtWidgets.QAction(MainWindowBase)
        self.actionSaveDataFiles.setObjectName("actionSaveDataFiles")
        self.actionTrackingPathColor = QtWidgets.QAction(MainWindowBase)
        self.actionTrackingPathColor.setObjectName("actionTrackingPathColor")
        self.actionPath = QtWidgets.QAction(MainWindowBase)
        self.actionPath.setCheckable(True)
        self.actionPath.setChecked(True)
        self.actionPath.setObjectName("actionPath")
        self.actionCircle = QtWidgets.QAction(MainWindowBase)
        self.actionCircle.setCheckable(True)
        self.actionCircle.setChecked(True)
        self.actionCircle.setObjectName("actionCircle")
        self.actionIntervalMark = QtWidgets.QAction(MainWindowBase)
        self.actionIntervalMark.setCheckable(True)
        self.actionIntervalMark.setChecked(True)
        self.actionIntervalMark.setObjectName("actionIntervalMark")
        self.actionShape = QtWidgets.QAction(MainWindowBase)
        self.actionShape.setCheckable(True)
        self.actionShape.setChecked(True)
        self.actionShape.setObjectName("actionShape")
        self.actionSkeleton = QtWidgets.QAction(MainWindowBase)
        self.actionSkeleton.setCheckable(True)
        self.actionSkeleton.setChecked(True)
        self.actionSkeleton.setObjectName("actionSkeleton")
        self.actionArrow = QtWidgets.QAction(MainWindowBase)
        self.actionArrow.setCheckable(True)
        self.actionArrow.setChecked(True)
        self.actionArrow.setObjectName("actionArrow")
        self.actionOpenJSONFile = QtWidgets.QAction(MainWindowBase)
        self.actionOpenJSONFile.setObjectName("actionOpenJSONFile")
        self.actionOpenColorFile = QtWidgets.QAction(MainWindowBase)
        self.actionOpenColorFile.setObjectName("actionOpenColorFile")
        self.actionChangeOrderOfNum = QtWidgets.QAction(MainWindowBase)
        self.actionChangeOrderOfNum.setObjectName("actionChangeOrderOfNum")
        self.menuFile.addAction(self.actionOpenCSVFile)
        self.menuFile.addAction(self.actionOpenJSONFile)
        self.menuFile.addAction(self.actionOpenColorFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveDataFiles)
        self.menuSettings.addAction(self.actionTrackingPathColor)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionPath)
        self.menuSettings.addAction(self.actionCircle)
        self.menuSettings.addAction(self.actionIntervalMark)
        self.menuSettings.addAction(self.actionShape)
        self.menuSettings.addAction(self.actionSkeleton)
        self.menuSettings.addAction(self.actionArrow)
        self.menuData.addAction(self.actionChangeOrderOfNum)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(MainWindowBase)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

    def retranslateUi(self, MainWindowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBase.setWindowTitle(_translate("MainWindowBase", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindowBase", "Tracking"))
        self.groupBox_2.setTitle(_translate("MainWindowBase", "Zoom"))
        self.label_2.setText(_translate("MainWindowBase", "Path length:"))
        self.label.setText(_translate("MainWindowBase", "Circle radius:"))
        self.label_3.setText(_translate("MainWindowBase", "Mark interval:"))
        self.overlayCheckBox.setText(_translate("MainWindowBase", "Overlay"))
        self.menuFile.setTitle(_translate("MainWindowBase", "File"))
        self.menuSettings.setTitle(_translate("MainWindowBase", "View"))
        self.menuData.setTitle(_translate("MainWindowBase", "Edit"))
        self.actionOpenCSVFile.setText(_translate("MainWindowBase", "Open CSV File"))
        self.actionSaveDataFiles.setText(_translate("MainWindowBase", "Save Data FIles"))
        self.actionTrackingPathColor.setText(_translate("MainWindowBase", "Tracking Path Color"))
        self.actionPath.setText(_translate("MainWindowBase", "Path"))
        self.actionCircle.setText(_translate("MainWindowBase", "Circle"))
        self.actionIntervalMark.setText(_translate("MainWindowBase", "Interval Mark"))
        self.actionShape.setText(_translate("MainWindowBase", "Shape"))
        self.actionSkeleton.setText(_translate("MainWindowBase", "Skeleton"))
        self.actionArrow.setText(_translate("MainWindowBase", "Arrow"))
        self.actionOpenJSONFile.setText(_translate("MainWindowBase", "Open JSON File"))
        self.actionOpenColorFile.setText(_translate("MainWindowBase", "Open Color File"))
        self.actionChangeOrderOfNum.setText(_translate("MainWindowBase", "Change the order of individual numbers"))

from .overlaid_graphics_view import OverlaidGraphicsView
from .video_playback_widget import VideoPlaybackWidget
