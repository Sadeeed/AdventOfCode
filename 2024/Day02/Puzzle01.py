from utils import get_input

input = get_input('input.txt')

def check_safety(report):
    report = report.split(" ")
    # print("\n*******\n")
    for i in range(len(report)):
        # print(report[i])
        if i+1 < len(report):
            difference = abs(int(report[i]) - int(report[i+1]))
            if difference > 3 or difference < 1:
                print(f"Report is not safe: {report[i]} - {report[i+1]} = {difference}")
                return False
    # print("\n*******\n")
    # print(f"Report is safe: {report}")
    return True

def is_monotonic(report):
    report = list(map(int, report.split(" ")))
    return all(report[i] <= report[i+1] for i in range(len(report)-1)) or all(report[i] >= report[i+1] for i in range(len(report)-1))
        
safe_reports = 0
for report in input:
    is_safe = check_safety(report)
    monotonic = is_monotonic(report)
    print(f"Is safe: {is_safe}")
    print(f"Is monotonic: {monotonic}\n")
    if is_safe and monotonic:
        safe_reports += 1

print(f"Safe reports: {safe_reports}")
