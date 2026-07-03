def analyze_logs(log_content):

    findings = []

    failed_keywords = [
        "authentication failed",
        "invalid password",
        "login failed",
        "failed"
    ]

    lines = log_content.split("\n")

    for line in lines:

        for keyword in failed_keywords:

            if keyword.lower() in line.lower():

                findings.append(
                    f"🚨 Failed Login Detected: {line}"
                )

                break

    return findings