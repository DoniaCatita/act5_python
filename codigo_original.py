import csv
from pathlib import Path
from collections import Counter
from datetime import datetime
def enRango(data):
    formato="%d/%m/%y, %H:%M:%S"
    h= datetime.strptime(data, formato)
    return h.hour in range(0, 12)
def miFiltro(csv_reader, cant):
    users = filter(lambda x:  enRango(x["Hora"]), csv_reader)
    return Counter( map(lambda x: x['Nombre completo del usuario'], users)).most_common(cant)

file_route = Path('archivos') / 'logs_catedra.csv'
with open(file_route) as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    x= miFiltro(csv_reader, 5)
for elem in x:
    print(f'Usuario: {elem[0]} - Cantidad: {elem[1]}')
