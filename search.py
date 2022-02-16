import indexer
import PySimpleGUI as sg
from collections import defaultdict


def search(query, index):
    if query in index:
        return index[query]
    else:
        return {}


def launch(data):
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

        if event == 'Gain':
            final_set, temp_set = set(), set()
            flag = True
            for item in indexer.tokenize(values['INPUT']):
                if flag:
                    final_set = set(search(item, data).keys())
                    flag = False
                else:
                    temp_set = set(search(item, data).keys())
                    final_set = final_set & temp_set

            print(final_set)
            result = defaultdict(int)
            for item in indexer.tokenize(values['INPUT']):
                for url in final_set:
                    result[url] += search(item, data)[url]

            sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
            for i in range(5):
                if i < len(list(sorted_result.keys())):
                    window[str(i)].update(list(sorted_result.keys())[i])
                else:
                    window[str(i)].update("")
