import matplotlib.pyplot as plt


def plot_error_frequency(error_counts):

    errors = list(error_counts.keys())
    counts = list(error_counts.values())

    plt.figure()

    plt.bar(errors, counts)

    plt.title("Error Frequency Analysis")
    plt.xlabel("Error Type")
    plt.ylabel("Occurrences")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("output/charts/error_frequency_chart.png")

    plt.show()



def plot_log_levels(logs):

    level_counts = {}

    for log in logs:
        level = log["level"]
        level_counts[level] = level_counts.get(level, 0) + 1

    labels = list(level_counts.keys())
    values = list(level_counts.values())

    plt.figure()

    plt.pie(values, labels=labels, autopct='%1.1f%%')

    plt.title("Log Level Distribution")

    plt.savefig("output/charts/log_level_distribution.png")

    plt.show()



def plot_error_timeline(logs):

    error_times = []

    for log in logs:
        if log["level"] == "ERROR":
            error_times.append(log["timestamp"])

    y = [1] * len(error_times)

    plt.figure()

    plt.scatter(error_times, y)

    plt.title("Failure Timeline")
    plt.xlabel("Time")

    plt.yticks([])

    plt.tight_layout()

    plt.savefig("output/charts/error_timeline.png")

    plt.show()