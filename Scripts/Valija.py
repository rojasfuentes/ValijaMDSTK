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
        [sg.Listbox([], size=(30, 6), key='-LIST-', enable_events=True)],
        [sg.Button('Editar', key='-EDIT-'), sg.Button('Eliminar', key='-DELETE-'), sg.Button('Salir'),]
    ]

    window = sg.Window('Valija', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Salir':
            no_valija = values['-VALIJA-']
            print(no_valija)
            break

        if event == '-ADD-':
            text = values['-INPUT-']
            if text:
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

    window.close()

if __name__ == '__main__':
    main()
