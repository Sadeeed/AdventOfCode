def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines]
    return lines


def parse_cards(lines):
    scores = []
    matches = {}
    for line in lines:
        card_id, card_data = line.replace("Card ", "").split(":")
        card_data = card_data.split("|")
        card_data = [data.strip().split(" ") for data in card_data]
        winning_numbers, our_numbers = card_data
        score = 0
        winning_numbers = [int(number) for number in winning_numbers if number != '']
        our_numbers = [int(number) for number in our_numbers if number != '']
        match = 0
        for number in our_numbers:
            if number in winning_numbers:
                match += 1
                if score == 0:
                    score = 1
                else:
                    score *= 2
        scores.append(score)
        matches[int(card_id)] = {"match": match, "total": 1}
        print(f"Card ID: {card_id} | Score: {score}")
    print('\n')
    return scores, matches


def process_matches(matches):
    total = 0
    for key, value in matches.items():
        for i in range(value["match"]):
            matches[key + i + 1]["total"] += matches[key]["total"]
        print(f"Card ID: {key} | Match: {value['match']} | Total: {value['total']}")
        total += value["total"]
    return total
