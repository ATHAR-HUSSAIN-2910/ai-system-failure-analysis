from datetime import datetime


def parse_logs(logs):
    """
    Convert timestamp strings into datetime objects
    for easier time-based analysis.
    """

    parsed_logs = []

    for log in logs:

        # Convert timestamp string into datetime object
        timestamp = datetime.strptime(log["timestamp"], "%Y-%m-%dT%H:%M:%SZ")

        parsed_log = {
            "timestamp": timestamp,
            "level": log["level"],
            "message": log["message"]
        }

        parsed_logs.append(parsed_log)

    return parsed_logs