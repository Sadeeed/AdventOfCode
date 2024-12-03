from utils import get_input

input = get_input("input.txt")


def check_safety(report):
    # report = list(map(int, report.split(" ")))
    # is_incremental = True
    is_incremental = report[1] > report[0]
    # # for idx, (num1, num2) in enumerate(zip(report[0::], report[1::])):
    for i in range(1, len(report)):
        # if idx == 0:
        #     if num1 > num2:
        #         is_incremental = False

        difference = report[i] - report[i-1]
        # if not (1 <= difference <= 3):
        #     return False

        # if is_incremental:
        #     if num1 > num2:
        #         return False
        # else:
        #     if num1 < num2:
        #         return False
            
        if not (1 <= abs(difference) <= 3):  
            return False
        elif (is_incremental and difference < 0) or (not is_incremental and difference > 0):
            return False 
    return True


safe_reports = 0
for report in input:
    report = list(map(int, report.split(" ")))
    is_safe = check_safety(report)
    print(f"Report: {report}")
    if is_safe:
        safe_reports += 1
        continue

    # report = report.split(" ")
    # for i in report:
    for i in range(len(report)):
        # dampened_report = report.copy()
        # dampened_report.remove(i)
        dampened_report = report[:i] + report[i+1:]
        is_safe = check_safety(dampened_report)
        if is_safe:
            safe_reports += 1
            break

print(f"Safe reports: {safe_reports}")
