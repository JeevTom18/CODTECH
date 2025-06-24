import pandas as pd
from fpdf import FPDF

# Load the data
df = pd.read_csv("scores.csv")

# Basic analysis
avg_score = df["Score"].mean()
max_score = df["Score"].max()
min_score = df["Score"].min()
topper = df.loc[df["Score"].idxmax()]["Name"]

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Student Performance Report", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, f"Average Score: {avg_score:.2f}", ln=True)
pdf.cell(200, 10, f"Highest Score: {max_score}", ln=True)
pdf.cell(200, 10, f"Lowest Score: {min_score}", ln=True)
pdf.cell(200, 10, f"Top Performer: {topper}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Full Score List", ln=True)

pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(200, 10, f"{row['Name']} - {row['Subject']} - {row['Score']}", ln=True)

# Save the report
pdf.output("student_report.pdf")
print("PDF report generated successfully.")
