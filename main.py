import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFrame, QSpacerItem,
                             QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon


class ImprovedEmployeeForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro de Empleados')
        self.setFixedSize(600, 500)  # Tamaño más grande
        self.setWindowIcon(QIcon('user_icon.png'))  # Opcional
        self.initUI()

    def initUI(self):
        # Configuración principal
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f2f5;
            }
            QFrame {
                background-color: white;
                border-radius: 12px;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)

        # Frame principal
        form_frame = QFrame()
        form_frame.setFixedSize(QSize(500, 400))
        form_layout = QVBoxLayout(form_frame)
        form_layout.setContentsMargins(40, 30, 40, 30)
        form_layout.setSpacing(25)

        # Título
        title = QLabel('REGISTRO DE EMPLEADOS')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                padding-bottom: 10px;
                border-bottom: 2px solid #3498db;
                margin-bottom: 20px;
            }
        """)
        title.setFont(QFont('Segoe UI', 12, QFont.Bold))

        # Sección de campos
        fields_layout = QVBoxLayout()
        fields_layout.setSpacing(15)

        # Campo Nombre
        name_layout = QVBoxLayout()
        name_label = QLabel('Nombre completo:')
        name_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #34495e;
                font-weight: 600;
                margin-bottom: 5px;
            }
        """)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Ej: Juan Pérez González')
        self.name_input.setMinimumHeight(40)
        self.name_input.setStyleSheet("""
            QLineEdit {
                padding: 8px 12px;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                font-size: 15px;
                background-color: #f8f9fa;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: white;
            }
        """)

        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        # Campo Correo
        email_layout = QVBoxLayout()
        email_label = QLabel('Correo electrónico:')
        email_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #34495e;
                font-weight: 600;
                margin-bottom: 5px;
            }
        """)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('Ej: juan.perez@empresa.com')
        self.email_input.setMinimumHeight(40)
        self.email_input.setStyleSheet("""
            QLineEdit {
                padding: 8px 12px;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                font-size: 15px;
                background-color: #f8f9fa;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: white;
            }
        """)

        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_input)

        # Espaciador
        spacer = QSpacerItem(20, 30, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)

        # Botón
        button_layout = QHBoxLayout()
        register_btn = QPushButton('REGISTRAR EMPLEADO')
        register_btn.setCursor(Qt.PointingHandCursor)
        register_btn.setMinimumHeight(45)
        register_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 0 30px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6ea4;
            }
        """)
        button_layout.addWidget(register_btn, alignment=Qt.AlignCenter)

        # Ensamblaje final
        fields_layout.addLayout(name_layout)
        fields_layout.addLayout(email_layout)
        fields_layout.addItem(spacer)
        fields_layout.addLayout(button_layout)

        form_layout.addWidget(title)
        form_layout.addLayout(fields_layout)

        main_layout.addWidget(form_frame)
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ImprovedEmployeeForm()
    window.show()
    sys.exit(app.exec_())
