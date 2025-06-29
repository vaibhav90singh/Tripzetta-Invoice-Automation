import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText

# === Load CSV ===
df = pd.read_csv('invoices.csv')

# === Gmail Configuration ===
sender_email = "sociolabs0321@gmail.com"
app_password = "zswr pftj dfmc dgea"

# === Function to Send Email ===
def send_email():
    customer_name = selected_customer.get()
    receiver_email = email_entry.get().strip()

    if not customer_name or not receiver_email:
        messagebox.showerror("Input Error", "Please select customer and enter recipient's email.")
        return

    try:
        row = df[df['customer'] == customer_name].iloc[0]
    except IndexError:
        messagebox.showerror("Error", "Customer not found in CSV.")
        return

    # === Compose Dynamic HTML ===
    invoice_html = f"""
    <html><body style="font-family: Arial; color: #333;">
    <p>Dear <strong> {row['customer']}</strong>,</p><br>
    <p>Please find below the details of your invoice from <strong>Tripzetta</strong>:</p><br><br>

    <h3>🧾 Invoice Summary:</h3>
    <table border="1" cellpadding="8" style="border-collapse: collapse; width:100%">
        <tr><td><strong>Invoice Date</strong></td><td>{row['date']}</td></tr>
        <tr><td><strong>Invoice No</strong></td><td>{row['invoiceNo']}</td></tr>
        <tr><td><strong>Place of Supply</strong></td><td>{row['place']}</td></tr>
        <tr><td><strong>Name</strong></td><td>{row['customer']}</td></tr>
        <tr><td><strong>Address</strong></td><td>{row['address']}</td></tr>
        <tr><td><strong>GSTIN (Customer)</strong></td><td>{row['gstin']}</td></tr>
        <tr><td><strong>State</strong></td><td>{row['state']}</td></tr>
        <tr><td><strong>GSTIN (Company)</strong></td><td>07APDPA8620A1ZL</td></tr>
        <tr><td><strong>PAN</strong></td><td>APDPA8620A</td></tr>
        <tr><td><strong>Registered Address</strong></td><td>408, Devika Tower, Nehru Place, New Delhi</td></tr>
        <tr><td><strong>Contact</strong></td><td>+91 9650485130</td></tr>
    </table><br><br>

    <h3>🛎️ Service Details:</h3>
    <table border="1" cellpadding="8" style="border-collapse: collapse; width:100%">
        <tr>
            <th>S.No</th><th>Service Description</th><th>SAC Code</th><th>Tax Type</th>
            <th>Taxable Value</th><th>SGST%</th><th>SGST Amt</th>
            <th>CGST%</th><th>CGST Amt</th><th>IGST%</th><th>IGST Amt</th><th>Total</th>
        </tr>
        <tr>
            <td>1</td><td>{row['service']}</td><td>{row['sac']}</td><td>{row['taxType']}</td>
            <td>{row['value']}</td><td>9%</td><td>{row['sgst']}</td>
            <td>9%</td><td>{row['cgst']}</td><td>18%</td><td>{row['igst']}</td>
            <td>{float(row['value']) + float(row['igst']) + float(row['cgst']) + float(row['sgst'])}</td>
        </tr>
    </table><br><br>

    <h3>🏦 Bank Details:</h3>
    <table border="1" cellpadding="8" style="border-collapse: collapse; width:100%">
        <tr><td><strong>Beneficiary</strong></td><td>TRIPZETTA</td></tr>
        <tr><td><strong>Bank</strong></td><td>YES BANK</td></tr>
        <tr><td><strong>Branch</strong></td><td>East of Kailash, Delhi</td></tr>
        <tr><td><strong>IFSC</strong></td><td>YESB0000514</td></tr>
        <tr><td><strong>Account No</strong></td><td>051463700000043</td></tr>
    </table><br><br>

    <h3>💰 Invoice Total:</h3>
    <table border="1" cellpadding="8" style="border-collapse: collapse; width:100%">
        <tr><td><strong>Total Before Tax</strong></td><td>₹{row['value']}</td></tr>
        <tr><td><strong>SGST @ 9%</strong></td><td>₹{row['sgst']}</td></tr>
        <tr><td><strong>CGST @ 9%</strong></td><td>₹{row['cgst']}</td></tr>
        <tr><td><strong>IGST @ 18%</strong></td><td>₹{row['igst']}</td></tr>
        <tr><td><strong>Total Invoice Value</strong></td><td><strong>₹{float(row['value']) + float(row['igst']) + float(row['cgst']) + float(row['sgst'])}</strong></td></tr>
        <tr><td><strong>In Words</strong></td><td>{row['amountWords']}</td></tr>
    </table><br>

    <p>Thank you for choosing Tripzetta!<br><br>Warm regards,<br><strong>Tripzetta</strong></p>
    </body></html>
    """

    # === Prepare and Send Email ===
    msg = MIMEText(invoice_html, "html")
    msg["Subject"] = f"{row['customer']} - Tripzetta Invoice – {row['invoiceNo']}"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        messagebox.showinfo("Success", f"Invoice sent to {receiver_email}")
    except Exception as e:
        messagebox.showerror("Email Failed", str(e))

# === GUI Setup ===
root = tk.Tk()
root.title("Tripzetta Invoice Email Sender")
root.geometry("500x250")

tk.Label(root, text="Select Customer:", font=("Arial", 12)).pack(pady=5)
selected_customer = tk.StringVar()
customer_dropdown = ttk.Combobox(root, textvariable=selected_customer, font=("Arial", 12))
customer_dropdown['values'] = df['customer'].unique().tolist()
customer_dropdown.pack(pady=5)

tk.Label(root, text="Enter Recipient Email:", font=("Arial", 12)).pack(pady=5)
email_entry = tk.Entry(root, font=("Arial", 12))
email_entry.pack(pady=5)

tk.Button(root, text="Send Invoice Email", command=send_email, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)

root.mainloop()
