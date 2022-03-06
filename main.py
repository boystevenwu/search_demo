import json
import search


if __name__ == "__main__":
    # run this file to start the user interface (GUI) for query searching
    with open('posting.json') as f:
        json = json.load(f)

    # lunch the web interface of search engine
    print("Please visit http://127.0.0.1:2222/")
    search.launch(json)
