from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add the image (change filename if needed)
pdf.image("/home/kali/Downloads/Untitled.jpeg", x=10, y=10, w=190)

# Add space after image
pdf.ln(110)

# Add text
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Dear User,

This is an important document. Please read carefully and click the link below to view additional content.
""")

# Add clickable link to your track.html
pdf.ln(10)
pdf.set_text_color(0, 0, 255)
pdf.set_font("Arial", 'U', 12)
pdf.cell(200, 10, txt="Click here to view additional content", ln=True, link="http://137.59.231.46:5000/track.html")

pdf.output("legitimate_document.pdf")
print("✅ PDF created: legitimate_document.pdf")
