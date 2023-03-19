#!/usr/bin/env python
"""A script that cleans and normalizes the data obtained from the CHILDES corpus."""


import argparse
import re


def get_data(path: str) -> list:
    """reads the data into a list of strings"""
    list_of_lines = []
    with open(path, "r") as source:
        for line in source:
            if not line:
                continue
            else:
                list_of_lines.append(line.lstrip().rstrip())
    return list_of_lines


def part1(data: list) -> list:
    """removes strings starting with '&', '+', '-', or a digit"""
    for token in data:
        if token.startswith(("&", "+", "-")) or token[0].isdigit():
            data.remove(token)
    return data


def part4(data: list) -> list:
    """removes the 'special code'"""
    for token in data:
        if ord(token[0]) == 21 or ord(token[-1]) == 21:
            data.remove(token)
    return data


def writelines(data: list, path: str) -> None:
    """iterates over a list of strings and outputs them into a file"""
    with open(path, "w") as sink:
        for item in data:
            print(item, file=sink)


def main(args: argparse.Namespace) -> None:
    data_to_clean = get_data(args.input)
    cleaned_data = []
    for item in data_to_clean:
        # removes the parentheses but leaves their content
        no_parentheses = re.sub(r"[()]", "", item)
        # removes the chevrons but leaves their content
        no_chevrons = re.sub(r"[<>]", "", no_parentheses)
        # removes the brackets and their content
        no_brackets = re.sub(r"\[.*?\]", "", no_chevrons)
        # removes the '*MOT: ' marker from utterance line
        no_MOT_markers = re.sub(r"^.{6}", "", no_brackets)
        # splits the line by whitespace to implement custom functions
        split = no_MOT_markers.split() # returns a list of strings
        first_bullet = part1(split)
        fourth_bullet = part4(first_bullet)
        # rejoins the utterance by whitespace
        concatenated = " ".join(fourth_bullet)
        # removes all punctuation except the apostrophes
        no_punctuation = re.sub(r"[^\w\d'\s]+",'',concatenated)
        # removes duplicated whitespace
        single_whitespace = re.sub(r"\s+", " ", no_punctuation)
        # appends cleaned utterance to a list
        cleaned_data.append(single_whitespace.lstrip().rstrip().casefold())
    writelines(cleaned_data, args.output)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="path to the input file")
    parser.add_argument("--output", help="path to the output file")
    main(parser.parse_args())
