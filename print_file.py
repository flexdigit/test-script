#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Name: print_files.py
Description: A Python script to read and print the contents of one or more files.
             It accepts a list of file paths as input and prints their contents to the console.
             Errors (e.g., file not found) are handled gracefully.

Usage: python print_files.py <file1> <file2> ...

Version: 1.0
Date: March 2025
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
            print(f"Contents of '{file_path}':")
            print(contents)
            print("-" * 40)  # Separator for better readability
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python print_file.py <file1> <file2> ...")
    else:
        # Get all file paths from command-line arguments (excluding the script name)
        file_paths = sys.argv[1:]
        for file_path in file_paths:
            print_file_contents(file_path)
