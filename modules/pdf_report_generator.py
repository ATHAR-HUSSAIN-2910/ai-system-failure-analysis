from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(failure_start, failure_end, downtime, total_errors, error_counts, root_cause):

    pdf_path = "output/reports/system_failure_report.pdf"

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI-Based System Failure Analysis Report", styles['Title']))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Failure Start Time: {failure_start}", styles['Normal']))
    elements.append(Paragraph(f"Failure End Time: {failure_end}", styles['Normal']))
    elements.append(Paragraph(f"Total Downtime: {downtime}", styles['Normal']))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Total Errors: {total_errors}", styles['Normal']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Error Frequency:", styles['Heading2']))

    for error, count in error_counts.items():
        elements.append(Paragraph(f"{error} : {count}", styles['Normal']))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Predicted Root Cause: {root_cause}", styles['Heading2']))
    elements.append(Spacer(1, 30))

    elements.append(Paragraph("Charts", styles['Heading2']))
    elements.append(Spacer(1, 10))

    elements.append(Image("output/charts/error_frequency_chart.png", width=400, height=250))
    elements.append(Spacer(1, 20))

    elements.append(Image("output/charts/log_level_distribution.png", width=400, height=250))
    elements.append(Spacer(1, 20))

    elements.append(Image("output/charts/error_timeline.png", width=400, height=250))

    pdf = SimpleDocTemplate(pdf_path)
    pdf.build(elements)