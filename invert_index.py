from bs4 import BeautifulSoup
import indexer
from os import listdir
import json


def get_index():
    count = 0
    result = dict()
    for folder in ['www-db_ics_uci_edu', 'www_cs_uci_edu', 'www_informatics_uci_edu']:
        for file in [f for f in listdir(folder) if f.endswith(".json")]:
            # JSON file
            f = open(folder + '/' + file, "r")
            # Reading from file
            data = json.loads(f.read())

            soup = BeautifulSoup(data['content'], 'html.parser')
            title = soup.find('header', class_='entry-header')
            text_1 = soup.find('div', id='content')
            text_2 = soup.find('div', class_='entry-content')
            text_3 = soup.find('body')

            s = str()
            for content in [title, text_3, text_2, text_1]:
                if content is not None:
                    for item in content.find_all(['p', 'h1', 'h2', 'h3', 'b', 'strong', 'center']):
                        s += item.text
            tokens = indexer.tokenize(s)

            count += 1
            if not tokens:
                print(data['url'])
            indexer.build_index(tokens, data['url'])

    indexer.calculate_tf_idf(indexer.freq)


if __name__ == "__main__":
    get_index()
