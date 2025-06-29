import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import pywhatkit as kit
from datetime import datetime
import time

# Load CSV data
df = pd.read_csv('invoices.csv')

# GUI App
def send_invoice():
    customer_name = selected_customer.get()
    if not customer_name:
        messagebox.showerror("Error", "Please select a customer.")
        return

    # Filter row based on customer
    row = df[df['customer'] == customer_name].iloc[0]

    # Extract details
    invoice_message = f"""
🧾 *Tripzetta Invoice – {row['invoiceNo']}*

👤 *Client:*          Mr. {row['customer']}
📅 *Invoice Date:*    {row['date']}
🌐 *Place of Supply:* {row['place']}
🏷 *Service:*         {row['service']}
💰 *Amount:*          ₹{float(row['value']):,.2f}
🧾 *CGST @(%):*       ₹{float(row['cgst']):,.2f}
🧾 *SGST @(%):*       ₹{float(row['sgst']):,.2f}
🧾 *IGST @(%):*       ₹{float(row['igst']):,.2f}
💵 *Total:*           ₹{float(row['value']) + float(row['cgst']) + float(row['sgst']) + float(row['igst']):,.2f}

🏦 *Bank Details:*
TRIPZETTA –  YES BANK
A/C No:      051463700000043
IFSC:        YESB0000514
Branch:      East of Kailash, Delhi

📞 Contact: Tripzetta
"""

    number = phone_entry.get().strip()
    if not number.startswith("+"):
        messagebox.showerror("Invalid Number", "Use international format like +91...")
        return

    # Get current time and schedule 1 minute later
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 1

    try:
        kit.sendwhatmsg(number, invoice_message, hour, minute)
        messagebox.showinfo("Success", f"Invoice sent to {number}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI window
root = tk.Tk()
root.title("Tripzetta WhatsApp Invoice Sender")
root.geometry("500x250")

tk.Label(root, text="Select Customer:", font=("Arial", 12)).pack(pady=5)

# Dropdown for customers
selected_customer = tk.StringVar()
customer_dropdown = ttk.Combobox(root, textvariable=selected_customer, font=("Arial", 12))
customer_dropdown['values'] = df['customer'].unique().tolist()
customer_dropdown.pack(pady=5)

tk.Label(root, text="Enter WhatsApp Number (+91...):", font=("Arial", 12)).pack(pady=5)
phone_entry = tk.Entry(root, font=("Arial", 12))
phone_entry.pack(pady=5)

tk.Button(root, text="Send WhatsApp Invoice", command=send_invoice, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

root.mainloop()
