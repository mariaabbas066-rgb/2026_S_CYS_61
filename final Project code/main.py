import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic

# ==========================================
# INTELLIGENT CONTENT-BASED UI FINDER
# ==========================================
def find_ui_by_content():
    login_path, billing_path, stock_path = None, None, None
    for file in os.listdir('.'):
        if os.path.isfile(file) and not file.endswith('.py') and not file.endswith('.mp4'):
            try:
                with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if "LOGIN" in content and "lineEdit_2" in content:
                        login_path = file
                    elif "Generate Bill" in content or "Add to Cart" in content:
                        billing_path = file
                    elif "Stock" in content or "lineEdit_11" in content or "Search Item" in content:
                        stock_path = file
            except Exception:
                continue
    return login_path, billing_path, stock_path

UI_LOGIN, UI_BILLING, UI_STOCK = find_ui_by_content()

# ==========================================
# SCREEN 1: LOGIN CONTROLLER (1 project)
# ==========================================
class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        if not UI_LOGIN:
            QMessageBox.critical(self, "Fatal Error", "Login UI file nahi mili!")
            sys.exit()
        uic.loadUi(UI_LOGIN, self)
        if hasattr(self, 'pushButton'): self.pushButton.clicked.connect(self.verify_login)
        if hasattr(self, 'pushButton_2'): self.pushButton_2.clicked.connect(self.close)

    def verify_login(self):
        user = self.lineEdit.text().strip() if hasattr(self, 'lineEdit') else ""
        password = self.lineEdit_2.text().strip() if hasattr(self, 'lineEdit_2') else ""
        if user == "admin" and password == "123":
            self.billing = BillingScreen()
            self.billing.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Ghalat Username ya Password!\nHint: admin / 123")

# ==========================================
# SCREEN 2: BILLING CONTROLLER (2 project)
# ==========================================
class BillingScreen(QMainWindow):
    def __init__(self):
        super(BillingScreen, self).__init__()
        if not UI_BILLING:
            QMessageBox.critical(self, "Fatal Error", "Billing UI file nahi mili!")
            sys.exit()
        uic.loadUi(UI_BILLING, self)
        self.cart_items = []
        if hasattr(self, 'lineEdit_5'):
            self.lineEdit_5.setText(str(random.randint(5000, 9999)))
            self.lineEdit_5.setReadOnly(True)
        for btn_name in ['pushButton', 'pushButton_6', 'pushButton_7']:
            if hasattr(self, btn_name): getattr(self, btn_name).clicked.connect(self.navigate_to_stock)
        if hasattr(self, 'pushButton_2'): self.pushButton_2.clicked.connect(self.flush_cart)
        if hasattr(self, 'pushButton_3'): self.pushButton_3.clicked.connect(self.close)
        if hasattr(self, 'pushButton_4'): self.pushButton_4.clicked.connect(self.add_item_logic)
        if hasattr(self, 'pushButton_8'): self.pushButton_8.clicked.connect(self.process_bill_generation)
        if hasattr(self, 'pushButton_9'): self.pushButton_9.clicked.connect(self.simulate_printer)
        if hasattr(self, 'lineEdit_14'): self.lineEdit_14.textChanged.connect(self.refresh_totals)

    def navigate_to_stock(self):
        self.stock_window = StockScreen(self)
        self.stock_window.show()
        self.hide()

    def add_item_logic(self):
        prod_title = self.lineEdit_7.text().strip() if hasattr(self, 'lineEdit_7') else ""
        qty_value = self.spinBox.value() if hasattr(self, 'spinBox') else 1
        try:
            unit_price = float(self.lineEdit_8.text().strip()) if hasattr(self, 'lineEdit_8') and self.lineEdit_8.text() else 0.0
        except ValueError:
            QMessageBox.warning(self, "Format Error", "Price field mein sirf number likhein!")
            return
        if not prod_title or unit_price <= 0:
            QMessageBox.warning(self, "Alert", "Item Name aur Price sahi se fill karein.")
            return
        computed_row_total = qty_value * unit_price
        self.cart_items.append({'sub': computed_row_total})
        if hasattr(self, 'label_23'): self.label_23.setText(prod_title)
        if hasattr(self, 'label_27'): self.label_27.setText(str(qty_value))
        if hasattr(self, 'label_31'): self.label_31.setText(f"{unit_price:.2f}")
        if hasattr(self, 'label_35'): self.label_35.setText(f"{computed_row_total:.2f}")
        self.refresh_totals()
        if hasattr(self, 'lineEdit_7'): self.lineEdit_7.clear()
        if hasattr(self, 'lineEdit_8'): self.lineEdit_8.clear()

    def refresh_totals(self):
        aggregated_sub = sum(node['sub'] for node in self.cart_items)
        try:
            deductible_discount = float(self.lineEdit_14.text().strip()) if hasattr(self, 'lineEdit_14') and self.lineEdit_14.text() else 0.0
        except ValueError:
            deductible_discount = 0.0
        net_grand_payable = max(0.0, aggregated_sub - deductible_discount)
        if hasattr(self, 'lineEdit_13'): self.lineEdit_13.setText(f"{aggregated_sub:.2f}")
        if hasattr(self, 'lineEdit_15'): self.lineEdit_15.setText(f"{net_grand_payable:.2f}")

    def flush_cart(self):
        self.cart_items.clear()
        for field in ['lineEdit_13', 'lineEdit_14', 'lineEdit_15']:
            if hasattr(self, field): getattr(self, field).setText("0.00")
        QMessageBox.information(self, "Cart", "Cart khali kar diya gaya hai.")

    def process_bill_generation(self):
        QMessageBox.information(self, "Success", "Bill kamyabi se generate ho gaya hai!")

    def simulate_printer(self):
        QMessageBox.information(self, "Printer", "Print command bhej di gayi hai.")

