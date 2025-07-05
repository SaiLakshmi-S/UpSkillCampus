import datetime
import os

class Invoice:
    def __init__(self, client_name, service_description, rate_per_hour, hours_worked, tax_percent=18):
        self.client_name = client_name
        self.service_description = service_description
        self.rate_per_hour = float(rate_per_hour)
        self.hours_worked = float(hours_worked)
        self.tax_percent = tax_percent
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.invoice_number = f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    def calculate_total(self):
        subtotal = self.rate_per_hour * self.hours_worked
        tax = subtotal * (self.tax_percent / 100)
        total = subtotal + tax
        return subtotal, tax, total

    def generate_invoice_text(self):
        subtotal, tax, total = self.calculate_total()
        return f"""
        -------------------------------------------
                    FREELANCE INVOICE
        -------------------------------------------
        Invoice Number: {self.invoice_number}
        Date: {self.date}

        Client Name: {self.client_name}
        Service Description: {self.service_description}

        Rate per Hour: ₹{self.rate_per_hour}
        Hours Worked: {self.hours_worked}
        Subtotal: ₹{subtotal:.2f}
        Tax ({self.tax_percent}%): ₹{tax:.2f}
        -------------------------------------------
        Total Amount Due: ₹{total:.2f}
        -------------------------------------------
        Thank you for your business!
        """

    def save_to_file(self):
        filename = f"Invoice_{self.invoice_number}.txt"
        with open(filename, 'w') as f:
            f.write(self.generate_invoice_text())
        print(f"\nInvoice saved as {filename}")

# --- MAIN PROGRAM ---

def main():
    print("------ FREELANCER INVOICE GENERATOR ------")
    client = input("Client Name: ")
    service = input("Service Description: ")
    rate = input("Rate per Hour (₹): ")
    hours = input("Hours Worked: ")

    try:
        invoice = Invoice(client, service, rate, hours)
        print(invoice.generate_invoice_text())
        invoice.save_to_file()
    except ValueError:
        print("Invalid input! Please enter numeric values for rate and hours.")

if __name__ == "__main__":
    main()
