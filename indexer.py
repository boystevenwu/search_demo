import math
import re
from collections import defaultdict
import json
import math
from nltk.stem import PorterStemmer

freq = {}
total_number_documents = 1212

ps = PorterStemmer()

def tokenize(file_text):
    # tokenize the sentence into words
    listt = []
    lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', file_text)
    #print('tokenize:', lineplus.lower().split())
    for item in lineplus.lower().split():
        #print('stem_item:', ps.stem(item))
        listt.append(ps.stem(item))
    #listt += lineplus.lower().split()
        #print('listt:', listt)
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

    # update the tf-idf score by multiply the tf score above with the idf score
    for token in tf.keys():
        result[token] = dict()
        for url in tf[token]:
            result[token][url] = (tf[token][url] * math.log(total_number_documents / len(tf[token].keys())))

    # write the result inside a json file
    with open('posting_test.json', 'w') as file:
        json.dump(result, file)

    return result
