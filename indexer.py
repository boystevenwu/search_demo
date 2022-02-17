import math
import re
from collections import defaultdict
import json
import math

freq = {}
total_number_documents = 1988


def tokenize(file_text):
    listt = []
    lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', file_text)
    listt += lineplus.lower().split()

    return listt


def build_index(ls, url):
    global freq

    # build a dictionary for all the words with respective tf
    for word in ls:
        if word not in freq.keys():
            freq[word] = dict()

        if url in freq[word].keys():
            freq[word][url] += 1 / len(ls)
        else:
            freq[word][url] = 1 / len(ls)


def calculate_tf_idf(tf):
    result = dict()

    for token in tf.keys():
        result[token] = dict()
        for url in tf[token]:
            result[token][url] = (tf[token][url] * math.log(total_number_documents / len(tf[token].keys())))

    # write the result inside a json file
    with open('posting.json', 'w') as file:
        json.dump(result, file)

    return result
