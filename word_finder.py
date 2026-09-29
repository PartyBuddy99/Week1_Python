import sys 
import logging

filename = sys.argv[1]
word = sys.argv[2]

count = 0

try:
    with open(filename) as f:
        for line in f:
            if(word in line):
                count = count + 1
    print(count)
except Exception as e:
    print("Error: ",e)
logging.info(f"{filename}: word '{word}' found {count} times")    
logging.basicConfig(filename="finder.log", level=logging.INFO, format="%(asctime)s - %(message)s")
