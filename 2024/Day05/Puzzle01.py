from utils import get_input

input = get_input('input.txt')

def parse_input(input):
    idx = input.index('')
    rules = [list(map(int, rule.split('|'))) for rule in input[:idx]]
    pages = [list(map(int, page.split(','))) for page in input[idx+1:]]
    return rules, pages

rules, pages = parse_input(input)

print(f"Rules: {rules}\n**********")
print(f"Pages: {pages}\n**********")

def check_rule(rules, page):
    for idx, num in enumerate(page):
        for rule in rules:
            if idx==0:
                if num == rule[1] and rule[0] in page:
                    return False
            if num == rule[0] and rule[1] in page:
                r1_idx = page.index(rule[1])
                if r1_idx < idx:
                    return False
    return True

def get_mean(page):
    return page[(len(page)//2)]

total_mean = 0
for page in pages:
    is_correct = check_rule(rules, page)
    if is_correct:
        print(f"Page: {page} is correct")
        total_mean += get_mean(page)
    else:
        print(f"Page: {page} is incorrect")

print(f"Total Mean: {total_mean}")