import json
import search


if __name__ == "__main__":
    # run this file to start the user interface (GUI) for query searching
    with open('posting_test.json') as f:
        json = json.load(f)

    search.launch(json)
