#!/usr/bin/env python
#------------------------------------------------------
#      BY: r0achezsEk
#      MODIFIED: Evil Username Generator
#------------------------------------------------------
from platform import python_version
from sys import exit, argv
from argparse import ArgumentParser
from os import system
import itertools

# Check Python version
version = python_version().startswith('2', 0, len(python_version()))
if version:
    print('Are you using python version {}\n'
          'Please, use version 3.X of python'.format(python_version()))
    exit(1)

# Define colors
RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'

# Extended Unicode replacements for usernames
unicodes = [{'a':'\u0430'},  # Cyrillic Small Letter A
            {'c': '\u03F2'}, # Greek Lunate Sigma Symbol
            {'e':'\u0435'},  # Cyrillic Small Letter Ie
            {'o':'\u043E'},  # Cyrillic Small Letter O
            {'p':'\u0440'},  # Cyrillic Small Letter Er
            {'s':'\u0455'},  # Cyrillic Small Letter Dze
            {'d':'\u0501'},  # Cyrillic Small Letter Komi De
            {'q':'\u051B'},  # Cyrillic Small Letter Qa
            {'w':'\u051D'}]  # Cyrillic Small Letter We

# Display tool banner
def message():
    system('clear')
    print(f"{RED}Evil Username Generator{END}\n")

# Clean text from color codes
def cleanTxt(txt):
    for i in (RED, WHITE, GREEN, END, YELLOW):
        txt = txt.replace(i, '')
    return txt

# Clean the output file
def cleanFile(output):
    with open(output, 'w') as arq:
        arq.write('')

# Display and log the output
def printParser(txt, output=False):
    print(txt)
    if output:
        with open(output, 'a') as arq:
            arq.write(cleanTxt(txt) + '\n')

# Generate variations of the username
def generate_username(username, output=False):
    evils = [{'a':'\u0430'}, {'c': '\u03F2'}, {'e': '\u0435'}, {'o': '\u043E'}, 
             {'p': '\u0440'}, {'s': '\u0455'}, {'d': '\u0501'}, {'q': '\u051B'}, {'w': '\u051D'}]

    e_matchs = [key for item in evils for key in item if key in username.lower()]
    
    variations = []
    for i in range(1, len(e_matchs) + 1):
        for combo in itertools.combinations(e_matchs, i):
            new_username = username
            for letter in combo:
                for evil in evils:
                    if letter in evil:
                        new_username = new_username.replace(letter, evil[letter])
            variations.append(new_username)

    # Print and log the generated usernames
    for variation in variations:
        printParser(f'{GREEN}[*]{END} Evil Username: {RED}{variation}{END}', output)

# Handle arguments
def parseHandler():
    parser = ArgumentParser(usage="evil_username.py [options]", description="Generate evil Unicode usernames.")
    parser.add_argument("-l", dest="list_of_usernames", help="List of usernames to generate evil variations for", nargs='+')
    parser.add_argument("-o", dest="output", help="Save generated usernames to a file")

    if len(argv) == 1:
        parser.print_help()
        exit(1)

    args = parser.parse_args()
    usernames = args.list_of_usernames
    output = args.output

    if output:
        cleanFile(output)
        message()

    if usernames:
        for username in usernames:
            printParser(f'{GREEN}[+]{END} Generating for: {username}', output)
            generate_username(username, output)

if __name__ == '__main__':
    try:
        message()
        parseHandler()
    except KeyboardInterrupt:
        exit()
