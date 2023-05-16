import Valija
from datetime import date
from tkinter import filedialog
import pandas as pd
import PySimpleGUI as sg



Valija.main()
file_path = filedialog.askopenfilename(title="Selecciona 'Calidad de la Orden'", filetypes=(("Archivo CSV", "*.csv"),))

barcode_list = Valija.barcode_list
no_valija = Valija.no_valija

#example =['DESTRUMPNOV', '16004343', '16004344', 'DE-23-001', 'REEN-16004344']
hoy = date.today()

df = pd.read_csv(file_path)
df = df.iloc[:, [1, 2, 20, 24, 23, 33, 32]]

formato_path = r'C:\Users\Mayo\Downloads\Valija\Archivos\SGC-000614 Relación de Acuses de Recibo Enviados.xlsx'
formato = pd.read_excel(formato_path)
book = pd.ExcelFile(formato_path)

limpiar = pd.DataFrame(index=range(100), columns=range(12))
limpiar = limpiar.fillna('')

not_found = [code for code in barcode_list if code not in df['ID_de_envío'].values]
if not_found:
    sg.popup(f"No se encontraron {len(not_found)} archivos: {', '.join(not_found)}")

new_barcode_list = [code for code in barcode_list if code not in not_found]
if new_barcode_list:
    new_df = df.loc[df['ID_de_envío'].isin(new_barcode_list)]
    new_df['No'] = range(1, len(new_df) + 1)
    new_df['No. Factura'] = 'N/A'
    new_df['No. Valija'] = no_valija
    new_df['Fecha de registro de evidencia'] = hoy

    new_df = new_df.iloc[:, [7, 0, 1, 2, 3, 4, 6, 5, 10, 8, 9]]
    new_df.columns = ['No', 'Division', 'Delivery', 'Destino', 'Municipio', 'Estado', 'Fecha de embarque', 'Fecha de entrega', 'Fecha de registro de evidencia', 'No. Factura', 'No. Valija']

    with pd.ExcelWriter(formato_path, mode='a', if_sheet_exists='new') as writer:
        limpiar.to_excel(writer, sheet_name='VALIJA GENERAL NUEVA', startrow=4, startcol=0, header=None, index=None)
        df.to_excel(writer, sheet_name='VALIJA GENERAL NUEVA', startrow=4, startcol=0, header=None, index=None)


    print("¡Se ha completado la escritura del archivo!")
else:
    sg.popup("Todos los códigos de barras no se encontraron en el archivo, no se puede continuar con el proceso.")
