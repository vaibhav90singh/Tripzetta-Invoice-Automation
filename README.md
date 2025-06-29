# Tripzetta Invoice Automation

A Python-based GUI tool that automates sending travel service invoices to customers through **WhatsApp** and **Email (Gmail)** using invoice details stored in a CSV file.

## 📌 Features

- 📤 Send dynamic **WhatsApp messages** with invoice summary using PyWhatKit
- 📧 Send detailed **HTML invoice emails** using Gmail SMTP
- 🧑‍💼 User-friendly **Tkinter GUI** to select customers and trigger messages
- 🧾 Uses structured invoice data from a central CSV (`invoices.csv`)
- 🏦 Includes banking and tax summary for GST-compliant invoicing
- 🧠 Built for **Tripzetta Travel Company**'s operational use

---

## 🖼 GUI Screenshots

- Customer selector
- WhatsApp number/email input
- "Send Invoice" button with real-time confirmation

> *(You can add screenshots here after pushing code)*

---

## 🛠 Technologies Used

| Tool         | Purpose                         |
|--------------|---------------------------------|
| Python       | Core language                   |
| Tkinter      | GUI development                 |
| Pandas       | CSV data parsing                |
| PyWhatKit    | Sending WhatsApp messages       |
| smtplib      | Sending HTML emails via Gmail   |
| MIMEText     | HTML email formatting           |

---

## 📂 Folder Structure

tripzetta-invoice-automation/
├── PYTHON_WHATSAPP.py # WhatsApp invoice sender app
├── PYTHON_GMAIL.py # Gmail invoice sender app
├── invoices.csv # Customer invoice data
├── PyWhatKit_DB.txt # WhatsApp send history (log)
├── README.md

---

## 🧪 How to Use

### 1. Clone the Repository

    git clone https://github.com/your-username/tripzetta-invoice-automation
    cd tripzetta-invoice-automation
    
2. Install Dependencies

        pip install pandas pywhatkit
   
4. Run the Apps
   
🟢 For WhatsApp Invoice Sender:

python PYTHON_WHATSAPP.py

🔵 For Gmail Invoice Sender:

python PYTHON_GMAIL.py

⚠️ Notes & Requirements

    WhatsApp messages require internet + desktop WhatsApp Web login

    Gmail requires an app password (enable 2-step verification in Google)

    Phone numbers must be in international format (+91...)

    Your CSV file should follow the format used in invoices.csv

✅ Sample Entry in invoices.csv
invoiceNo  	customer	    date	      value	    cgst	    sgst	  igst	place	  service	              sac	  taxType	  address	        gstin	            state	    amountWords
INV1006	    Meena Joshi	  2025-06-06	12000.0	  1080.0	  1080.0	0.0	  Delhi	  Shimla & Kufri Escape	9985	Intra	    Delhi Address	  07AABCD1234F1Z9	  Delhi	    Fourteen                                                                                                                                                                       Thousand

👨‍💻 Author

Vaibhav
API Automation Developer
[Tripzetta Travel Company]
📍 Nehru Place, Delhi

📄 License

MIT License

Copyright (c) 2025 Vaibhav
