from typing import List

def main(reports):
    is_safe_count = 0

    for report in reports:
        is_safe = is_report_safe(report)
        if is_safe:
            is_safe_count+=1


    return is_safe_count

def is_report_safe(report: List[int]) -> bool:
    is_ascending = None

    for i, level in enumerate(report):
        if i == 0:
            continue
        
        difference = abs(level - report[i-1])

        if difference > 3 or difference < 1:
            return False
        
        if is_ascending == None:
            is_ascending = True if level > report[i-1] else False
            continue
        elif is_ascending != (level > report[i-1]):
            return False 
            
    return True


if __name__ == '__main__':
    reports = []
    with open('./input/input.txt', 'r') as f:
    # with open('./input/test_input.txt', 'r') as f:
        for line in f:
            report = [int(x) for x in line.removesuffix('\n').split(' ')]
            reports.append(report)

    safe_count = main(reports)
    print('safe_count', safe_count)