def generate_report(failure_start, failure_end, downtime, total_errors, error_count, root_cause):

    report = "\n===== SYSTEM FAILURE REPORT =====\n\n"

    report += f"Failure Start Time: {failure_start}\n"
    report += f"Failure End Time: {failure_end}\n"
    report += f"Total Downtime: {downtime}\n\n"

    report += f"Total Errors: {total_errors}\n\n"

    report += "Error Summary:\n"

    for error, count in error_count.items():
        report += f"- {error} ({count})\n"

    report += "\nPredicted Root Cause:\n"
    report += f"{root_cause}\n"

    file_path = "output/reports/system_failure_report.txt"

    with open(file_path, "w") as file:
        file.write(report)

    return report