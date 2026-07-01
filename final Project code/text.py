import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# --- 1. LOGIN SCREEN ---
class SimpleLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1100, 800)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Main Title
        self.title1 = QLabel("Grocery Billing Management System", self)
        self.title1.setGeometry(250, 150, 600, 50)
        self.title1.setFont(QFont("Arial", 20, QFont.Bold))
        self.title1.setAlignment(Qt.AlignCenter)
        self.title1.setStyleSheet("color: #333333;")

        # Sub Title
        self.title2 = QLabel("Login page", self)
        self.title2.setGeometry(450, 220, 200, 40)
        self.title2.setFont(QFont("Arial", 16))
        self.title2.setAlignment(Qt.AlignCenter)
        self.title2.setStyleSheet("color: #555555;")

        # Username Input
        self.lbl_user = QLabel("Username:", self)
        self.lbl_user.setGeometry(350, 320, 100, 35)
        self.lbl_user.setFont(QFont("Arial", 12))
        
        self.Username = QLineEdit(self)
        self.Username.setGeometry(470, 320, 250, 35)
        self.Username.setStyleSheet("background-color: white; border: 1px solid #7f7f7f; border-radius: 3px; padding-left: 5px; font-size: 14px;")

        # Password Input
        self.lbl_pass = QLabel("Password:", self)
        self.lbl_pass.setGeometry(350, 380, 100, 35)
        self.lbl_pass.setFont(QFont("Arial", 12))
        
        self.Password = QLineEdit(self)
        self.Password.setGeometry(470, 380, 250, 35)
        self.Password.setEchoMode(QLineEdit.Password)
        self.Password.setStyleSheet("background-color: white; border: 1px solid #7f7f7f; border-radius: 3px; padding-left: 5px; font-size: 14px;")

        # Login Button (Green)
        self.login = QPushButton("login", self)
        self.login.setGeometry(430, 480, 100, 40)
        self.login.setFont(QFont("Arial", 11, QFont.Bold))
        self.login.setStyleSheet("background-color: #55ff7f; color: black; border: 1px solid #7f7f7f;")

        # Exit Button (Red)
        self.Exit = QPushButton("Exit", self)
        self.Exit.setGeometry(570, 480, 100, 40)
        self.Exit.setFont(QFont("Arial", 11, QFont.Bold))
        self.Exit.setStyleSheet("background-color: #ff8a8a; color: black; border: 1px solid #7f7f7f;")

# --- 2. BILLING SCREEN ---
class BillingScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1100, 800)
        self.setStyleSheet("background-color: #ffffff;")

        title = QLabel("Main Billing Screen", self)
        title.setGeometry(300, 200, 500, 50)
        title.setFont(QFont("Arial", 26, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #27ae60;")

        # Go to Stock Button (Blue)
        self.btn_stock = QPushButton("Go to Stock / Inventory", self)
        self.btn_stock.setGeometry(425, 350, 250, 45)
        self.btn_stock.setFont(QFont("Arial", 12, QFont.Bold))
        self.btn_stock.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px;")

# --- 3. STOCK SCREEN ---
class StockScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1100, 800)
        self.setStyleSheet("background-color: #ffffff;")

        title = QLabel("Stock Management Screen", self)
        title.setGeometry(300, 200, 500, 50)
        title.setFont(QFont("Arial", 26, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2980b9;")

        # Back to Billing Button (Yellow)
        self.btn_back = QPushButton("BACK to Billing", self)
        self.btn_back.setGeometry(450, 350, 200, 45)
        self.btn_back.setFont(QFont("Arial", 12, QFont.Bold))
        self.btn_back.setStyleSheet("background-color: #f1c40f; color: black; border-radius: 5px;")


# --- MAIN CONTROLLER ---
class GroceryApp:
    def __init__(self):
        self.stacked_widget = QStackedWidget()
        
        # Teeno windows create ho rahi hain
        self.login_screen = SimpleLogin()
        self.billing_screen = BillingScreen()
        self.stock_screen = StockScreen()
        
        # Stacked Widget mein daal rahe hain
        self.stacked_widget.addWidget(self.login_screen)   # Index 0
        self.stacked_widget.addWidget(self.billing_screen) # Index 1
        self.stacked_widget.addWidget(self.stock_screen)   # Index 2
        
        # Buttons ko functions ke sath connect kar rahe hain
        self.login_screen.login.clicked.connect(self.handle_login)
        self.login_screen.Exit.clicked.connect(sys.exit)
        self.billing_screen.btn_stock.clicked.connect(self.goto_stock)
        self.stock_screen.btn_back.clicked.connect(self.goto_billing)
        
        self.stacked_widget.setWindowTitle("Grocery Billing Management System")
        self.stacked_widget.resize(1100, 800)
        self.stacked_widget.show()

    def handle_login(self):
        # Username: admin | Password: 123
        if self.login_screen.Username.text() == "admin" and self.login_screen.Password.text() == "123":
            self.stacked_widget.setCurrentIndex(1) # Login sahi hone par Billing screen (Index 1) par jao
            self.login_screen.Username.clear()
            self.login_screen.Password.clear()
        else:
            QMessageBox.warning(self.stacked_widget, "Error", "Galat Username ya Password!")

    def goto_stock(self):
        self.stacked_widget.setCurrentIndex(2) # Stock screen (Index 2) par jao

    def goto_billing(self):
        self.stacked_widget.setCurrentIndex(1) # Wapas Billing screen (Index 1) par jao


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = GroceryApp()
    sys.exit(app.exec_())