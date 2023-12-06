def get_input(filename):
    with open(filename) as f:
        lines = f.read()
        f.close()
    return lines


def parse_input(lines):
    data = {}
    key = None
    for line in lines.split('\n'):
        if ':' in line:
            key, _ = line.split(':')
            data[key] = {} if key != 'seeds' else list(map(int, _.split()))
        elif line:
            if key == 'seeds':
                values = convert_to_map(list(map(int, line.split())), data['seeds'])
            else:
                values = convert_to_map(list(map(int, line.split())), None)
            data[key].update(values)
    return data


def convert_to_map(values, seeds):
    destination_start = values[0]
    source_start = values[1]
    range_length = values[2]
    mapped_data = {src: dst for src, dst in zip(range(source_start, source_start + range_length),
                                                range(destination_start, destination_start + range_length))}
    if seeds:
        mapped_data = {src: dst for src, dst in zip(range(source_start, source_start + range_length),
                                                    range(destination_start, destination_start + range_length)) if src in seeds}
    return mapped_data


def get_seed_data(data):
    seeds = data['seeds']
    seed_data = {}
    for seed in seeds:
        if seed in data['seed-to-soil map'].keys():
            soil = data['seed-to-soil map'][seed]
        else:
            soil = seed
        if soil in data['soil-to-fertilizer map'].keys():
            fertilizer = data['soil-to-fertilizer map'][soil]
        else:
            fertilizer = soil
        if fertilizer in data['fertilizer-to-water map'].keys():
            water = data['fertilizer-to-water map'][fertilizer]
        else:
            water = fertilizer
        if water in data['water-to-light map'].keys():
            light = data['water-to-light map'][water]
        else:
            light = water
        if light in data['light-to-temperature map'].keys():
            temperature = data['light-to-temperature map'][light]
        else:
            temperature = light
        if temperature in data['temperature-to-humidity map'].keys():
            humidity = data['temperature-to-humidity map'][temperature]
        else:
            humidity = temperature
        if humidity in data['humidity-to-location map'].keys():
            location = data['humidity-to-location map'][humidity]
        else:
            location = humidity

        seed_data[seed] = {'soil': soil, 'fertilizer': fertilizer, 'water': water, 'light': light,
                           'temperature': temperature, 'humidity': humidity, 'location': location}

    return seed_data


def expand_seeds(seeds):
    expanded_seeds = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i + 1]
        expanded_seeds.extend(range(start, start + length))
    return expanded_seeds
