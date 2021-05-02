import csv, json

def start():
    with open('data/universities_ranking.json') as data2:
        listado = json.load(data2)
    
        listado = [[univ['title'],
                    univ['location'],
                    float(univ['perc intl students'].replace('%', '.0'))] for univ in listado]
        listado = sorted(listado, key = lambda pct_int: pct_int[1], reverse=True)[:10]

        with open('data/resultados_data2.json', 'w') as result2:
            json.dump(listado, result2)