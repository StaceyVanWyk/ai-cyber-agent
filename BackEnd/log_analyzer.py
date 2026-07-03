def analyze_logs(log_content):

    findings = []
    seen_lines = set()

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

                if line not in seen_lines:

                    findings.append(
                        f"🚨 Failed Login Detected: {line}"
                    )

                    seen_lines.add(line)

                break

    return findings