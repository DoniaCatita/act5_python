import csv
from pathlib import Path
from collections import Counter
from datetime import datetime

def enRango(data):
    formato="%d/%m/%y, %H:%M:%S"
    h= datetime.strptime(data, formato)
    return h.hour in range(0, 12)

def miFiltro(csv_reader, cant=None):
    users = list(filter(lambda x:  enRango(x["Hora"]), csv_reader))
    primer_usuario = users[0]['Nombre completo del usuario']
    apariciones = Counter( map(lambda x: x['Nombre completo del usuario'], users))
    if(cant is None):
        return [(primer_usuario,apariciones[primer_usuario])]  # retorno siempre lista de tuplas para no generar conflicto
    else:
        return apariciones.most_common(cant)
    
file_route = Path('archivos') / 'logs_catedra.csv'
try:
    with open(file_route, encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        x= miFiltro(csv_reader,5)
except (UnicodeDecodeError, ValueError, KeyError):
    print(f"Error: el formato del archivo es incorrecto")
except FileNotFoundError:
    print(f"Error: el archivo no existe")
except Exception as e:
    print(f"Error inesperado ({e})")
else: 
    for elem in x:
        print(f'Usuario: {elem[0]} - Cantidad: {elem[1]}')