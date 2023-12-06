def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines]
    return lines


def parse_input(lines):
    data = {}
    for line in lines:
        key, value = line.split(':')
        data[key] = [int(x) for x in value.split()]
    return data


def get_winning_distances(data):
    distances = {}
    for index, time in enumerate(data['Time']):
        record_distance = data['Distance'][index]
        winning_distances = []
        for i in range(time):
            new_distance = (time - i) * i
            if new_distance > record_distance:
                winning_distances.append(new_distance)
        distances[time] = winning_distances
    return distances


def parse_with_kerning(lines):
    data = {}
    for line in lines:
        key, value = line.split(':')
        data[key] = [int(value.replace(" ", ""))]
    return data
