def analyze_logs(log_content):

    findings = []

    failed_keywords = [
        "failed",
        "invalid password",
        "authentication failed",
        "login failed"
    ]

    lines = log_content.split("\n")

    for line in lines:

        for keyword in failed_keywords:

            if keyword.lower() in line.lower():

                findings.append(
                    f"Failed Login Detected: {line}"
                )

    return findings