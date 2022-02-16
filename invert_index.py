from bs4 import BeautifulSoup
import indexer
from os import listdir
import json


def get_index():
    count = 0
    result = dict()
    for folder in ['www-db_ics_uci_edu', 'www_cs_uci_edu', 'www_informatics_uci_edu']:
        for file in [f for f in listdir(folder) if f.endswith(".json")]:
            s = str()
            # JSON file
            f = open(folder + '/' + file, "r")
            # Reading from file
            data = json.loads(f.read())

            soup = BeautifulSoup(data['content'], 'html.parser')
            title = soup.find('header', class_='entry-header')
            text = soup.find('div', class_='entry-content')

            if title is not None and text is not None:
                for item in title.find_all(['p', 'h1', 'h2', 'h3', 'b', 'strong']):
                    s += item.text
                for item in text.find_all(['p', 'h1', 'h2', 'h3', 'b', 'strong']):
                    s += item.text

            tokens = indexer.tokenize(s)
            count += 1
            if not tokens:
                print(data['url'])
            result = indexer.build_index(tokens, data['url'])


# if __name__ == "__main__":
#     get_index()
