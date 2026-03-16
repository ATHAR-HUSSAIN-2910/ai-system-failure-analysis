from modules.log_input import load_logs
from modules.failure_detection import detect_failure
from modules.downtime_calculator import calculate_downtime
from modules.error_analysis import analyze_errors
from modules.root_cause_analysis import detect_root_cause
from modules.report_generator import generate_report
from modules.charts import plot_error_frequency, plot_log_levels, plot_error_timeline
from modules.pdf_report_generator import generate_pdf_report


# Load logs
logs = load_logs("logs/cloud_logs.json")
print("Logs parsed successfully!\n")

for log in logs:
    print(log)


# Failure Detection
print("\n------ Failure Analysis ------")

failure_start, failure_end = detect_failure(logs)

print("Failure Start Time:", failure_start)
print("Failure End Time:", failure_end)


# Downtime Calculation
print("\n------ Downtime Report ------")

downtime = calculate_downtime(failure_start, failure_end)

print("Total Downtime:", downtime)


# Error Pattern Analysis
print("\n------ Error Pattern Analysis ------")

error_counts = {}
total_errors = 0

for log in logs:
    if log["level"] == "ERROR":
        message = log["message"]
        error_counts[message] = error_counts.get(message, 0) + 1
        total_errors += 1

print("Total Errors:", total_errors)

print("\nError Frequency:")
for error, count in error_counts.items():
    print(f"{error} → {count}")


# Root Cause Detection
print("\n------ Root Cause Detection ------")

root_cause = detect_root_cause(error_counts)

print("Predicted Root Cause:", root_cause)


# Generate Report
print("\n------ Report Generated ------")

generate_report(
    failure_start,
    failure_end,
    downtime,
    total_errors,
    error_counts,
    root_cause
)

print("Report saved to: output/reports/system_failure_report.txt")


# Generate Charts
plot_error_frequency(error_counts)
plot_log_levels(logs)
plot_error_timeline(logs)

generate_pdf_report(
    failure_start,
    failure_end,
    downtime,
    total_errors,
    error_counts,
    root_cause
)