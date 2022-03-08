import indexer
import PySimpleGUIWeb as sg
from collections import defaultdict
from nltk.stem import PorterStemmer
import timeit


def search(query, index):
    # if the tokens inside the query exists in our token list, we return the result
    if query in index:
        return index[query]
    else:
        return {}


ps = PorterStemmer()


def launch(data):
    # user interface GUI
    layout = [[sg.Text("An Answer Gained")],
              [sg.Input(size=(45, 1), key='INPUT'), sg.Button(size=(5, 1), button_text='Gain')],
              [sg.Text("")],
              [sg.Input(size=(55, 1), key='0')],
              [sg.Input(size=(55, 1), key='1')],
              [sg.Input(size=(55, 1), key='2')],
              [sg.Input(size=(55, 1), key='3')],
              [sg.Input(size=(55, 1), key='4')]]

    window = sg.Window('An Answer Gained', layout, element_justification='c', web_port=2222, web_start_browser=False)

    print("Please visit http://127.0.0.1:2222/")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        # as we click the 'Gain' button, the results will come out
        if event == 'Gain':
            start = timeit.default_timer()
            final_set, temp_set = set(), set()

            # stemming for all the words in the queries
            ls_token = indexer.tokenize(values['INPUT'])
            print('Tokens:', ls_token, end=' ')
            flag = True
            for item in ls_token:
                if flag:
                    final_set = set(search(item, data).keys())
                    flag = False
                else:
                    temp_set = set(search(item, data).keys())
                    final_set = final_set & temp_set

            result = defaultdict(int)
            # put all urls satisfied the required query along with their scores inside the dictionary
            for item in ls_token:
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

            # calculate query execution time
            stop = timeit.default_timer()
            print('Time: ', stop - start, '\n')
