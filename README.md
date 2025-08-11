# 🚀 SmartInvoiceBot

**Automate PDF Invoice Data Extraction — Simplify Your Workflow**

---

### ✨ Overview  
SmartInvoiceBot is a lightweight Python tool that extracts important information from PDF invoices, helping you save time and reduce manual data entry errors.

---

### 🔍 Features  
- Extract key details: Invoice number, date, vendor, amounts  
- Batch process multiple PDFs effortlessly  
- Export data to CSV or JSON formats  
- Easy-to-customize for your specific invoice formats

---

### ⚙️ Installation

git clone https://github.com/yourusername/SmartInvoiceBot.git  
cd SmartInvoiceBot  

python3 -m venv venv  
source venv/bin/activate   # Windows: venv\Scripts\activate  

pip install -r requirements.txt

---

### 🚀 Usage

1. Place your PDF invoices in the `invoices/` folder  
2. Run the script:  
python main.py  
3. Find extracted data in the `output/` folder

---

### 🛠 Configuration  
- Customize parsing logic in `parser.py`  
- Modify input/output paths in `config.py`  

---

### 📦 Dependencies  
- Python 3.6+  
- PyPDF2  
- pandas (for CSV handling)

---

### 🤝 Contributions  
Contributions are welcome! Please open an issue or submit a pull request.

---

### 📄 License  
[MIT License](LICENSE)

---

Made with ❤️ by Safeer Hussain
