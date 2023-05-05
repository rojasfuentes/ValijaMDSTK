import PySimpleGUI as sg


def main():
    
    layout = [
        [sg.Text('Escanea los códigos de barras:')],
        [sg.InputText(key='-INPUT-'), sg.Button('Agregar', key='-ADD-')],
        [sg.Listbox([], size=(30, 6), key='-LIST-', enable_events=True)],
        [sg.Button('Editar', key='-EDIT-'), sg.Button('Eliminar', key='-DELETE-'), sg.Button('Salir')]
    ]

    window = sg.Window('Valija', layout)

    text_list = []

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Salir':
            print(text_list)
            break

        if event == '-ADD-':
            text = values['-INPUT-']
            if text:
                text_list.append(text[2:])
                window['-LIST-'].update(text_list)
                window['-INPUT-'].update('')

        elif event == '-EDIT-':
            selected = window['-LIST-'].get_indexes()
            if selected:
                text = text_list[selected[0]]
                edited_text = sg.popup_get_text('Editar cadena de texto', text)
                if edited_text:
                    text_list[selected[0]] = edited_text
                    window['-LIST-'].update(text_list)

        elif event == '-DELETE-':
            selected = window['-LIST-'].get_indexes()
            if selected:
                del text_list[selected[0]]
                window['-LIST-'].update(text_list)

    window.close()

if __name__ == '__main__':
    main()
