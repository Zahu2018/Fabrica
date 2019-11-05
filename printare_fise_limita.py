"""PREGATIRE PENTRU PRINTAT FISE LIMITA."""


import os


"""{'Author': 'Florian Zah',
'Contact': '',
'Copyright': '',
'Credits': '',
'Date': '05.11.2019',
'Description': "Pune fisele limita dintr-o luna intr-un singur fisier pentru\
                a fi printate. ATENTIE sa fie doar fise limita Nu si altceva.",
'Last Modification': '27.09.2019',
'Licence': '',
'Maintainer': 'Florian Zah',
'Status': 'Production',
'Tags': ['fise limita', 'fl', 'printat', 'pregatit'],
'Title': 'PREGATIRE PENTRU PRINTAT FISE LIMITA',
'Version': '1.0.0'}.
"""

# FISE LIMITA CONSUM: font = 22
# DATA: font = 14
# MAISTRII: font = 12 (opitional)

header = """
,,,,,,,,,,,,,,,,FISA LIMITA DE CONSUM
,,,,,,,,,,,,,,,,{}.{},


"""

semnaturi = """


,,,,,,,,,,,Semnatura magazioner,,,,Semnatura maistrii croit,,,,Semnatura maistrii cusut

,,,,,,,,,,,Stefan Pop ______________,,,,Szilagiy Attila ______________,,,,Lacatus Florina ______________

,,,,,,,,,,,,,,,,,,,Pop Anamaria ______________

,,,,,,,,,,,,,,,,,,,Pop Mariana ______________
"""


def citeste_fisiere_csv():
    lista_csv_uri = [i for i in os.listdir() if i[-4:] == ".csv"]
    print(lista_csv_uri, len(lista_csv_uri))
    return lista_csv_uri


def citeste_fisierul_csv(fila):
    data = fila[0:5]
    with open(fila, 'r') as fila:

        _ = fila.read()
        return _, data


def append_fisierul_csv(continut, data):
    with open('de_printat.csv', 'a') as fila:

        fila.write(header.format(data, '2019'))
        fila.write(continut)
        fila.write(semnaturi)


def main():
    lista_csv_uri = citeste_fisiere_csv()
    for item in lista_csv_uri:
        _, data = citeste_fisierul_csv(item)
        append_fisierul_csv(_, data)


main()
