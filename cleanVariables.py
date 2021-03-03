'''
Python Script to remove unused variables in pipeline templates
'''

import json
import sys
import os
import argparse

#Add parser arguments
parser = argparse.ArgumentParser()
parser.add_argument("-varFile",help="Location of variable file")
parser.add_argument("-directory",help="location of templates directory")

args = parser.parse_args()

if not args.varFile or not args.directory:
    print("Missing OR wrong arguments. Use -h for help options")
    exit()

InputFilename = args.varFile
directory = args.directory


with open(InputFilename, 'r') as inputFile:
    content = json.loads(inputFile.read())
    for everyKey in list(content):
        counter = 0
        for root, dirs, files in os.walk(directory):
            for each_file in files:
                input_file = os.path.join(directory, each_file)
                with open(input_file, mode='r') as FileHandler:
                    file_content = FileHandler.read()
                if everyKey in file_content:
                    counter = 1

        if counter == 0:
            print('We can delete: ' + str(everyKey))  
            del content[everyKey]

    #print(json.dumps(content, indent=4))

  

with open(InputFilename, 'w') as outputFile:
    outputFile.write(json.dumps(content, indent=4))


