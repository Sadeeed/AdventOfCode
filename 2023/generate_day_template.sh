#!/usr/bin/zsh

# This script generates a template for the day's puzzle.
# It creates a directory for the day, and a file for the puzzle input.
# It also creates a file for the puzzle solution, with a template for the
# solution function.

# Usage: ./generate_day_template.sh <day>

# Example: ./generate_day_template.sh 1

if [ "$1" -lt 10 ]
then
    mkdir "Day0$1"
else
    mkdir "Day$1"
fi
#mkdir "Day0$1"
touch "Day$1/input.txt"
touch "Day$1/test_input.txt"
touch "Day$1/utils.py"
touch "Day$1/Puzzle01.py"
touch "Day$1/Puzzle02.py"
printf "def get_input(filename):\n    with open(filename) as f:\n        lines = f.readlines()\n        f.close()\n    return lines\n" > "Day$1/utils.py"
