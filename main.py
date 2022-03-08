import json
import search


if __name__ == "__main__":
    # run this file to start the user interface (GUI) for query searching
    with open('posting.json') as f:
        json = json.load(f)

    # lunch the web interface of search engine
    search.launch(json)