# ==========================================
# SCREEN 3: STOCK CONTROLLER (3 project)
# ==========================================
class StockScreen(QMainWindow):
    def __init__(self, billing_window=None):
        super(StockScreen, self).__init__()
        if not UI_STOCK:
            QMessageBox.critical(self, "Fatal Error", "Stock UI file nahi mili!")
            sys.exit()
        uic.loadUi(UI_STOCK, self)
        self.billing_window = billing_window

        # Aapke video ke mutabiq items map kiye hain
        self.stock_inventory = [
            {"id": "1", "name": "Rice", "qty": 50, "price": 60},
            {"id": "2", "name": "Sugar", "qty": 35, "price": 45},
            {"id": "3", "name": "Tea", "qty": 25, "price": 120},
            {"id": "4", "name": "Oil", "qty": 20, "price": 150},
            {"id": "5", "name": "Dal", "qty": 30, "price": 90}
        ]

        # Buttons ke text aur connections ko video ke mutabiq line kiya hai
        if hasattr(self, 'pushButton_5'): self.pushButton_5.clicked.connect(self.return_to_base_billing) # Back to Billing
        if hasattr(self, 'pushButton_3'): self.pushButton_3.clicked.connect(self.add_new_item_logic)       # Add New
        if hasattr(self, 'pushButton_4'): self.pushButton_4.clicked.connect(self.update_item_logic)    # Update Item
        if hasattr(self, 'pushButton_6'): self.pushButton_6.clicked.connect(self.delete_item_logic)    # Delete Item
        if hasattr(self, 'pushButton_2'): self.pushButton_2.clicked.connect(self.search_item_logic)    # Search Item
        if hasattr(self, 'pushButton_7'): self.pushButton_7.clicked.connect(self.clear_fields_logic)   # Clear Fields
        if hasattr(self, 'pushButton_8'): self.pushButton_8.clicked.connect(self.refresh_table_display) # Refresh
        if hasattr(self, 'pushButton_11'): self.pushButton_11.clicked.connect(self.refresh_table_display) # Scan Items

        self.refresh_table_display()

    def refresh_table_display(self):
        table = None
        for i in range(1, 15):
            if hasattr(self, f'tableWidget_{i}'):
                table = getattr(self, f'tableWidget_{i}')
                break
        if not table and hasattr(self, 'tableWidget'): table = self.tableWidget
        if not table: return

        table.setRowCount(0)
        total_items_count = len(self.stock_inventory)
        total_qty_sum = 0
        total_value_sum = 0

        for row_idx, data in enumerate(self.stock_inventory):
            table.insertRow(row_idx)
            table.setItem(row_idx, 0, QTableWidgetItem(str(data["id"])))
            table.setItem(row_idx, 1, QTableWidgetItem(str(data["name"])))
            table.setItem(row_idx, 2, QTableWidgetItem(str(data["qty"])))
            table.setItem(row_idx, 3, QTableWidgetItem(str(data["price"])))
            
            line_val = data["qty"] * data["price"]
            if table.columnCount() > 4:
                table.setItem(row_idx, 4, QTableWidgetItem(str(line_val)))
            
            total_qty_sum += data["qty"]
            total_value_sum += line_val

        # Bottom analytic fields update logic
        if hasattr(self, 'lineEdit_5'): self.lineEdit_5.setText(str(total_items_count))
        if hasattr(self, 'lineEdit_6'): self.lineEdit_6.setText(str(total_qty_sum))
        if hasattr(self, 'lineEdit_7'): self.lineEdit_7.setText(f"Rs. {total_value_sum}")

    def add_new_item_logic(self):
        i_id = self.lineEdit.text().strip() if hasattr(self, 'lineEdit') else ""
        i_name = self.lineEdit_2.text().strip() if hasattr(self, 'lineEdit_2') else ""
        i_qty = self.lineEdit_3.text().strip() if hasattr(self, 'lineEdit_3') else ""
        i_price = self.lineEdit_4.text().strip() if hasattr(self, 'lineEdit_4') else ""

        if not i_id or not i_name or not i_qty or not i_price:
            QMessageBox.warning(self, "Input Error", "Meharbani karke saari entry fields fill karein!")
            return

        try:
            for item in self.stock_inventory:
                if item["id"] == i_id:
                    QMessageBox.warning(self, "Duplicate Error", "Is ID ka item pehle se mojud hai!")
                    return
            self.stock_inventory.append({"id": i_id, "name": i_name, "qty": int(i_qty), "price": float(i_price)})
            self.refresh_table_display()
            self.clear_fields_logic()
            QMessageBox.information(self, "Success", f"Item '{i_name}' stock mein shamil ho gaya!")
        except ValueError:
            QMessageBox.critical(self, "Data Error", "Quantity aur Price mein sirf number likhein!")

    def update_item_logic(self):
        i_id = self.lineEdit.text().strip() if hasattr(self, 'lineEdit') else ""
        for item in self.stock_inventory:
            if item["id"] == i_id:
                try:
                    if hasattr(self, 'lineEdit_2'): item["name"] = self.lineEdit_2.text().strip()
                    if hasattr(self, 'lineEdit_3'): item["qty"] = int(self.lineEdit_3.text().strip())
                    if hasattr(self, 'lineEdit_4'): item["price"] = float(self.lineEdit_4.text().strip())
                    self.refresh_table_display()
                    QMessageBox.information(self, "Updated", "Item details kamyabi se badal di gayi hain!")
                    return
                except ValueError:
                    QMessageBox.critical(self, "Format Error", "Valid numeric formats write karein!")
                    return
        QMessageBox.warning(self, "Not Found", "Is ID ka koi item stock table mein nahi mila.")

    def delete_item_logic(self):
        i_id = self.lineEdit.text().strip() if hasattr(self, 'lineEdit') else ""
        for idx, item in enumerate(self.stock_inventory):
            if item["id"] == i_id:
                del self.stock_inventory[idx]
                self.refresh_table_display()
                self.clear_fields_logic()
                QMessageBox.information(self, "Deleted", "Item stock se remove ho gaya!")
                return
        QMessageBox.warning(self, "Error", "Ghalat Item ID!")

    def search_item_logic(self):
        search_edit = None
        for k in ['lineEdit_11', 'lineEdit_12', 'lineEdit_10', 'lineEdit_9', 'lineEdit_8']:
            if hasattr(self, k): 
                search_edit = getattr(self, k)
                break
        query = search_edit.text().strip().lower() if search_edit else ""
        if not query:
            # Fallback wrapper over video top header layouts
            for item in self.stock_inventory:
                if hasattr(self, 'lineEdit') and self.lineEdit.text().strip() == item["id"]:
                    query = item["name"].lower()
                    break
        if not query:
            QMessageBox.warning(self, "Query Blank", "Search field mein kuch likhein!")
            return
        for item in self.stock_inventory:
            if query in item["name"].lower() or query == item["id"]:
                if hasattr(self, 'lineEdit'): self.lineEdit.setText(item["id"])
                if hasattr(self, 'lineEdit_2'): self.lineEdit_2.setText(item["name"])
                if hasattr(self, 'lineEdit_3'): self.lineEdit_3.setText(str(item["qty"]))
                if hasattr(self, 'lineEdit_4'): self.lineEdit_4.setText(str(item["price"]))
                return
        QMessageBox.information(self, "Not Found", "Item stock directory mein nahi mila.")

    def clear_fields_logic(self):
        if hasattr(self, 'lineEdit'): self.lineEdit.clear()
        if hasattr(self, 'lineEdit_2'): self.lineEdit_2.clear()
        if hasattr(self, 'lineEdit_3'): self.lineEdit_3.clear()
        if hasattr(self, 'lineEdit_4'): self.lineEdit_4.clear()

    def return_to_base_billing(self):
        if self.billing_window: self.billing_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    root_execution_stream = LoginScreen()
    root_execution_stream.show()
    sys.exit(app.exec_())