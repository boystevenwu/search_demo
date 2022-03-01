from bs4 import BeautifulSoup
import indexer
from os import listdir
import json


def get_index():
    count = 0
    for folder in ['www-db_ics_uci_edu', 'www_cs_uci_edu', 'www_informatics_uci_edu']:
        for file in [f for f in listdir(folder) if f.endswith(".json")]:
            # JSON file
            f = open(folder + '/' + file, "r")
            # Reading from file
            data = json.loads(f.read())

            if '#' not in data['url']:
                # locate the portion of texts inside the html
                soup = BeautifulSoup(data['content'], 'html.parser')
                title = soup.find('header', class_='entry-header')
                text_1 = soup.find('div', id='content')
                text_2 = soup.find('div', class_='entry-content')
                text_3 = soup.find('body')

                # parse all the text and get the tokens
                s = str()
                for content in [title, text_3, text_2, text_1]:
                    if content is not None:
                        for item in content.find_all(['h1', 'h2', 'h3', 'strong']):
                            s += item.text * 3
                        for item in content.find_all(['p', 'b', 'center']):
                            s += item.text
                tokens = indexer.tokenize(s)

                count += 1
                if not tokens:
                    print(data['url'])

                # calculate tf-idf score in each url for each token
                # build_index and calculate_tf_idf function is inside indexer.py
                indexer.build_index(tokens, data['url'])
    print('page count: ', count)
    indexer.calculate_tf_idf(indexer.freq)


if __name__ == "__main__":
    get_index()
