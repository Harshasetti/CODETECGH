import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Set absolute paths
csv_path = r"C:\Users\pabbi\Desktop\Projects\data.csv"
pdf_path = r"C:\Users\pabbi\Downloads\Sales_Report.pdf"
chart_path = r"C:\Users\pabbi\Downloads\sales_chart.png"

# Check if data.csv exists
if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found! Please check the file location.")
    exit()

print("Reading data.csv...")
data = pd.read_csv(csv_path)
print("Data read successfully!")

# Analyze data
print("Analyzing data...")
total_sales = data["Sales"].sum()
average_sales = data["Sales"].mean()
best_employee = data.loc[data["Sales"].idxmax(), "Employee"]
print(f"Analysis complete! Total Sales: {total_sales}, Best Employee: {best_employee}")

# Generate a Sales Chart
print("Generating sales chart...")
plt.figure(figsize=(6, 4))
plt.bar(data["Employee"], data["Sales"], color='blue')
plt.xlabel("Employee")
plt.ylabel("Sales ($)")
plt.title("Sales Performance")
plt.savefig(chart_path)
plt.close()
print(f"Sales chart saved as {chart_path}!")

# Generate PDF Report
print("Generating PDF report...")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Automated Sales Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, f"Total Sales: ${total_sales}", ln=True)
pdf.cell(0, 10, f"Average Sales: ${average_sales:.2f}", ln=True)
pdf.cell(0, 10, f"Best Employee: {best_employee}", ln=True)
pdf.ln(10)

# Check if sales chart exists before adding
if os.path.exists(chart_path):
    pdf.image(chart_path, x=10, y=None, w=180)
else:
    print("Warning: Sales chart not found, skipping image!")

pdf.output(pdf_path)

# Check if PDF was created
if os.path.exists(pdf_path):
    print(f"Report successfully generated as {pdf_path}!")
    os.startfile(pdf_path)  # Open automatically on Windows
else:
    print("Error: PDF report was NOT generated!")
