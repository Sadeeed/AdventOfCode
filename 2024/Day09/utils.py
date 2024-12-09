def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines]
    return lines
