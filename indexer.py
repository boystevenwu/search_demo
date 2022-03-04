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
    # stemming every word for similar words
    for item in lineplus.lower().split():
        listt.append(ps.stem(item))
    return listt


def build_index(tokens, url):
    global freq

    # stop_words list that will be counted with lower weights
    with open('./stopwords.txt', "r", encoding="utf-8") as f:
        stop_words = set()
        for line in f:
            lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', line)
            for item in lineplus.lower().split():
                stop_words.add(ps.stem(item))

    # # ignore stopwords if they are over 2/3 of the sentence
    # if len(stop_words) / len(tokens) > (2 / 3):
    #     stop_words = set()

    # build a dictionary for all the words with respective tf
    for word in tokens:
        if word not in freq.keys():
            freq[word] = dict()

        # if the word in the query is a stop word, then we will regard it as 1/20 regular word.
        if word in stop_words:
            if url in freq[word].keys():
                freq[word][url] += 0.05 / len(tokens)
            else:
                freq[word][url] = 0.05 / len(tokens)
        else:
            if url in freq[word].keys():
                freq[word][url] += 1 / len(tokens)
            else:
                freq[word][url] = 1 / len(tokens)


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
