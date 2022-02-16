import json
import search


if __name__ == "__main__":
    with open('posting.json') as f:
        json = json.load(f)

    search.launch(json)
