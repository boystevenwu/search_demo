import indexer
import PySimpleGUI as sg
from collections import defaultdict
from nltk.stem import PorterStemmer


def search(query, index):
    # if the tokens inside the query exists in our token list, we return the result
    if query in index:
        return index[query]
    else:
        return {}


ps = PorterStemmer()


def launch(data):
    # user interface GUI
    layout = [[sg.Input(key='INPUT', justification='left'), sg.Button('Gain')],
              [sg.Text("")],
              [sg.Input(size=(55, 1), key='0', readonly=True)],
              [sg.Input(size=(55, 1), key='1', readonly=True)],
              [sg.Input(size=(55, 1), key='2', readonly=True)],
              [sg.Input(size=(55, 1), key='3', readonly=True)],
              [sg.Input(size=(55, 1), key='4', readonly=True)]]

    window = sg.Window('An Answer Gained', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        # as we click the 'Gain' button, the results will come out
        if event == 'Gain':
            final_set, temp_set = set(), set()
            ls_token = indexer.tokenize(values['INPUT'])
            ls_stem = []
            # stemming for all the words in the queries
            for item in ls_token:
                ls_stem.append(ps.stem(item))
            print('ls_stem:', ls_stem)
            flag = True
            for item in ls_stem:
                if flag:
                    final_set = set(search(item, data).keys())
                    flag = False
                else:
                    temp_set = set(search(item, data).keys())
                    final_set = final_set & temp_set

            result = defaultdict(int)
            # put all urls satisfied the required query along with their scores inside the dictionary
            for item in ls_stem:
                for url in final_set:
                    result[url] += search(item, data)[url]

            # reverse ordering the dictionary based on the tf-idf score corresponding to each url for each token
            sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
            print(sorted_result)

            # get top 5 url for each query
            for i in range(5):
                if i < len(list(sorted_result.keys())):
                    window[str(i)].update(list(sorted_result.keys())[i])
                else:
                    window[str(i)].update("")
