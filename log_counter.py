import sys

filename = sys.argv[1]

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}

with open(filename) as f:
    for line in f:
        if "INFO" in line:
            counts["INFO"] = counts["INFO"] + 1
        elif "WARNING" in line:
            counts["WARNING"] = counts["WARNING"] + 1
        elif "ERROR" in line:
            counts["ERROR"] = counts["ERROR"] + 1
        elif "DEBUG" in line:
            counts["DEBUG"] = counts["DEBUG"] + 1

print(counts)