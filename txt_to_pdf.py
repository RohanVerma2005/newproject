from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

def text_to_pdf(input_path, output_path):
    # Set up the PDF document
    doc = SimpleDocTemplate(output_path, pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)

    # Define styles
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    heading_style = ParagraphStyle(
        name="HeadingCenter",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        spaceAfter=12
    )

    story = []

    # Read lines from file
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    paragraph_buffer = ""
    first_line = True

    for line in lines:
        stripped = line.strip()

        if first_line and stripped != "":
            # First non-empty line is heading
            story.append(Paragraph(stripped, heading_style))
            story.append(Spacer(1, 0.2 * inch))
            first_line = False
        elif stripped == "":
            if paragraph_buffer:
                story.append(Paragraph(paragraph_buffer.strip(), normal_style))
                story.append(Spacer(1, 0.15 * inch))
                paragraph_buffer = ""
        else:
            paragraph_buffer += line.rstrip() + " "

    # Add final paragraph if needed
    if paragraph_buffer.strip():
        story.append(Paragraph(paragraph_buffer.strip(), normal_style))

    # Build the final PDF
    doc.build(story)

# Usage

index_chapter = 0

while index_chapter<232:
    text_to_pdf(f"E:\\Z\\chapter_text_files\\chapter_{index_chapter}.txt",f"E:\\Z\\chapter_pdf_files\\chapter_{index_chapter}.pdf")
    print(f"Created the chapter_{index_chapter}.pdf")
    index_chapter+=1
