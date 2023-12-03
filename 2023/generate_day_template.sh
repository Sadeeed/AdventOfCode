#!/usr/bin/zsh

# This script generates a template for the day's puzzle.
# It creates a directory for the day, and a file for the puzzle input.
# It also creates a file for the puzzle solution, with a template for the
# solution function.

# Usage: ./generate_day_template.sh <day>

# Example: ./generate_day_template.sh 1

if [ "$1" -lt 10 ]
then
  FOLDER_NAME="Day0$1"
else
  FOLDER_NAME="Day$1"
fi
mkdir "$FOLDER_NAME"
touch "$FOLDER_NAME/input.txt"
touch "$FOLDER_NAME/test_input.txt"
touch "$FOLDER_NAME/utils.py"
touch "$FOLDER_NAME/Puzzle01.py"
touch "$FOLDER_NAME/Puzzle02.py"
printf "def get_input(filename):\n    with open(filename) as f:\n        lines = f.readlines()\n        f.close()\n        lines = [line.strip() for line in lines]\n    return lines\n" > "$FOLDER_NAME/utils.py"
