import PySimpleGUI as psgui

import main
import meteorite_data_class


data = open("MeteoriteDataFile.txt", "r")
data.readline()


def run_app():
    layout_list = [
        [psgui.Text('Mass Data Filter')],
        [psgui.Multiline(size=(120, 10), key='Mass Output Box', disabled=True)],
        [psgui.Text('Year Data Filter')],
        [psgui.Multiline(size=(120, 10), key='Year Output Box', disabled=True)],
        [psgui.Button('Apply Filter', size=(20, 2)), psgui.Button('EXIT', size=(20, 2))],
        [psgui.Text('Minimum Year Limit (0 - 2022, exclusive): > '),
         psgui.Input(key='min_year_param', size=6)],
        [psgui.Text('Minimum Mass Limit (grams, exclusive): > '),
         psgui.Input(key='min_mass_param', size=20)], ]

    main_window = psgui.Window(title='Meteorite Data Filter', layout=layout_list, margins=(30, 30))

    while True:
        event, values = main_window.read()

        if event == psgui.WIN_CLOSED or event == 'EXIT':
            break

        if event == 'Apply Filter':

            #clear multiline boxes
            main_window['Mass Output Box'].update("")
            main_window['Year Output Box'].update("")

            min_mass_param: int = values['min_mass_param']
            min_year_param: int = values['min_year_param']

            main.meteor_filter(min_mass_param, min_year_param)

            mass_file = open("mass_filtered_data.txt", "r")
            for i in range(len(main.mass_list)):
                main_window['Mass Output Box'].write(mass_file.readline())

            year_file = open("year_filtered_data.txt", "r")
            for i in range(len(main.year_list)):
                main_window['Year Output Box'].write(year_file.readline())


if __name__ == '__main__':
    run_app()

