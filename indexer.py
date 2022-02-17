import math
import re
from collections import defaultdict
import json
import math

freq = {}
total_number_documents = 27


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
            freq[word][url] += 1 / len(ls)
        else:
            freq[word][url] = 1 / len(ls)

    for token in freq.keys():
        for url in freq[token]:
            print(freq[token][url])
            freq[token][url] = freq[token][url] * math.log(total_number_documents / len(freq[token].keys()))
            if freq[token][url] > 3.5:
                print()
                print(math.log(total_number_documents / len(freq[token].keys())))
                print(freq[token][url])
                print()

    # write the result inside a json file
    with open('posting.json', 'w') as file:
        json.dump(freq, file)

    return freq
