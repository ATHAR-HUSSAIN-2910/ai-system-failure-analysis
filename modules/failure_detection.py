def detect_failure(parsed_logs):
    """
    Detect the start and end of a system failure.
    """

    failure_start = None
    failure_end = None

    for log in parsed_logs:

        # Detect failure start
        if log["level"] == "ERROR" and failure_start is None:
            failure_start = log["timestamp"]

        # Detect recovery
        if "rollback completed" in log["message"].lower():
            failure_end = log["timestamp"]

    return failure_start, failure_end