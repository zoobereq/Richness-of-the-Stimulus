#!/usr/bin/env python
"""A script that iterates over the CHILDES corpus.  
It isolates instances of caregiver's speech (indicated by '*MOT:') and outputs them into a separate text file."""

import argparse
import os


def listfiles(root: str) -> list:
    """lists all files in the specified directory"""
    filelist = []
    for subdirectory, directories, files in os.walk(root):
        for file in files:
            filepath = os.path.join(subdirectory, file)
            filelist.append(filepath)
    return filelist


def getlines(input: str) -> list:
    """isolates the desired lines and aggregates them into a list of strings"""
    lines = []
    with open(input, "r") as source:
        for line in source:
            if line == False:
                continue
            if line.startswith("*MOT:"):
                lines.append(line.rstrip())
    return lines


def writelines(data: list, path: str) -> None:
    """iterates over a list of strings and outputs them into a file"""
    with open(path, "w") as sink:
        for item in data:
            print(item, file=sink)


def main(args: argparse.Namespace) -> None:
    alllines = []
    filelist = listfiles(args.input)
    for file in filelist:
        targetlines = getlines(file)
        for line in targetlines:
            alllines.append(line)
    writelines(alllines, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="root directory path")
    parser.add_argument("--output", help="path to output")
    main(parser.parse_args())
