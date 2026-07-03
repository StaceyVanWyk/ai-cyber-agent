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

# Brute Forece Detection function 
def brute_force_detection(log_content):

    failed_attempts = 0

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

                failed_attempts += 1
                break

    if failed_attempts >= 5:

        return {
            "detected": True,
            "attempts": failed_attempts,
            "risk": "HIGH"
        }

    elif failed_attempts >= 3:

        return {
            "detected": False,
            "attempts": failed_attempts,
            "risk": "MEDIUM"
        }

    else:

        return {
            "detected": False,
            "attempts": failed_attempts,
            "risk": "LOW"
        }
    
    