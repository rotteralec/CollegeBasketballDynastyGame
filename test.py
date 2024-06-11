import pandas as pd



global expo
expo = []

with open("Programs.txt") as f:
    for line in f:
        line = line.split(" ")
        print(line)

