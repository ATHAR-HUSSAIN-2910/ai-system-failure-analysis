from datetime import datetime


def calculate_downtime(start, end):

    start_time = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
    end_time = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")

    downtime = end_time - start_time

    return downtime