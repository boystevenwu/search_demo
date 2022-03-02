import math
import re
from collections import defaultdict
import json
import math
from nltk.stem import PorterStemmer

freq = {}
total_number_documents = 1127

ps = PorterStemmer()


def tokenize(file_text):
    # tokenize the sentence into words
    listt = []
    lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', file_text)
    for item in lineplus.lower().split():
        listt.append(ps.stem(item))
    return listt


def build_index(ls, url):
    global freq

    # stop_words list that will have lower weights
    op = open('./stopword.txt', "r", encoding="utf-8")

    stop_words = set()
    for a in op:
        lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', a)
        for item in lineplus.lower().split():
            stop_words.add(ps.stem(item))

    # build a dictionary for all the words with respective tf
    for word in ls:
        if word not in freq.keys():
            freq[word] = dict()

        if word in stop_words:
            if url in freq[word].keys():
                freq[word][url] += 0.05 / len(ls)
            else:
                freq[word][url] = 0.05 / len(ls)
        else:
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
    with open('posting.json', 'w') as file:
        json.dump(result, file)

    return result
