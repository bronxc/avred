#!/usr/bin/python3

import pickle
import sys

filename: str = sys.argv[1]
outcome = None
with open(filename, "rb") as input_file:
    outcome = pickle.load(input_file)

print(str(outcome))
