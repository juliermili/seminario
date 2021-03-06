import csv, json, os

def start():
    with open(os.path.abspath('data/universities_ranking.json')) as data2:
        listado = json.load(data2)
    
        listado = [{'title':univ['title'],
                    'location': univ['location'],
                    'pct': float(univ['perc intl students'].replace('%', '.0'))} 
        for univ in listado]

        listado = sorted(listado, key = lambda univ: univ['pct'], reverse=True)[:10]

        with open(os.path.abspath('data/resultados_data2.json'), 'w') as result2:
            json.dump(listado, result2)