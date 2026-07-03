from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer

)

from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
        filename,
        threath_count,
        risk_level,
        findings,
        brute_force

        
):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CyberGaurd AI Incident Report",
            styles["Title"]

        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Threats Detected: {threath_count}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {risk_level}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(  
            
            "Findings:",
            styles["Heading2"]
        ))
    
    for finding in findings:

        content.append(
            Paragraph(
                finding,
                styles["Normal"]
            )
        )
    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Brute Force Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Detected: {brute_force['detected']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Attempts: {brute_force['attempts']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk: {brute_force['risk']}",
            styles["Normal"]
        )
    )

    doc.build(content)