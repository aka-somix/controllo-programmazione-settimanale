from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QTextEdit
from modules.widgets import g_constants as g_const
from modules.csv_check import CheckCsv
from modules import __version__


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        # File Settings 
        self.filename = None
        self.uploadedFileLabel = None
        self.checkFileButton = None
        self.outputTextArea = None
        
        # Checker
        self.checker = CheckCsv()
        
        # init ui 
        self.__init_ui__()
        
    def __init_ui__(self):
        
        # main Layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(60,0,60,0)

        # ------------------ TOP LAYOUT ------------------
        topLayout = QHBoxLayout()
        topLayout.setContentsMargins(0,80,0,30)
        
        # upload file label 
        uploadFileLabel = QLabel()
        uploadFileLabel.setText(f"<font color={g_const.primary_color}>1. Carica File Programmazione</font>")
        uploadFileLabel.setFont(QFont('Helvetica', g_const.font_size))

        # Upload file button
        uploadFileButton = QPushButton("Scegli file Excel")
        uploadFileButton.setFont(QFont('Helvetica', g_const.font_size_small))
        uploadFileButton.setCheckable(True)
        uploadFileButton.clicked.connect(self.openFileNameDialog)
        
        topLayout.addWidget(uploadFileLabel)
        topLayout.addWidget(uploadFileButton)   

        # ------------------ BODY LAYOUT ------------------
        bodyLayout = QVBoxLayout()
        bodyLayout.setContentsMargins(0,0,0,80)

        # uploaded file label
        self.uploadedFileLabel = QLabel()
        self.uploadedFileLabel.setFont(QFont('Helvetica', g_const.font_size_small))
        self.uploadedFileLabel.setContentsMargins(0,0,0,60)
        bodyLayout.addWidget(self.uploadedFileLabel)
        
        # start check label 
        startCheckLabel = QLabel()
        startCheckLabel.setText(f"<font color={g_const.primary_color}>2. Avvia Controllo File </font>")
        startCheckLabel.setFont(QFont('Helvetica', g_const.font_size))
        bodyLayout.addWidget(startCheckLabel)
        
        # check file button
        self.checkFileButton = QPushButton("Avvia")
        self.checkFileButton.setFont(QFont('Helvetica', g_const.font_size_small))
        self.checkFileButton.setEnabled(False)
        self.checkFileButton.setCheckable(True)
        self.checkFileButton.clicked.connect(self.check_week)
        bodyLayout.addWidget(self.checkFileButton)
        
        # output text area
        self.outputTextArea = QTextEdit()
        self.outputTextArea.setReadOnly(True)
        self.setFont(QFont('Helvetica', g_const.font_size_small))
        self.outputTextArea.setPlainText("Pronto ad iniziare.")
        bodyLayout.addWidget(self.outputTextArea)
        
        # ------------------ FOOTER LAYOUT ------------------
        footerLayout = QVBoxLayout()
        footerLayout.setContentsMargins(0,30,0,0)
        
        footerLabel = QLabel()
        footerLabel.setText(f"<font color={g_const.secondary_color}> {__version__} Made with ❤ by Salvatore Cirone </font>")
        footerLabel.setFont(QFont('Helvetica', g_const.font_size_smaller))
        footerLabel.setAlignment(QtCore.Qt.AlignRight)
        footerLayout.addWidget(footerLabel)
        
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bodyLayout)
        mainLayout.addLayout(footerLayout)
        self.setLayout(mainLayout)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Excel Files (*.xlsx);;All Files (*)", options=options)
        if filename:
            self.uploadedFileLabel.setText(f"<font color={g_const.secondary_color}>File corrente: {filename}</font>")
            if filename.endswith('.xlsx'):
                self.filename = filename
                self.outputTextArea.setPlainText("Pronto ad iniziare.")
                self.checkFileButton.setEnabled(True)
                self.checker.set_document(self.filename)
            else:
                self.checkFileButton.setEnabled(False)
                self.outputTextArea.setText(f"<font color={g_const.error_color}>{filename} non è un file Excel</font>")
                
                

    def check_week(self):
        self.outputTextArea.setPlainText("Processando\n")
        self.checkFileButton.setEnabled(False)
        
        errors, warnings = self.checker.check_file()
        messages = ""
        
        if len(errors) == 0 and len(warnings) == 0:
            messages = f"<font color={g_const.success_color}> Programmazione Corretta! </font>"
        else:
            errors.extend(warnings)
            for mes in errors:
                messages += f"{mes}\n"
        
        self.outputTextArea.setText(messages)
        self.checkFileButton.setEnabled(True)
