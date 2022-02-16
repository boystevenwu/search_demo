import re
from collections import defaultdict
import json

freq = {}


def tokenize(file_text):
    listt = []
    lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', file_text)
    listt += lineplus.lower().split()

    return listt


def build_index(ls, url):
    global freq

    # build a dictionary for all the words
    for word in ls:
        if word not in freq.keys():
            freq[word] = defaultdict(int)

        if url in freq[word].keys():
            freq[word][url] += 1
        else:
            freq[word][url] = 1

    # write the result inside a json file
    with open('posting.json', 'w') as file:
        json.dump(freq, file)

    return freq
