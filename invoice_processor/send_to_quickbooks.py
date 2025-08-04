import requests

invoice_data = {
    "PO Number": "123456",
    "Due Date": "Aug 15, 2025",
    "Bill To": "Safeer Hussain",
    "Ship To": "Rahim Yar Khan",
    "Total": "$1500.00",
    "Balance Due": "$1500.00"
}

url = 'http://localhost:5001/invoices'

try:
    response = requests.post(url, json=invoice_data)
    if response.status_code == 201:
        print("✅ Invoice sent successfully to QuickBooks API!")
        print(response.json())
    else:
        print("❌ Failed to send invoice:", response.text)
except Exception as e:
    print("🚨 Error connecting to API:", e)
