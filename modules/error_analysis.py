from collections import Counter

def analyze_errors(parsed_logs):
    """
    Analyze error patterns from logs
    """

    error_messages = []

    for log in parsed_logs:
        if log["level"] == "ERROR":
            error_messages.append(log["message"])

    error_count = Counter(error_messages)

    total_errors = len(error_messages)

    return total_errors, error_count