import csv, json

def start(year):
    with open('data/world-happiness-report.csv') as data1:
        reader = csv.reader(data1, delimiter = ',')
        encabezados = next(reader)

        listado = [[linea[0],linea[1],linea[2]] for linea in filter(lambda linea: linea[1]==year, reader)]
        listado = sorted(listado, key = lambda pais: pais[2], reverse=True)[:10]

        with open('data/happiest.json', 'w') as result1:
            json.dump(listado, result1)