import re
import csv
import os
from PyPDF2 import PdfReader

# ---------- STEP 1: Extract Text from PDF ----------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


# ---------- STEP 2: Extract Invoice Data from Text ----------
def extract_invoice_data(text):
    data = {}

    # Each field is assumed to be on the same line (after the colon)
    patterns = {
        "PO Number": r"PO Number\s*:\s*(\S+)",
        "Due Date": r"Due Date\s*:\s*(.+)",
        "Bill To": r"Bill To\s*:\s*(.+)",
        "Ship To": r"Ship To\s*:\s*(.+)",
        "Total": r"Total\s*:\s*\$?([\d,]+\.\d{2})",
        "Balance Due": r"Balance Due\s*:\s*\$?([\d,]+\.\d{2})"
    }

    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        data[field] = match.group(1).strip() if match else "Not Found"

    return data


# ---------- STEP 3: Save Extracted Data to CSV ----------
def save_to_csv(data, filename="extracted_invoices.csv"):
    fieldnames = list(data.keys())

    # Check if file exists to write header only once
    file_exists = os.path.exists(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
        print(f"✅ Data saved to {filename}")


# ---------- MAIN EXECUTION ----------
if __name__ == "__main__":
    pdf_path = "data/invoices/invoice.pdf"  # update path if needed

    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
    else:
        print("🔍 Extracting text...")
        raw_text = extract_text_from_pdf(pdf_path)

        print("📦 Extracting invoice fields...")
        extracted_data = extract_invoice_data(raw_text)
        print("📄 Extracted Invoice Data:")
        for k, v in extracted_data.items():
            print(f"{k}: {v}")

        save_to_csv(extracted_data)
