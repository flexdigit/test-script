#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
print_file.py

Description:
    This Python script reads the contents of a file specified by the user and prints it to the console.

Usage:
    python print_file.py <file_path>

Arguments:
    <file_path> : Path to the text file whose contents are to be printed.

Date:
    March 2025

Version:
    1.0

Example:
    python print_file.py /path/to/your/file.txt
"""

import sys

def print_file_contents(file_path):
    """
    Reads and prints the contents of the specified file.

    Args:
        file_path (str): Path to the file to be read.
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_file.py <file_path>")
    else:
        file_path = sys.argv[1]
        print_file_contents(file_path)

