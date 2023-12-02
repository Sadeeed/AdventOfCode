def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
    return lines


def parse_game(line):
    line = line.replace("\n", "")
    line = line.replace("Game ", "")
    game_id, cube_sets = line.split(": ")
    cube_sets = cube_sets.split("; ")
    red_max = 0
    green_max = 0
    blue_max = 0

    for cube_set in cube_sets:
        cube_set = cube_set.split(", ")
        for cube in cube_set:
            cube.replace("\n", "")
            cube = cube.split(" ")
            if 'red' in cube:
                red_max = max(red_max, int(cube[0]))
            elif 'green' in cube:
                green_max = max(green_max, int(cube[0]))
            elif 'blue' in cube:
                blue_max = max(blue_max, int(cube[0]))
    game = [int(game_id), red_max, green_max, blue_max]
    return game


def get_possible_games(games, red, green, blue):
    possible_games = []
    for game in games:
        if red >= game[1] and green >= game[2] and blue >= game[3]:
            possible_games.append(game[0])
    return possible_games


def sum_of_powers(games):
    powers = []
    for game in games:
        print("Game:", game)
        game_pwr = game[1] * game[2] * game[3]
        print("Game ID:", game[0], "Power:", game_pwr)
        powers.append(game_pwr)
    return sum(powers)