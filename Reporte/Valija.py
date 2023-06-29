import PySimpleGUI as sg

barcode_list = []
no_valija = ''

def main():
    global no_valija
    global barcode_list

    layout = [
        [sg.Text('Número de Valija:'), sg.InputText(key='-VALIJA-')],
        [sg.Text('Escanea los códigos de barras:')],
        [sg.InputText(key='-INPUT-'), sg.Button('Agregar', key='-ADD-')],
        [sg.Text('Agrega una lista:'), sg.Button('Agregar Lista', key='-ADDLIST-')],
        [sg.Listbox([], size=(30, 6), key='-LIST-', enable_events=True)],
        [sg.Button('Editar', key='-EDIT-'), sg.Button('Eliminar', key='-DELETE-'), sg.Button('Continuar')],
    ]

    window = sg.Window('Valija', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Continuar':
            no_valija = values['-VALIJA-']
            print(no_valija)
            break

        if event == '-ADD-':
            text = values['-INPUT-']
            if text:
                text = text.replace("'", "-")
                text = text.upper()
                barcode_list.append(text[2:])
                window['-LIST-'].update(barcode_list)
                window['-INPUT-'].update('')

        elif event == '-EDIT-':
            selected = window['-LIST-'].get_indexes()
            if selected:
                text = barcode_list[selected[0]]
                edited_text = sg.popup_get_text('Editar cadena de texto', text)
                if edited_text:
                    barcode_list[selected[0]] = edited_text
                    window['-LIST-'].update(barcode_list)

        elif event == '-DELETE-':
            selected = window['-LIST-'].get_indexes()
            if selected:
                del barcode_list[selected[0]]
                window['-LIST-'].update(barcode_list)

        elif event == '-ADDLIST-':
            input_layout = [
                [sg.Multiline(size=(30, 6), key='-LISTINPUT-')],
                [sg.Button('Listo', key='-LISTDONE-')]
            ]

            input_window = sg.Window('Agregar Lista', input_layout)

            while True:
                event, input_values = input_window.read()

                if event == sg.WINDOW_CLOSED or event == '-LISTDONE-':
                    input_list = input_values['-LISTINPUT-'].split('\n')
                    barcode_list.extend([item.strip() for item in input_list if item.strip()])
                    window['-LIST-'].update(barcode_list)
                    break

            input_window.close()

    window.close()

if __name__ == '__main__':
    main()
