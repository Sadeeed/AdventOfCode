from pathlib import Path

test_input_file = Path('./2021/Day05/input_test.txt')
input_file = Path('./2021/Day05/input.txt')
lines = []

with open(input_file) as fp:
    for line in fp:
        lines.append(line.strip('\n').split(' -> '))

def get_overlapping_lines(lines):
    start = list()
    end = list()
    total_covered = set()
    points_covered = set()
    overlap_points = set()

    for line in lines:
        start = list(map(int, line[0].split(',')))
        end = list(map(int, line[1].split(',')))
        if start[0] == end[0]:
            if start[1] > end[1]:
                points_covered = ((start[0],x) for x in range(end[1],start[1]+1))
            elif end[1] > start[1]:
                points_covered = ((start[0],x) for x in range(start[1],end[1]+1))
        elif start[1] == end[1]:
            if start[0] > end[0]:
                points_covered = ((x,start[1]) for x in range(end[0],start[0]+1))
            elif end[0] > start[0]:
                points_covered = ((x,start[1]) for x in range(start[0],end[0]+1))
        else:
            if start[0] > end[0] and start[1] > end[1]:
                points_covered = zip(range(end[0],start[0]+1),range(end[1],start[1]+1))
            elif end[0] > start[0] and  end[1] > start[1]:
                points_covered = zip(range(start[0],end[0]+1),range(start[1],end[1]+1))
            elif start[0] > end[0] and end[1] > start[1]:
                points_covered = zip(range(start[0],end[0]-1,-1), range(start[1],end[1]+1))
            elif end[0] > start[0] and start[1] > end[1]:
                points_covered = zip(range(start[0],end[0]+1), range(start[1],end[1]-1,-1))

        for point in points_covered:
            if point in total_covered:
                overlap_points.add(point)
            else:
                total_covered.add(point)

    print(len(overlap_points))



get_overlapping_lines(lines=lines)