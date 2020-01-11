
#  Importing JSON and SequenceMatcher from the difflib library.

import json
from difflib import get_close_matches

#  Opening  the attached JSON file. 

data = json.load(open("data.json"))

#  Function that looks up the input and returns a definition from the JSON file.  Includes many else statements if the input might be incorrect.

def lookup(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif len(get_close_matches(x, data.keys())) > 0:
        yes_no = input("Did you mean %s instead? Enter y if yes, or n if no: " % get_close_matches(x, data.keys())[0])
        if yes_no == "y":
            return data[get_close_matches(x, data.keys())[0]]
        else:
            word = input("Enter another word: ")

#  Takes an input from the user.

word = input("Enter word: ")

#   Checks the dictionary 

output = lookup(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
