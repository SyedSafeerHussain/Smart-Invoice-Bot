from invoice_processor.pdf_extractor import extract_invoice_data
import os
if __name__=="__main__":
    invoice_folder="data/invoices"
    for file_name in os.listdir(invoice_folder):
        if file_name.endswith(".pdf"):
            print(f"\nprocessing:{file_name}")
            file_path=os.path.join(invoice_folder,file_name)
            data=extract_invoice_data(file_path)
            print("Extracted data:")
            for k,v in data.items():
                print(f"{k}:{v}")